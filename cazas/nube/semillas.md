# Semillas — de dónde salen los nichos que todavía no miramos

Generador de nichos nuevos para las rutinas (pedido de Carlos, 2026-11-21). La cola se estaba quedando
sin nodos `virgen` porque el modo A repetía siempre las mismas 13-14 huellas. Este archivo es el
combustible: **las rutinas lo leen, no lo editan** (vive en `cazas/nube/`). Lo que van usando se anota
en `cazas/semillas-usadas.md`, para no repetir.

## 0. Cómo se usa (cada corrida, en la Etapa 1 de `NUBE.md` §7)

1. **Una keyword no se repite antes de 7 días, y las nunca usadas van primero** (orden de Carlos,
   2026-11-21: buscar productos y nichos que no tocamos, sin repetir keywords muy seguido). Antes de
   elegir cada semilla, fijate cuándo se usó por última vez, en cualquier sesión, también antes de este
   archivo: `grep -rin -- "<keyword>" cazas/cola.md cazas/semillas-usadas.md RAW/cazas-auto/`. La fecha
   sale de la fila (cola y semillas-usadas) o del nombre del archivo (`RAW/cazas-auto/YYYY-MM-DD-...`);
   vale la más reciente. **Para las huellas de §1, `python3 cazas/nube/indice-cazas.py semillas <Idioma>` hace
   este mismo cruce de una vez** y las devuelve ordenadas (las fechas futuras de la cola, que son agenda, no cuentan).
   - **No aparece** → nunca se usó: es la mejor semilla.
   - **Última vez hace 7+ días** → se puede volver a usar, pero solo cuando no quedan nunca usadas de
     ese tipo. Al repetirla, mirá sobre todo las páginas que no salieron la vez anterior.
   - **Última vez hace menos de 7 días** → saltala.
2. Elegí **20 semillas** (desde el 2026-11-22, con una sola corrida por día), en el idioma nativo de tu mercado:
   - **12 huellas de formato** (§1, la lista de tu idioma), en orden: primero las nunca usadas, después
     las de 7+ días, la más vieja primero.
   - **8 combinaciones** de §2 × §3 (molde × tema) o de §4 (momentos de vida), con la misma regla. Un tema
     que ya es nodo en `cazas/cola.md` no cuenta como semilla: saltalo.
   - En las sesiones de varios idiomas (EU: IT, FR, DE, PT, NL; ESTE: RO, PL, CZ, HU), repartí las 20 parejo
     entre los idiomas: unas 3 huellas y 2 combinaciones por idioma.
   - Si ya no quedan huellas nunca usadas de tu idioma, anotá «huellas nuevas agotadas en <idioma>» en
     `cazas/nube/log-nube.md` (una sola vez), para que Carlos pida sumar más.
3. Cada semilla se busca como **par de palabras nativas** (el buscador hace AND por palabra). Una
   combinación molde × tema se arma nativa, nunca traducida palabra por palabra del inglés.
   - Una combinación es **molde + tema y nada más**: `visa checklist`, `chess openings`, `tattoo aftercare`.
     Nunca `visa checklist pdf`. Las palabras de formato (`pdf`, `guide`, `download`, `template`) van solo
     si son parte del molde, como en `<tema> mind maps` o `<tema> in pictures`. (La prueba del 2026-11-21
     les agregó «pdf» y varias dieron 0 o 1 resultado.)
4. **Regla de alta.** Una página con **10+ anuncios activos** en una semilla, cuyo tema **no** está en
   `cazas/cola.md`, ni en `cazas/descartados.md`, ni en los nichos excluidos, entra a la cola como nodo
   `virgen` con la nota «apareció por semilla «<semilla>» el <fecha> (<sesión>)». La próxima corrida de tu sesión lo perfora
   dentro de sus 20 keywords propias (`NUBE.md` §5).
5. **Catálogo de operadores.** Cuando un operador de la tabla «Operadores a seguir» lanza un producto
   de un tema que no está en la cola, ese tema entra igual, como `virgen` con «apareció en el catálogo
   de <operador>».
