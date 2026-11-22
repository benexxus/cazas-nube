# Caza automática — ES · lint de la cola + embudo con semillas — 2026-11-22 (dom 04:04, Europe/Madrid)

Países: CO MX ES CL PE. Evidencia: API (`ads_library_search`) + `firecrawl_scrape` de 2 snapshots (Digi Aprende). Relojes: hoy ≈ epoch 1795310000; cohorte 7+ = `ad_creation_time` ≤ 1794705000.

## Lint de la cola (ES)
Sin hallazgos: ningún nodo ES sin tocar > 30 días (el más viejo es del 2026-11-20), ningún 🟡 vencido y ningún re-conteo con fecha ≤ 2026-11-22 (el primero de ES es 2026-11-27). Nodos excluidos intactos.

## Shortlist
**1 tarjeta — Digi Aprende (`308598599011471`), «+350 mapas mentales de farmacología», 🇵🇪.**
- 🇵🇪 **19 / 39** sobrevivientes (ACTIVE; `ALL` también da 39 → no hay ofertas apagadas en este país). Creados: 2026-10-11 (2 ads), 2026-10-22 (16 ads, un solo lote), 2026-11-04 (1), 2026-11-19 (6), 2026-11-21/22 (16). ≥ 3 fechas distintas y ≥ 1 ad de los últimos 30 días → no es zombi. Longevidad por API del ad más viejo: ~41 d; snapshot verificado con Firecrawl (la Biblioteca lo muestra «Active»).
- Otros países de la sesión: CO 0 · MX 0 · ES 0 · CL 0 (ACTIVE, `page_ids` + país). Solo apareció en 🇵🇪 (los 4 subagentes la vieron únicamente ahí).
- Copy (snapshot 872737229226638 y 1741552156948738): «+350 mapas mentales de farmacología ilustrada… para estudiantes de Farmacia, Medicina, Enfermería, Nutrición», «Todo en PDF, a color, descargable e imprimible», «3 bonos de regalo», «Envíanos un mensaje por WhatsApp y obtenlos en 2 minutos» (CTA «Send WhatsApp message», `api.whatsapp.com`). **Precio: no dicho en el copy** (piso n/e).
- Ficha WA: vende = pack PDF de 350+ mapas de farmacología · promesa = repasar mecanismos, indicaciones, efectos adversos, dosis · dolor = farmacología «demasiada información» · precio dicho = n/e · bonos = 3 sin nombrar · teléfono/mensaje prellenado = no visible (Firecrawl no abre el destino de WhatsApp) · no se sabe = precio, contenido exacto, escalera, garantía · escalera n/e.
- Marca personal: página «Digi Aprende», sin cara ni nombre de persona en los 39 ads ni en el snapshot (solo logo). Gate: A ✅ · B (WhatsApp con la oferta en el copy) ✅ · D (PDF) ✅ · no excluido ✅.
- Duplicación (③): «Descárgalo HOY / Descárgalo en 2 minutos» repetido ~29 veces entre los sobrevivientes. Score: ① no (41 d < 45) · ② no (19 < 50) · ③ sí · ④ sin dato → **1/4**.
- Molde en otros mercados (señales, no tarjeta): Estudia Sencillo (`113453315134646`, farmacología «sin memorizar», USD; CO 130 act. / MX 138 act., 50 visibles, ads de farmacología más viejos del 2026-11-04 (7 ads, 18 d) y mezcla con guía GLP-1 clínica → cohorte indeterminada por oferta, tope 50); Vitus MX (`843892395468868`, «Farmacología VIP ilustrada», 0 sobrev. hoy); Salud en un Minuto MX (`1236525139551527`, 4 ads de 3 d); Farmacología Esencial / Simone Longo / FarmMaps (BR, ya vistos en BR).

