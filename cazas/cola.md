# Cola de caza — el árbol de nichos

Fuente de trabajo del programa de caza automatizado ([[automatizar-la-caza-de-winners]]). Cada sesión
(EN · BR · ES · EU · ESTE) elige de acá **qué** cazar y en **qué modo**, y al terminar actualiza su nodo.

> ⛔ **Regla madre: el cero no descarta.** Un nodo pasa a `descartado-eje` solo después de (a) 4-5
> keywords nativas, (b) un nivel de subnichos perforado (modo B) y (c) `ad_active_status: ALL` mirado.
> Antes de eso vuelve como `superficial`. Los 🔴 los pone **Carlos**, nunca una sesión automática.

## Estados

| Estado | Significa | Qué hace la sesión con él |
|---|---|---|
| `virgen` | nunca se barrió | **prioridad 1** — modo A o B |
| `superficial` | se barrió con pocas keywords o un solo mercado | **prioridad 2** — modo B (perforar) |
| `profundo` | 4+ keywords nativas por mercado, subnichos mirados | solo modo C (operadores/agenda) |
| `ENTRAR` | hay molde y destino; el producto está en el catálogo o en camino | modo C: vigilar la ventana |
| `propio` | producto nuestro vivo en el nicho | modo C: vigilar competidores |
| `descartado-eje` | ese eje, en esos mercados, no da infoproducto modelable | no se toca; los hermanos sí |
| `🔴` | descarte permanente del dueño | no se toca |
| `🟡 <fecha>` | revisable en fecha | modo C cuando llega la fecha |

**Orden de elección:** `virgen` más viejo → `superficial` más viejo → `🟡` vencido. Dentro del mismo
estado, primero el nodo cuyo mercado coincide con la sesión. Una sesión no repite un nodo que otra
sesión tocó en los últimos 7 días.

---

## El árbol

Cargá acá tus nichos. Un nodo por nicho o subnicho (`nicho/subnicho`). Las keywords literales viven en
la página del nicho de tu wiki; acá va el conteo y la fecha. La columna Mercados dice a qué sesión
le toca (EN · BR · ES · EU · ESTE). Si el árbol está vacío, las sesiones arrancan en modo A (huella) y lo van llenando con
los nichos que emergen.