6. Al cerrar, una línea por semilla en `cazas/semillas-usadas.md` (Edit al final, nunca Write).

> Nichos excluidos, siempre: neurokids, recetarios, actividades-para-adulto-mayor, religioso,
> manualidades. Si una semilla los trae, se ignoran sin anotarlos.

## 1. Huellas de formato, por idioma

Pares de palabras que delatan un infoproducto sin decir de qué tema es. El tema aparece en los resultados.

**Inglés (EN: US, GB, CA, AU)**
`instant download` · `printable pdf` · `digital download` · `workbook pdf` · `cheat sheet` ·
`study guide` · `printable flashcards` · `mind maps` · `checklist pdf` · `template bundle` ·
`spreadsheet template` · `notion template` · `canva templates` · `step-by-step guide` ·
`quick reference` · `illustrated guide` · `visual guide` · `explained visually` · `in pictures` ·
`on one page` · `lifetime access` · `instant access` · `emailed instantly` · `gumroad` · `payhip` ·
`stan store` · `systeme io` · `etsy digital` · `mini course` · `video course` · `starter kit` ·
`toolkit pdf` · `30-day plan` · `printable planner` · `printable journal` · `only $7` · `only $9` ·
`just $17` · `$27 today` · `£9 today` · `£17 only`

**Español (ES: CO, MX, ES, CL, PE)**
`descarga inmediata` · `acceso inmediato` · `pdf descargable` · `guía pdf` · `guía práctica` ·
`plantillas editables` · `plantilla excel` · `cuaderno de trabajo` · `fichas imprimibles` ·
`mapas mentales` · `resumen visual` · `láminas ilustradas` · `checklist pdf` · `paso a paso` ·
`curso grabado` · `minicurso` · `acceso de por vida` · `te llega al correo` · `por WhatsApp` ·
`hotmart` · `kit digital` · `pack de plantillas` · `guía ilustrada` · `en imágenes` ·
`explicado fácil` · `en una página` · `solo hoy` · `$199 MXN` · `$19.900` · `$9.990` · `S/ 29.90` · `S/ 39` · `9,90 €` · `17 €`

**Portugués de Brasil (BR) — y de Portugal (EU/PT, con precios en €)**
`acesso imediato` · `pdf completo` · `apostila pdf` · `guia prático` · `planilha pronta` ·
`mapas mentais` · `resumo visual` · `e-book completo` · `material digital` · `kit digital` ·
`passo a passo` · `curso gravado` · `minicurso` · `acesso vitalício` · `receba no e-mail` · `kiwify` ·
`hotmart` · `pay hotmart` · `fichas para imprimir` · `checklist completo` · `modelo pronto` ·
`templates canva` · `manual ilustrado` · `guia ilustrado` · `numa página` · `R$ 19,90` · `R$ 27` ·
`R$ 37` · `R$ 47` · `por apenas` · `9,90 €`

**Italiano (EU: IT, CH)**
`download immediato` · `pdf scaricabile` · `guida pratica` · `mappe concettuali` ·
`schemi riassuntivi` · `eserciziario pdf` · `modelli pronti` · `foglio excel` · `accesso immediato` ·
`accesso a vita` · `corso registrato` · `manuale illustrato` · `checklist pdf` · `kit digitale` ·
`quiz commentati` · `in una pagina` · `ricevi via email` · `solo 9,90` · `19 €`

**Francés (EU: FR, BE, CH)**
`téléchargement immédiat` · `pdf à télécharger` · `guide pratique` · `fiches de révision` ·
`cartes mentales` · `modèles prêts` · `tableau excel` · `accès immédiat` · `accès à vie` ·
`formation vidéo` · `guide illustré` · `checklist pdf` · `kit numérique` · `cahier d'exercices` ·
`en images` · `en une page` · `reçu par email` · `seulement 17 €`

**Alemán (EU: DE, AT, CH)**
`sofort download` · `pdf download` · `praxis leitfaden` · `lernkarten pdf` · `mindmaps pdf` ·
`vorlagen paket` · `excel vorlage` · `sofortiger zugriff` · `lebenslanger zugriff` · `videokurs` ·
`schritt für schritt` · `checkliste pdf` · `arbeitsbuch pdf` · `zusammenfassung pdf` ·
`ratgeber pdf` · `digitales paket` · `auf einer seite` · `nur 19 €`