## Veredicto provisorio
ENTRAR → 🇲🇽 🇨🇴 (mismo molde ya corre en Latam; Digi Aprende solo en 🇵🇪) y 🇺🇸 🇪🇸 🇮🇹 🇧🇷 🇵🇹 como destinos de mayor ticket para «farmacología ilustrada» (IT/PT comparten keyword: leer idioma). Par fuente 🇵🇪 → destino a decidir por Carlos. Nada de DESCARTAR.

## Embudo
- Etapa 1: 40 semillas ES nunca usadas (24 huellas + 16 molde × tema), 4 subagentes Haiku × 5 países (CO MX ES CL PE), `ACTIVE`, `limit 50`, ceros repetidos con `ALL`. Salieron ~210 páginas con señal sí/duda.
- Etapa 2: grep de `page_id` en `cazas/` y `RAW/cazas-auto/`: ninguna de las 10 elegidas aparecía → todas nuevas. 10 pasos rápidos + 1 paso completo (Digi Aprende: 4 países extra, `ALL` en PE, 2 `firecrawl_scrape`) + 4 búsquedas de molde (`mapas mentales farmacología` MX/CO, Estudia Sencillo CO/MX).

| Página | page_id | País del paso rápido | Resultado |
|---|---|---|---|
| Digi Aprende | `308598599011471` | PE | **19 / 39** → paso completo (arriba) |
| Estudio Contable Online | `1216662331539709` | CO | 0 / 12 (todo del 2026-11-20; «Método Contabilidad Práctica · 7 cuadernos + 8 bonos» US$) · solo apareció en CO/MX/CL en las tablas; re-conteo 11-29 |
| Ana Laura (acuario «10 guías visuales») | `114860084961404` | CO | 0 / 13 (más viejo 4 d, BRL); también 13 MX/CL/PE y 9 ES en las tablas; re-conteo 11-29 |
| Fer Rendon («Costeo de Menú» / finanzas constructoras, Excel) | `1977647735819349` | MX | 0 / ≥ 50 visibles, todo < 2 d, 159 activos → **cohorte indeterminada (tope 50)**; página con nombre de persona (posible marca personal) |
| Negocio en Regla («Carpeta de seguridad e higiene») | `1382378091630921` | MX | 0 / 21 (más viejo 4 d) |
| Cocina en Regla («+50 documentos para tu cocina») | `1516759901509982` | MX | 2 / 30 (< 4) |
| Pautas Listas para Urgencias | `1358096157393957` | ES | 0 / ≥ 50 visibles, todo < 3 d, 134 activos → indeterminada; los ads dicen «Búscalo en la app» → Filtro D (app) |
| Veterinario Lucas («180 mapas de emergencias equinas», US$ 12,90) | `1344618352077571` | CL | 0 / 4 (4 d) |
| Inglés en Mapas | `1470574242805325` | MX | 0 con ACTIVE: el `page_id` de la tabla no devolvió ads; sin contar (nodo `idiomas/mapas-visuales` ya cubre el molde) |
| Digital Guides (guías ilustradas REBT) | `1364466800085331` | CO | 0 con ACTIVE: id no devolvió ads; sin contar |