| Nodo | Padre | Mercados | Estado | Cobertura | Próxima acción |
|---|---|---|---|---|---|
| neurokids | — | todas | 🔴 | — | **EXCLUIDO por el dueño en la instalación: no se busca, no se perfora, no se agrega como hijo** |
| recetarios | — | todas | 🔴 | — | **EXCLUIDO por el dueño en la instalación: no se busca, no se perfora, no se agrega como hijo** |
| actividades-para-adulto-mayor | — | todas | 🔴 | — | **EXCLUIDO por el dueño en la instalación: no se busca, no se perfora, no se agrega como hijo** |
| religioso | — | todas | 🔴 | — | **EXCLUIDO por el dueño en la instalación: no se busca, no se perfora, no se agrega como hijo** |
| manualidades | — | todas | 🔴 | — | **EXCLUIDO por el dueño en la instalación: no se busca, no se perfora, no se agrega como hijo** |
| profesiones | — | todas | profundo | cerebro: 13 fichas, 7 mercados (importado 2026-11-20) | modo C: operadores de material listo, exámenes y oficios (§Operadores) |
| profesiones/material-de-clase-listo | profesiones | todas | profundo | validado 🇧🇷 🇺🇸 🇮🇹 en el cerebro | C; B solo en mercados sin barrer (🇨🇦 🇦🇺 Este) |
| profesiones/examenes-y-oposiciones | profesiones | todas | superficial | cerebro: concursos 🇮🇹, oposiciones 🇨🇿🇭🇺; EN 2026-11-20 abrió certificaciones | B: por examen oficial masivo de cada país |
| profesiones/manuales-de-oficio | profesiones | todas | profundo | electricista/fontanero/mecánica en 6+ idiomas | C: Furgo Libre, Nova Mind, Packs & Moldes, Energy Profitable |
| cuadernos-ilustrados | — | todas | 🟡 evaluable | formato «in pictures / made visual / în imagini»; decenas de operadores | C; diferencial por ángulo, avatar o mercado, no por producto |
| herencia-y-papeles | — | EN EU ESTE | profundo | ordenador de papeles rellenable; 🇺🇸🇬🇧🇩🇪🇫🇷🇵🇱 vistos; Este 2026-11-20: Mente que sana «Dosarul Familiei» RO ≥ 11/59 (tarjeta), CZ/HU del mismo operador apagados | B en 🇨🇦 🇦🇺 🇪🇸 🇮🇹; Este: re-conteo RO 2026-11-27 |
| idiomas | — | todas | superficial | 🟢 en el cerebro: PDF de idiomas, 4 pares de lenguas libres | B: un par de lenguas por mercado |
| dolor-y-movilidad | — | EN EU | profundo | protocolos casi todos en video/app (Filtro D); rama buena: movilidad deportiva | B solo movilidad deportiva en PDF |
| nutricion-antiinflamatoria | — | — | 🔴 | es mayormente **recetario** → cae en el nicho excluido «recetarios» | **no se caza** (solo planes no-recetario, si aparecen por huella) |
| jardineria | — | ES | propio | Huerta en Casa (producto propio, Testeando) | C: vigilar competidores de huerta urbana |
| idiomas/mapas-visuales | idiomas | EN | 🟡 2026-11-27 | EN 2026-11-20: 6 páginas (Spanish Made Visual 8/23 US, German Grammar Made Visual 6/30, Fluency Mapped 0/50≥, Italian Made Visual, Japanese Mapped, Fluent Maps); molde PDF «un mapa por página» US$ 14-19 | C: re-contar los 3 mayores el 11-27; B pendiente: hijos por par de lenguas en 🇨🇦 🇦🇺 🇬🇧 por separado y lenguas minoritarias (portugués, árabe, coreano, ruso) |
| profesiones/manuales-de-oficio/fichas-visuales-aprendia | profesiones/manuales-de-oficio | ES | `superficial` | apareció por huella el 2026-11-20: red AprendIA (8+ fanpages, 826 guías PDF «N fichas», ~US$ 19,90, WhatsApp, 🇲🇽; Guías Oficiales 49/55, Guías Expertas 29/56, Aprende Fácil ≥26/90); portafolio de SKUs | modo B/C: perforar por SKU (`search_terms` por título + `page_ids` + país) en busca de un tema con 30+ en 🇲🇽 🇨🇴; contar las 5 fanpages restantes; re-conteo 2026-11-27 |
| exámenes-certificaciones/guias-ilustradas | — | EN (US, GB) | `superficial` | huella 2026-11-20: 4 keywords, 2 páginas contadas (Visual Guide Lab, Fenix Library); B 2026-11-20 tarde: +Visual Journeyman Style 9/10 cerca (re-conteo 11-27), AOA lesson plans ≈6, Stark Exam Prep 0/28, Clearpage Books (119 activos, todo de hoy) | modo B: perforar por examen (aviación, radio, oficios, marítimo, TI, UK) con `search_terms` + `page_ids` + país; luego destinos BR/ES/IT/DE |

---

## Trampas de keyword (no se repiten)

Cada sesión la lee antes de generar keywords y **agrega** las que descubre.