**Neerlandés (EU: NL, BE)** — sumadas el 2026-11-21 y revisadas por revisor-traducciones
`direct downloaden` · `pdf downloaden` · `e-book pdf` · `ebook pdf` · `downloadbare pdf` · `digitale download` ·
`praktische gids` · `complete gids` · `visuele gids` · `stappenplan pdf` · `stap-voor-stapgids` ·
`printbare werkbladen` · `werkbladen pdf` · `mindmaps` · `kant-en-klare sjablonen` · `kant-en-klare templates` ·
`excel template` · `direct toegang` · `meteen toegang` · `onmiddellijk toegang` · `levenslange toegang` ·
`videocursus` · `in je eigen tempo` · `opgenomen lessen` · `minicursus` · `mini-cursus` · `checklist pdf` ·
`digitaal product` · `geen fysiek product` · `printbare planner` · `printables` · `canva templates` ·
`werkboek pdf` · `samenvatting pdf` · `oefenvragen pdf` · `direct in je mailbox` · `direct in je inbox` ·
`slechts €9` · `voor maar €19` · `slechts 9 euro` · `tijdelijke introductieprijs` · `e-book handleiding` ·
`op één pagina` · `op 1 pagina` · `in pdf-formaat` · `direct na betaling` · `direct na aankoop` ·
`eenmalige betaling` · `i.p.v.` · `nu voor`

> En Flandes se usa más `meteen` u `onmiddellijk` que `direct`. Sin comprobar cómo parte el buscador los
> guiones, el `€` y las tildes: si una huella da cero, probá la variante sin guion o sin tilde y anotalo en
> `cazas/nube/log-nube.md`.

**Rumano (ESTE: RO)** — revisadas por el agente revisor-traducciones el 2026-11-21
`descărcare imediată` · `ghid pdf` · `ghid practic` · `fișe de lucru` · `hărți mentale` ·
`modele editabile` · `tabel excel` · `acces imediat` · `acces pe viață` · `curs video` ·
`ghid ilustrat` · `checklist pdf` · `carte digitală` · `pachet digital` · `primești pe email` ·
`ghid complet` · `ghid pas cu pas` · `manual practic` · `curs înregistrat` · `minicurs` · `mini-curs` ·
`șabloane editabile` · `planner printabil` · `fișiere printabile` · `caiet de exerciții` ·
`fișe de recapitulare` · `rezumat pdf` · `notițe pdf` · `ebook complet` · `kit digital` ·
`descarcă ghidul` · `livrare instant pe email` · `doar 39 lei` · `doar 59 lei` · `doar 99 lei` ·
`preț de lansare` · `format pdf` · `imediat după plată` · `lei în loc de` · `printezi acasă` ·
`descarcare imediata` · `fise de lucru`

**Polaco (ESTE: PL)** — revisadas el 2026-11-21
`natychmiastowe pobranie` · `poradnik pdf` · `e-book pdf` · `praktyczny poradnik` · `karty pracy` ·
`mapy myśli` · `gotowe szablony` · `arkusz excel` · `arkusz w excelu` · `natychmiastowy dostęp` ·
`dostęp dożywotni` · `kurs wideo` · `ilustrowany poradnik` · `checklista pdf` · `produkt cyfrowy` ·
`otrzymasz mailem` · `poradnik krok po kroku` · `kompletny poradnik` · `nagrany kurs` · `minikurs` ·
`planer do druku` · `do wydruku` · `szablony canva` · `ćwiczenia pdf` · `fiszki do druku` ·
`notatki pdf` · `ściąga pdf` · `ebook poradnik` · `pobierz poradnik` · `dostęp od ręki` ·
`tylko 49 zł` · `materiały do pobrania` · `zestaw szablonów` · `gotowy plan` · `w formacie pdf` ·
`natychmiast po zakupie` · `zł zamiast` · `poradnik do pobrania`