## Cobertura (40 semillas; totales estimados por la API en ACTIVE; ruido dominante: short-dramas, novelas, ecommerce, academias, esoterismo)
| Keyword | Países | Qué trajo |
|---|---|---|
| descarga inmediata | CO MX ES CL PE | Mybibliotech, Proyecto Ingresos (6, curso), Planeador Docente MX (6) |
| pdf descargable | idem | Digi Aprende PE (16+), Lex Artis PE (4), Imprime y Enseña MX |
| guía práctica | idem | Aprendia MX (portafolio), páginas «… 1st» ES |
| plantilla excel | idem | Fer Rendon MX ~15, TecnoMax, Excel Listo CO, Organizando Tu Vida PE |
| cuaderno de trabajo | idem | Estudio Contable Online ~18 (CO/MX/CL), clase en vivo (Dani Schepers) |
| fichas imprimibles | idem | Aprende Ya / Guías Paso a Paso MX (portafolio), Kits Útiles (kids) |
| mapas mentales | idem | Inglés en Mapas MX ~25, Mapas de la Carrera, Cuaderno de Psicología, Veterinário Lucas CL ~10, Libroteca (streaming) |
| resumen visual | idem | Sesión Lista CO, Manuales Listos CO |
| láminas ilustradas | idem | decoración física; Contador en Acción PE (libro) |
| checklist pdf | idem | Negocio en Regla ~13, Cocina en Regla ~15 (MX) |
| curso grabado · minicurso | idem | cursos en video (Filtro D); Juanimporta 23 (curso) |
| te llega al correo | idem | Mundo Pequeño MX 7, Pautas Listas ES 9 |
| kit digital | idem | Kit Online ~9, Lectoescritura ya ~15 (neurokids: ignorado) |
| pack de plantillas | idem | packs de Canva (Insta Pack, Pack Insta de Impacto ~7) |
| guía ilustrada | idem | Digital Guides CO ~7, Ana Laura MX |
| en imágenes · en una página · explicado fácil | idem | casi todo ruido (10-24 k resultados genéricos) |
| acceso de por vida | idem | Mundo AutoCad PE ~11 (software), Valor Virtual PE |
| $19.900 · S/ 29.90 · 9,90 € · $199 MXN | idem | ruido de precio; $199 MXN trajo Vida Práctica MX (4), Of Nutrition (planes de entreno); ES = cero activo |
| atlas anatomía | idem | AnatoAtlas, VetAnatomía Visual, Elaris (130 mapas de oftalmología, PE) — ≤ 10 |
| plantillas barbería · cuidados tatuaje · trámites divorcio · presupuesto familiar | idem | servicios/clínicas; Aprende Ya barberías MX 5 |
| checklist mudanza | CO MX ES CL PE | cero activo (CO/CL/PE ALL=0-1) |
| plantilla facturas · plantillas currículum · excel pymes | idem | SaaS; Grulla (plantillas nutricionistas, 1 ad) |
| adiestramiento cachorros · ajedrez aperturas · acordes guitarra | idem | servicios/academias; Entrecaninos (curso), Master Educativo MegaPacks (1) |
| test autoescuela | CO MX PE | **cero activo** (ALL = 0); CL 0 ACTIVE / 4 ALL (app); ES 99 activos, Amezti Academia 10, Test Coche 3 |
| calendario embarazo | idem | short-dramas, clínicas, apps |
| acuario principiantes | idem | **Ana Laura 13 (CO MX CL PE) / 9 ES** |
| guiones whatsapp ventas | idem | agencias, franquicias IA, mentorías |

Trampas nuevas: `acordes guitarra`, `guiones whatsapp ventas`, `calendario embarazo` (50 resultados de cola, solo ruido/servicios); `en una página`, `en imágenes`, `acceso de por vida`, `guía práctica` (10-24 k resultados genéricos); `test autoescuela` da cero activo en CO/MX/PE; las huellas de precio (`S/ 29.90`, `9,90 €`) devuelven 100-200 k ads de cualquier cosa (el buscador no exige el símbolo).
Nodos nuevos propuestos para la cola: ver `cazas/cola.md` (5).

## Lo que no se pudo verificar
- Precio y teléfono/mensaje prellenado de Digi Aprende (WhatsApp; Firecrawl no abre `api.whatsapp.com`).
- Los subagentes Haiku reportaron que la atribución país/keyword de algunos bloques sale del orden de las llamadas; las páginas verificadas se contaron por `page_ids` + país, no con esas tablas.
- Estudia Sencillo CO/MX: el tope de 50 oculta la cola vieja; hay que cortar por título de oferta («Domina Farmacología Sin Memorizar») en la PC.
- Fer Rendon, Pautas Listas (ES), Estudia Sencillo: cohorte indeterminada (tope 50 con casi todo nuevo).