| Keyword / patrón | Por qué falla | Qué usar |
|---|---|---|
| `book` `novel` `read` (EN) | short-dramas (cientos de miles de resultados) | entregable + tema |
| `Google Sheets` / `sheets` | short-dramas | pares: `spreadsheet template`, `planilha controle` |
| keywords idénticas en ES/IT/PT (`farmacologia`, `peptide`, `dietoterapia`) | el mercado parece 3-8× más grande | la palabra que **no** se comparte; leer el idioma de cada creativo |
| siglas cortas (`EKG`) | spam de webnovelas | frase de 3+ palabras |
| préstamos del inglés (`barista`, `latte art`, `Meal Prep`) | traen anunciantes de otros países | la palabra nativa |
| keywords amplias en nichos de churn | solo devuelven las últimas 48 h | **angosto para ver la cola** |
| frases largas en `search_terms` | el matcher es **AND por token** | pares de palabras |
| huellas anchas en 🇧🇷 (`acesso imediato`, `apostila`, `kiwify`, precios) | decenas de miles de ads, los 50 primeros son de hoy: sirven para leer nombres de página, no para medir | barrer → anotar ~30 páginas → contar cada una con `page_ids` + `countries`; rinden `guia prático pdf`, `planilha pronta`, `ebook completo`, `material digital` |
| bloque `es` sin BO / EC / GT | subcuenta a los operadores andinos | `countries: ["MX","CO","AR","PE","CL","BO","EC","GT","ES"]` |
| `ad_creation_time` viejo sin impresiones | ads zombis | abrir el snapshot: «isn't in the Ad Library / no impressions» no cuenta |
| follow ads («Visit Instagram profile») | infl an la longevidad | la longevidad se lee **sobre el ad que vende** |
| `prova CNH simulado pdf` (BR) | solo 4 resultados en total: nicho casi vacío con esa frase | probar `autoescola`, `simulado Detran` por separado antes de hablar de CNH |
| `resumos enfermagem pdf` / `mapas mentais concurso` (BR) | el 80 % son ads de < 4 días de fábricas multi-SKU (apostilas por municipio, Tutoria EAD) | contar por título de oferta + `page_ids` + BR |
| `limit: 50` que devuelve 50 ads de hoy | cohorte truncada | reportar como piso, repetir con `page_ids` + `countries` |
| snapshot sin espera | `get_page_text` devuelve solo el encabezado | `wait` 4 s antes de leer |
| landing de operador 🇧🇷 | geo-redirige por idioma | el precio del mercado cazado se mira desde el checkout |
| página que devuelve **0 con `ALL`** | no está pausada: ya no existe | anotarla como desaparecida |
| un whale migra de página sin apagar el negocio | contar solo la página madre lo da por muerto | contar también las páginas hermanas de su ficha |
| `page_ids` con >50 activos | devuelve siempre los 50 más nuevos y la cohorte 7+ queda invisible | sumar `search_terms` por SKU + `page_ids` + `countries` para leer la cola vieja |
| `printable planner` (EN) | fábricas multi-SKU que recrean todo cada 2-3 días (cohorte 0) | contar por SKU y exigir 10+ en cohorte |
| `spanish workbook` · `korean alphabet` · `french grammar pdf` (EN) | redes de páginas-persona (audio/video, «She stopped studying») y libros de Amazon en € | `<idioma> maps`, `<idioma> mind maps`, `<idioma> grammar pdf`; leer cada creativo (Spanish Made Visual ya vende francés) |
| `paso a paso PDF` · `acceso inmediato PDF` sin país único (ES) | 87.166 / 2.477 resultados, los 50 primeros son de hoy (salud, juegos, short-dramas) | usar pares de entregable + tema (`fichas listas docentes imprimir`, `diagnósticos manual técnico`) y contar después por `page_ids` + país |
| red multi-fanpage «Aprendia» (🇲🇽) | cada ad vende un SKU distinto: la cohorte de la página es de portafolio, no de oferta | contar por título de SKU con `search_terms` + `page_ids` + país antes de hablar de vara |
| consulta combinada de varios `page_ids` (ESTE) | el tope de 50 devuelve lo más nuevo y deja fuera a los operadores más viejos (Rowan House no apareció) | una consulta por `page_id` + país |
| `ALL` + `page_ids` en CZ/PL/HU (ESTE) | trae cientos de ads pero `ACTIVE` da 0 aun con ads de hoy: no dice el estado | contar con `ACTIVE` por país suelto antes de decir «apagado» |
| `search_terms` con diacríticos (`šanon`) (CZ) | devolvió 0 con ads que lo traen | probar sin tilde o con el título entero |
| `ALL` sin `ACTIVE` (ESTE) | `ALL` no trae el estado del ad: un 126 en `ALL` puede ser todo apagado | contar vivos siempre con `ACTIVE`; `ALL` solo para ver qué se probó |
| `ads_library_search` con `page_ids` de fábrica multi-SKU (Clearpage Books, 119 activos) | los 50 visibles son todos de hoy; cohorte invisible | cortar por SKU con `search_terms` (título de examen) + `page_ids` + país |
| link de destino del ad | la API no lo trae; la web de la Biblioteca da 403 a WebFetch | `firecrawl_scrape` sobre el `ad_snapshot_url`/URL de la Biblioteca muestra copy y link |
| `riassunti concorso pdf` / `mappe concettuali concorso` (IT) | el primero es angosto y limpio (6); el segundo arrastra portafolios (Martina Rossi, «La Mappa <concurso> <año>» = una fanpage por concurso) | contar por oferta + `page_ids` + IT; no sumar fanpages hermanas |
| `Prüfungsvorbereitung PDF Lernkarten` (DE) · `exame ordem concurso pdf` / `mapas mentais concurso` (PT) | cero con `ACTIVE` (paso 1) | DE: `Lernzettel Prüfung`; PT: probar `ALL` y `concurso público resumo` antes de hablar de mercado |
| red AprendIA: `page_id` de «Guías profesionales» (ES) | en la cola figura `1319574141233447` pero la API devolvió `1322875314251329` con ese nombre | confirmar el id antes de contar |
| `ebook completo pdf` · `guia prático pdf` (BR) | ruido: velas/bordado (manualidades excluido), Autor.ia (software), marcas personales, Black Friday | `mapas mentais` + tema de concurso, `planilha pronta` + oficio; contar por `page_id` |