**Checo (ESTE: CZ)** — revisadas el 2026-11-21
`okamžité stažení` · `průvodce pdf` · `e-kniha pdf` · `praktický průvodce` · `pracovní listy` ·
`myšlenkové mapy` · `hotové šablony` · `tabulka v excelu` · `excelová tabulka` · `okamžitý přístup` ·
`doživotní přístup` · `videokurz` · `ilustrovaný průvodce` · `checklist pdf` · `digitální balíček` ·
`pošleme e-mailem` · `průvodce krok za krokem` · `kompletní průvodce` · `kurz ze záznamu` · `minikurz` ·
`e-book ke stažení` · `plánovač k tisku` · `k vytištění` · `šablony canva` · `šablony v canvě` ·
`pracovní sešit` · `kartičky k tisku` · `výpisky pdf` · `tahák pdf` · `e-book průvodce` ·
`stáhněte si e-book` · `stáhni si e-book` · `hotový plán` · `jen 299 Kč` · `sada šablon` ·
`materiály ke stažení` · `ve formátu pdf` · `ihned po zaplacení` · `Kč místo` · `příručka pdf`

**Húngaro (ESTE: HU)** — revisadas el 2026-11-21
`azonnali letöltés` · `pdf útmutató` · `e-könyv pdf` · `gyakorlati útmutató` · `feladatlapok` ·
`gondolattérképek` · `kész sablonok` · `excel táblázat` · `azonnali hozzáférés` · `örökös hozzáférés` ·
`videótanfolyam` · `illusztrált útmutató` · `checklist pdf` · `e-mailben küldjük` ·
`lépésről lépésre útmutató` · `teljes útmutató` · `videós kurzus` · `minikurzus` · `nyomtatható pdf` ·
`nyomtatható planner` · `canva sablonok` · `munkafüzet pdf` · `tanulókártyák` · `jegyzetek pdf` ·
`tételek pdf` · `puska pdf` · `e-könyv útmutató` · `letölthető pdf` · `azonnal letölthető` ·
`csak 4990 Ft` · `csak 4.990 Ft` · `sabloncsomag` · `étrend pdf` · `edzésterv pdf` · `digitális termék` ·
`pdf formátumban` · `vásárlás után azonnal` · `Ft helyett` · `nyomtatható feladatlapok`

> **Diacríticos y flexión (RO, PL, CZ, HU).** No está comprobado si el buscador de la Biblioteca ignora los
> diacríticos o reconoce las formas flexionadas (`Excelu`, `jegyzetek`). Si una huella con diacríticos da
> cero, probá antes la variante sin diacríticos (`descarcare imediata`) y anotá en `cazas/nube/log-nube.md`
> qué pasó, una sola vez por idioma: así queda resuelto para las próximas corridas.


> Las huellas de precio y de plataforma (`hotmart`, `R$ 27`, `doar 39 lei`) son anchas: sirven para leer
> nombres de página, no para medir. Se cuentan después con `page_ids` + `countries`.

## 2. Moldes que ya ganaron (estructura del producto)

Lo que se repite en los ganadores del cerebro. Se cruza con un tema de §3 y se busca nativo.

| Molde | Ejemplo que ganó | Cómo se busca (EN / ES / PT) |
|---|---|---|
| El tema **en imágenes** | Wiring Regs in Pictures | `<tema> in pictures` / `<tema> en imágenes` / `<tema> em imagens` |
| El tema **hecho visual** | Journeyman Exam Made Visual | `<tema> made visual` / `<tema> visual` / `<tema> visual` |
| **150+ mapas mentales** | Cybersecurity Mind Maps | `<tema> mind maps` / `mapas mentales <tema>` / `mapas mentais <tema>` |
| **Fichas o tarjetas visuales** | +200 Visual Cards for UK Electricians | `<tema> visual cards` / `fichas <tema>` / `fichas <tema>` |
| **Todo en una página** | The French past on one page | `<tema> one page` / `<tema> en una página` / `<tema> numa página` |
| **Atlas** del tema | Building Defects Atlas | `<tema> atlas` / `atlas de <tema>` / `atlas de <tema>` |
| **Kit de papeles** de un momento de vida | Leave It Sorted · My Estate Kit · Dosarul Familiei | `<momento> kit` / `kit <momento>` / `kit <momento>` |
| **Banco de preguntas** de examen | Concorsi in Mappe | `<examen> practice questions` / `preguntas <examen>` / `questões <examen>` |
| **Plantillas listas** para un oficio | — | `<oficio> templates` / `plantillas <oficio>` / `modelos <oficio>` |
| **Guía paso a paso** de un trámite | — | `<trámite> step by step` / `<trámite> paso a paso` / `<trámite> passo a passo` |

