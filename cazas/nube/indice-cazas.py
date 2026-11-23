"""Índice compacto del repo cazas-nube: reemplaza leer enteros bandeja.md y semillas-usadas.md.

Correr desde la raíz del clon. Solo librería estándar (Python 3.8+). No escribe nada.

  python3 cazas/nube/indice-cazas.py bandeja
      Una línea por tarjeta 🎯 (todas las secciones): sección · fecha · sesión · anunciante · page_id · slug.
      Sirve para no duplicar. Las tarjetas sin link a la Library salen con «sin page_id»: cruzalas por nombre.

  python3 cazas/nube/indice-cazas.py hoy [AAAA-MM-DD]
      Texto COMPLETO (tal cual) de lo que el informe Opus tiene que trabajar ese día: la lista
      «🔎 Para re-contar en la PC», las tarjetas con esa fecha y los bloques «Señales del día» de esa fecha.

  python3 cazas/nube/indice-cazas.py semillas <Idioma> [AAAA-MM-DD]
      Huellas del idioma (§1 de semillas.md) en el orden de uso de §0: nunca usadas, después usadas hace 7+ días
      (la más vieja primero). Una huella cuenta como usada si aparece en semillas-usadas.md, en cola.md o en
      RAW/cazas-auto/ (la fecha sale de la fila o del nombre del archivo). Ante la duda, la marca usada:
      puede saltear una semilla, nunca repetir una.

  python3 cazas/nube/indice-cazas.py ya-visto <page_id o nombre> [...]
      Busca en bandeja.md, descartados.md y bandeja-historico.md (si existe) y devuelve las líneas que lo nombran.

  python3 cazas/nube/indice-cazas.py ids
      Todos los page_id ya vistos (bandeja + descartados + histórico), uno por línea.
"""
import re, sys, datetime, pathlib, collections

R = pathlib.Path(".")
RX_PAGE = re.compile(r"view_all_page_id=(\d{10,20})")
RX_FECHA = re.compile(r"\d{4}-\d{2}-\d{2}")
MESES = "ene feb mar abr may jun jul ago sep oct nov dic".split()
FUENTES = ["cazas/bandeja.md", "cazas/descartados.md", "cazas/bandeja-historico.md"]


def leer(f):
    p = R / f
    return p.read_text(encoding="utf-8") if p.exists() else ""


def tarjetas():
    """(sección, cabecera, texto completo) de cada tarjeta 🎯 de la bandeja."""
    seccion, actual, out = "", None, []
    for l in leer("cazas/bandeja.md").splitlines():
        if l.startswith("## ") or l.startswith("<!--") or l.startswith("**Señales del día") or \
           (l.startswith("### ") and not l.startswith("### 🎯")):
            if actual: out.append(actual); actual = None
            if l.startswith("## "): seccion = l[3:].split("(")[0].strip()
        elif l.startswith("### 🎯"):
            if actual: out.append(actual)
            actual = [seccion, l, l + "\n"]
        elif actual:
            actual[2] += l + "\n"
    if actual: out.append(actual)
    return out


def campos(cab):
    p = cab[5:].split(" · ")
    slug = next((x.strip("` ") for x in p if x.strip().startswith("`")), "?")
    fecha = next((x.strip() for x in p if RX_FECHA.fullmatch(x.strip())), "?")
    quien = p[0].split(" — ")[-1].strip() if " — " in p[0] else p[0].strip()
    return fecha, p[-1].strip(), quien, slug


def bandeja():
    n = 0
    for sec, cab, txt in tarjetas():
        fecha, sesion, quien, slug = campos(cab)
        ids = [i for i, _ in collections.Counter(RX_PAGE.findall(txt)).most_common(1)]   # el anunciante de la tarjeta
        print(f'{sec} · {fecha} · {sesion} · {quien} · {ids[0] if ids else "sin page_id"} · {slug}')
        n += 1
    print(f"{n} tarjetas")


def hoy(fecha):
    d = datetime.date.fromisoformat(fecha)
    corta = f"{d.day}-{MESES[d.month - 1]}"                     # «23-nov», como en «Señales del día ES (23-nov, …)»
    txt = leer("cazas/bandeja.md").splitlines()
    out, dentro = [], False
    for l in txt:                                              # lista «Para re-contar», tal cual
        if l.startswith("### 🔎 Para re-contar"):
            dentro = True
        elif dentro and (l.startswith("### ") or l.startswith("## ")):
            break
        if dentro:
            out.append(l)
    print("\n".join(out) + "\n")
    for sec, cab, t in tarjetas():                             # tarjetas del día, completas
        if campos(cab)[0] == fecha:
            print(t.rstrip() + "\n")
    bloque = None                                              # señales del día, completas
    for l in txt + [""]:
        if l.startswith("**Señales del día"):
            if bloque: print("\n".join(bloque) + "\n")
            bloque = [l] if (corta in l or fecha in l) else None
        elif bloque is not None:
            if l.startswith("<!--") or l.startswith("### ") or l.startswith("## "):
                print("\n".join(bloque) + "\n"); bloque = None
            else:
                bloque.append(l)
    if bloque: print("\n".join(bloque))