## Operadores a seguir (modo C)

Fábricas multi-SKU y whales que muestran el próximo producto antes de que aparezca por keyword. Se
enumeran con `page_ids` + `countries`, siempre con el país. Cadencia: quincenal salvo que diga otra cosa.

| Operador | page_id | País | Por qué se lo sigue |
|---|---|---|---|
| Studio Facile (rota fanpages) | `1232011766670582 · 1272162682644374` | IT RO FR | red de cuadernos ilustrados; 546 activos, lanza por idioma |
| Fenix Books | `1311482932059218` | IT | misma plantilla de certificaciones que Diagram Books |
| Diagram Books | `1499263639932513` | FR GB | certificaciones ilustradas; vigilar si sobrevive |
| Rowan House Press (In pictures books) | `103448682074390` | GB PL | certificaciones en imágenes, 569 activos, ya en hindi |
| Pagine Chiare | `1362170890322476` | IT GB | trámites; 105 anuncios en 1,5 d |
| Nova Mind | `1372898352562817` | IT BR RO | manual del electricista en 6 idiomas |
| Packs & Moldes Pro | `1227856100409706` | BR | manuales de oficio (ficha en el cerebro) |
| Furgo Libre | `1405313469331346` | ES FR IT | cuadernos de oficio; abre ofertas nuevas de un día para otro |
| Energy Profitable | `720903437767543` | US GB | manual de oficio en inglés (ficha en el cerebro) |
| Griffbereit | `1395192210344917` | DE | bundle de oficios en Impultienda (ficha) |
| Gracie Williams | `1316868038177272` | DE US | fichas de enfermería → medical coding (ficha) |
| Giulia Ferraresi | `1299765756564104` | IT | Kit Contabile Pratico, 7 tandas |
| Atelier Horizon | `988601281012434` | FR IT | física en 60 segundos, 745 activos |
| Illustrated SYP | `1480945315094128` | DE GB RO | exámenes de acceso por país |
| Margin and Ink | `1429242170270934` | FR | dental |
| Nara Costa | `1403124126208097` | US | 150+ mapas de drenaje linfático; multi-SKU médico |
| James Carter | `112021632005643` | US | 150+ mind maps; saltó de automotriz a ciberseguridad |
| Markus Schneider | `1401781706350470` | GB | +200 visual cards para electricistas UK |
| Visualia Books | `1509026768951102` | RO HU IT GB | certificaciones técnicas, 450 activos, 0 sobrev. al medir |
| Learning Fast | `1469659026222538` | CZ IT HU | oposiciones, 524 activos, 0 sobrev. al medir |
| Smart Living Hub | `1471138532745172` | PT IT | instalador smart home |
| Mentális Zavarok Térképe · Harta Tulburărilor · Mapa duševních poruch | `1385372351328215 · 1385099554683635 · 1338549579349249` | HU RO CZ | mismo molde (mapa de trastornos) en el Este |
| 365 Aktywności Bez Ekranu | `1346208118579574` | PL | actividades sin pantalla (Impultienda) |
| Lorenz Varen | `1351005084760173` | FR IT | ciclistas (ficha); probó corredores y preparación física y los apagó |
| Rachel Bennett | `280579905138659` | IT | actividades escuela infantil (ficha), 4 tandas |
| Lingua Chiara (+ fanpages «Illustriert») | `1034177656443347` | IT DE FR | Lo Spagnolo in Mappe (ficha) |
| Fernanda Oller | `1262265860313000` | GB PT US | Building Defects Atlas (ficha) |
| Arquiteta Clara Finelon | `1282745681595572` | BR | segundo jugador del atlas |
| Verde Guides | `1413675531823485` | RO FR CZ GB | Planul Hashimoto 21 (oferta no validada) |
| George Windsor | `1059809390547396` | 15 países | lanzó 148 anuncios en 14 idiomas el 18-nov: experimento multi-idioma |
| Biblioteca Profesional | `948030185069933` | ES | multi-vertical (pádel, boxeo, fisio, electricidad) |
| AprendIA (red de fanpages) | `1453826204471738 · 1347816741752269 · 1372902832576549` (+ `1288181344388955 · 1365055716696947 · 1381808071689792 · 1390929764102651 · 1319574141233447`) | MX | tienda `aprendia.shop`: 826 guías PDF ~US$ 19,90, venta por WhatsApp `wa.me/12137860982`; Guías Oficiales 49/55 (33 d); seguir si una oferta suelta cruza 30 |