## 3. Temas para cruzar con los moldes

En español; cada sesión los pasa a su idioma nativo. **Saltá los que ya son nodo en `cazas/cola.md`**
(hoy la cola está cargada de profesiones, exámenes e idiomas: priorizá los demás grupos).

- **Oficios y técnicos:** electricista, fontanero, soldador, carpintero, HVAC y climatización, mecánico,
  chapa y pintura, albañil, techador, jardinero y paisajista, cerrajero, técnico de paneles solares,
  instalador de cámaras, técnico de celulares, tatuador, barbero, manicura, maquilladora, esteticista.
- **Salud y cuidado (no clínico):** auxiliar de enfermería, técnico en farmacia, cuidador de personas
  dependientes (solo papeles y rutinas, nunca actividades para adultos mayores), primeros auxilios,
  anatomía para estudiantes, masaje, drenaje linfático, fisioterapia para estudiantes, nutrición deportiva.
- **Exámenes y certificaciones fuera de lo ya cazado:** carnet de conducir, camionero y CDL, piloto
  privado, drones, guardia de seguridad, socorrista, agente inmobiliario, seguros, contador y
  certificaciones contables, ciberseguridad, AWS y nube, Excel avanzado, ciudadanía y test de idioma
  para visa.
- **Dinero y trabajo:** presupuesto familiar, salir de deudas, impuestos de autónomo, facturación de
  freelance, CV y entrevistas, LinkedIn, ventas por WhatsApp, atención al cliente, Excel para pymes,
  emprender desde casa, alquiler por temporada, reventa.
- **Hogar y vida práctica:** orden y limpieza, reformas, mantenimiento del auto, huerta, plantas de
  interior, ahorro de energía, mudanza, organización de papeles.
- **Mascotas:** adiestramiento de perros, cachorros, gatos, peces y acuarios, aves, caballos,
  peluquería canina, alimentación natural de mascotas.
- **Hobbies y habilidades (no manualidades):** fotografía con el celular, edición de video, dibujo
  digital, música y guitarra, ajedrez, pesca, caza deportiva, camping, ciclismo, running, gimnasio en
  casa, yoga, defensa personal, oratoria, escritura, memoria, lectura rápida.
- **Estudio:** técnicas de estudio, química, física, matemática de secundaria, historia, biología,
  programación para principiantes, inteligencia artificial para el trabajo.
- **Familia (fuera de neurokids):** embarazo semana a semana, primer año del bebé, lactancia,
  organización de la boda, divorcio y custodia, finanzas en pareja.

## 4. Momentos de vida (el eje que más rindió y menos se miró)

Un momento de vida trae papeles, decisiones y miedo: el molde «kit de papeles» o «guía paso a paso».
Ejemplo que ganó: Leave It Sorted (herencia) → My Estate Kit 37/37 en 🇬🇧 y Dosarul Familiei en 🇷🇴.

herencia y testamento · muerte de un familiar y trámites · divorcio · casamiento · mudanza ·
emigrar y visa · volver al país · comprar una casa · alquilar por primera vez · primer empleo ·
despido · jubilación · abrir un negocio · cerrar un negocio · primer bebé · adoptar · cuidar a un
padre dependiente (papeles y dinero) · sacar el carnet de conducir · ir a la universidad ·
diagnóstico de una enfermedad crónica (organización, no tratamiento) · accidente de tránsito ·
demanda o juicio chico · deudas y embargos · robo de identidad · emergencias del hogar.