def semillas(idioma, fecha):
    hoy_ = datetime.date.fromisoformat(fecha)
    sec1 = leer("cazas/nube/semillas.md").split("## 1.", 1)[1].split("\n## ", 1)[0]
    b = re.search(r"\*\*" + re.escape(idioma) + r"[^*]*\*\*[^\n]*\n(.*?)(?:\n\s*\n|\n\*\*)", sec1, re.S)
    if not b:
        sys.exit(f"No encontré «{idioma}» en semillas.md §1. Idiomas: " + ", ".join(re.findall(r"\*\*([^*(]+?) \(", sec1)))
    huellas = re.findall(r"`([^`]+)`", b.group(1))
    # (fecha o None, texto en minúsculas) de cada lugar donde una keyword queda registrada como usada
    registros = []
    for l in leer("cazas/semillas-usadas.md").splitlines():
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) >= 5 and RX_FECHA.fullmatch(c[0]):
            registros.append((c[0], (c[3] + " | " + c[4]).lower()))
    for l in leer("cazas/cola.md").splitlines():
        m = [d for d in RX_FECHA.findall(l) if d <= fecha]        # las fechas futuras de la cola son agenda, no uso
        registros.append((max(m) if m else None, l.lower()))
    for f in sorted((R / "RAW/cazas-auto").glob("*.md")):
        m = RX_FECHA.match(f.name)
        registros.append((m.group(0) if m else None, f.read_text(encoding="utf-8").lower()))
    corte = (hoy_ - datetime.timedelta(days=7)).isoformat()
    nunca, viejas, sin_fecha, frenadas = [], [], [], []
    for h in huellas:
        fechas = [d for d, t in registros if h.lower() in t]
        if not fechas:
            nunca.append(h)
        elif any(d is None for d in fechas) and not [d for d in fechas if d]:
            sin_fecha.append(h)
        else:
            u = max(d for d in fechas if d)
            (viejas if u <= corte else frenadas).append((h, u))
    viejas.sort(key=lambda x: x[1])
    print(f"{idioma}: {len(huellas)} huellas · corte {corte}")
    print("1. Nunca usadas:", " · ".join(nunca) or "—")
    print("2. Usadas hace 7+ días:", " · ".join(f"{h} ({u})" for h, u in viejas) or "—")
    print("3. Usadas, sin fecha (solo si faltan):", " · ".join(sin_fecha) or "—")
    print("No usar todavía:", " · ".join(f"{h} ({u})" for h, u in frenadas) or "—")
    if len(nunca) + len(viejas) < 10:
        print(f"AVISO: quedan {len(nunca) + len(viejas)} huellas disponibles en {idioma} -> anotarlo en log-nube.md para sumar más")


def ya_visto(terminos):
    for t in terminos:
        hits = [f"{f}:{i}: {l.strip()[:200]}" for f in FUENTES for i, l in enumerate(leer(f).splitlines(), 1)
                if t.lower() in l.lower()]
        print(f"«{t}»: " + ("no aparece" if not hits else f"{len(hits)} líneas"))
        for h in hits[:8]:
            print("  " + h)


def ids():
    print("\n".join(sorted({i for f in FUENTES for i in RX_PAGE.findall(leer(f))} |
                           {i for f in FUENTES for i in re.findall(r"`(\d{13,17})`", leer(f)) if f.endswith("descartados.md")})))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
    a = sys.argv[1:]
    hoy_iso = datetime.date.today().isoformat()
    if not a:
        sys.exit(__doc__)
    elif a[0] == "bandeja":
        bandeja()
    elif a[0] == "hoy":
        hoy(a[1] if len(a) > 1 else hoy_iso)
    elif a[0] == "semillas" and len(a) >= 2:
        semillas(a[1], a[2] if len(a) > 2 else hoy_iso)
    elif a[0] == "ya-visto" and len(a) >= 2:
        ya_visto(a[1:])
    elif a[0] == "ids":
        ids()
    else:
        sys.exit(__doc__)