## Rotación vigente

| Día | EN | BR | ES | EU | ESTE |
|---|---|---|---|---|---|
| Lun | A huella | B perforar | C operadores | A huella | B perforar |
| Mar | B perforar | C operadores | A huella | B perforar | C operadores |
| Mié | C operadores | A huella | B perforar | C operadores | A huella |
| Jue | A huella | B perforar | C operadores | A huella | B perforar |
| Vie | B perforar | C operadores | A huella | B perforar | C operadores |
| Sáb | C agenda | A huella | B perforar | C agenda | A huella |
| Dom | lint de la cola | lint de la cola | lint de la cola | lint de la cola | lint de la cola |

## Bitácora de la cola

Una línea por sesión, la más nueva arriba. La sesión la escribe **antes** de cazar (con «en curso») y
la completa al terminar.

| Fecha | Sesión | Modo | Nodo | Keywords corridas | Resultado | Nodo queda en |
|---|---|---|---|---|---|---|
| 2026-11-21 | BR (mañana) | A huella | — | 5 huellas (guia prático pdf, planilha pronta, material digital, mapas mentais, ebook completo pdf) + 7 conteos por page_id | 0 tarjetas · 4 señales (Mentagrama 8/16 una tanda, ≤5 por oferta = vigilancia; Mapa do Aprovado «R$10» 5/36 = vigilancia; Vistoria Pro 3 sobrev. en 3 ofertas; Descomplica em Mapas 0/4) | sin nodo nuevo: Mentagrama y Mapa do Aprovado entran como operadores en `profesiones/examenes-y-oposiciones` (BR); re-conteo 2026-11-28 |
| 2026-11-21 | EN (mañana) | C agenda/operadores | operadores EN (Energy Profitable, Nara Costa, James Carter, Markus Schneider, Rowan House, Diagram Books, Fernanda Oller) + re-conteos Visual Journeyman Style / Spanish Made Visual | en curso | en curso | en curso |
| 2026-11-20 | ESTE (tarde) | B perforar | herencia-y-papeles (tramo Este: RO PL CZ HU) | 13 keywords nativas (PL ×4, RO ×4, CZ ×3, HU ×4) + 12 conteos por page_id | 1 tarjeta (Mente que sana «Dosarul Familiei» RO ≥ 11 / 59, embudo no verificado; el mismo operador la probó y apagó en CZ y HU) + 2 señales (Klidné předání CZ / Querida Familia HU apagados; Dobrze Wiedzieć PL 0 sobrev.) | `herencia-y-papeles` tramo Este pasa a `superficial`: faltan PL (sin operador PDF vivo) y re-conteo de Mente que sana 2026-11-27 |
| 2026-11-20 | EU (tarde) | B perforar | profesiones/examenes-y-oposiciones (tramo EU: IT concorsi, DE Prüfung, FR concours, PT exame) | 9 keywords nativas (IT ×2, DE ×3, FR ×2, PT ×2) + 8 conteos por page_id | 1 tarjeta (Concorsi in Mappe IT, 25 / 40, €17, Hotmart; score 1/4; cruzar con «Concorso Docenti in Mappe» 🔴) + 5 señales (red «La Mappa <concurso>» IT, Pflege Ausbildung DE = marca personal, Pilote Autrement DE ≤ 4, Martina Rossi, Belle Plume FR) | `examenes-y-oposiciones` sigue superficial (tramo EU: FR y DE con 2-3 keywords, PT en cero sin `ALL`; faltan Beamtenprüfung, concours cat. C, concurso público PT) |
| 2026-11-20 | EN (tarde) | B perforar | exámenes-certificaciones/guias-ilustradas (todos los nodos superficiales EN tocados hoy; se perfora el propio por examen) | 4 keywords (pilot exam study guide, NCLEX study guide pdf, electrician exam visual, real estate exam cheat sheet) + 10 conteos por page_id | 0 tarjetas · 3 señales (Visual Journeyman Style 9/10 US = cerca, re-conteo 2026-11-27; AirlinesOnAutopilot lesson plans ≈6 = vigilancia; Stark Exam Prep 0/28) | `guias-ilustradas` sigue superficial (4 de 12 exámenes mirados: faltan radioaficionado, plomería, marítimo, UK PPL, CompTIA, CDL, EMT) |
| 2026-11-20 | ES (tarde) | B perforar | profesiones/manuales-de-oficio/fichas-visuales-aprendia (perforar por SKU, MX CO ES) | 2 búsquedas (`fichas ISO 9001` MX, `fichas guía visual` CO) + 7 conteos por page_id (4 fanpages hermanas MX, Psyacademy CO y MX+ES) | 0 tarjetas · 3 señales (4 hermanas = portafolio, ningún SKU > 3 ads; Aprende Hoy 36/62 por página; Psyacademy «210 fichas» 0/7 CO) | nodo pasa a `superficial`: faltan conteos por SKU de Aprende Ya y Aprende Más (cola invisible) |
| 2026-11-20 | BR (tarde) | B perforar | profesiones/examenes-y-oposiciones (slice BR: OAB, concursos, CNH, enfermagem) | 4 keywords (resumo OAB pdf, mapas mentais concurso, prova CNH simulado pdf, resumos enfermagem pdf) + 7 conteos por page_id | 0 tarjetas · 3 señales (Maria «1.000 Questões Comentadas» enfermagem 8/27 = cerca, re-conteo 2026-11-27; O Concurseiro Aprova «Edital Ilustrado OAB» 0/50≥ cohorte invisible; Carlos Santos cards enfermagem 5/22 multi-SKU) | `profesiones/examenes-y-oposiciones` sigue superficial (BR: faltan ENEM, bancas, CNH) |
| 2026-11-20 | ESTE (mañana) | C operadores | operadores ESTE: Mentális Zavarok Térképe · Harta Tulburărilor · Mapa duševních poruch · Visualia Books · Learning Fast · 365 Aktywności Bez Ekranu · Illustrated SYP · Verde Guides · Studio Facile · Nova Mind | 14 consultas por page_id + país (ACTIVE y ALL en los que dieron cero) | 0 tarjetas · 4 señales (Mentális HU 0/8 y Harta RO 0/10 aún sin cohorte; Visualia, Learning Fast, Illustrated SYP, Verde Guides y Mapa CZ con 0 activos hoy; Studio Facile RO 27/41 pero portafolio, ninguna oferta > 8) | operadores ESTE siguen en vigilancia; re-conteo Mentális/Harta 2026-11-27 |
| 2026-11-20 | ES (mañana) | A huella | — (cola sin nodos ES: B sin nodo) | 8 huellas (acceso inmediato PDF, moldes imprimir PDF, plantillas editables PDF, diagnósticos manual técnico, guía PDF WhatsApp, paso a paso PDF, oposiciones temario esquemas, plantillas Excel, fichas listas docentes) + 9 conteos por page_id (MX CO ES) | 0 tarjetas · 3 señales (red AprendIA: catálogo de 826 guías PDF US$ 19,90 por WhatsApp; Guías Oficiales 49/55 🇲🇽 vara 30, pero portafolio de SKUs → sin tarjeta) | nodo nuevo `profesiones/manuales-de-oficio/fichas-visuales-aprendia` virgen; huellas ES rindieron: `fichas listas docentes imprimir`, `guía PDF WhatsApp` |
| 2026-11-20 | BR (mañana) | C operadores | operadores BR: Packs & Moldes Pro · Arquiteta Clara Finelon · Nova Mind | 7 consultas: 3 conteos ACTIVE/ALL por page_id + `manual eletricista pdf` + 3 páginas nuevas | 0 tarjetas · 3 señales (Packs & Moldes Pro 29/29 · vara 30, re-conteo 2026-11-27; Clara Finelon y Nova Mind 0 con ALL en BR) | `profesiones/manuales-de-oficio` BR sigue profundo; Packs & Moldes en vigilancia 🟡 2026-11-27 |
| 2026-11-20 | EN (mañana, 2ª corrida del día) | B perforar | idiomas | 13 keywords (EN: spanish workbook, french grammar pdf, learn spanish pdf, french/italian/japanese/german/portuguese maps y variantes) + 9 conteos por page_id (US; GB CA AU unión) | 0 tarjetas · 3 señales (familia «mapas visuales»: Spanish Made Visual 8/23; re-conteo 2026-11-27) | `idiomas` EN pasa a profundo-parcial: hijo `idiomas/mapas-visuales` EN en vigilancia (🟡 2026-11-27) |
| 2026-11-20 | EN (mañana) | A huella (cola vacía: B sin nodo) | — | printable planner, payhip, spreadsheet template, study guide pdf (US+GB) + 11 conteos por page_id | 1 tarjeta (Visual Guide Lab, guías de examen PDF US$27) + 3 señales | nodo nuevo `exámenes-certificaciones/guias-ilustradas` superficial |
| | | | | | | |
