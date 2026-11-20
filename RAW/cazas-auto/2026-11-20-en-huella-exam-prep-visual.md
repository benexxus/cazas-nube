# Caza automática — EN · huella (cola vacía; B sin nodo) · 2026-11-20

Corrida de viernes por la mañana (modo B por tabla, pero la cola no tiene nodos `virgen`/`superficial`: se aplicó la regla «cola vacía → modo A»). Hora de arranque 02:37 Europe/Madrid. Corte de cohorte 7+ = ads creados antes de 2026-11-13 01:40 UTC (epoch 1794534000).

## Shortlist

### Visual Guide Lab — page_id 1467890346400480 — 🇺🇸 US (candidato a tarjeta)
- Ads Library US: https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&view_all_page_id=1467890346400480&search_type=page&media_type=all
- Ads Library GB: https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=GB&view_all_page_id=1467890346400480&search_type=page&media_type=all
- Total activos US: 168 (estimated_total_count). Cohorte 7+ medida con `search_terms: pilot` + `page_ids` + `countries: ["US"]`: **11 / 30** (piso, solo el slice «pilot»: Sport Pilot, Private Pilot, Part 107, Amateur Extra). Edades 7,1 d (1) y 9,0 d (10). Sin escalonamiento largo: dos tandas (≈7 d y ≈9 d).
- Resto de la página US: los 50 más nuevos de la página completa son todos < 4 días (tanda de churn de ~5 días); la cohorte total de la página no se puede medir por API (tope 50, orden por recencia).
- GB: 94 activos; los 50 más nuevos (el más viejo 5,5 d) → cohorte 7+ = 0 visible. GB no está probado.
- Tipo de página: fantasma (sin cara ni nombre de persona; marca «Visual Guide Lab»). Gate A OK.
- Embudo verificado por Firecrawl (la web de la Biblioteca devolvió el creativo; WebFetch no usado): ad → `drone-pilot-made-visual.visualguidelab.com` → landing de venta directa con checkout. Vende «Drone Pilot Part 107, Explained Visually»: PDF de 79 páginas ilustradas + 2 bonos (Test Day Checklist, Illustrated Aviation Glossary), **US$ 27** pago único (tachado US$ 95,80), garantía 30 días, «PDF by email: nothing is printed or shipped», oferta «valid today only» (urgencia con reloj). Un subdominio por SKU (`commercial-pilot-visual.visualguidelab.com`, etc.). Gate B OK. Filtro C: front-end único, sin upsell visible en la landing (checkout no recorrido).
- Hook: «El mapa seccional tiene líneas y tintes con significado; la guía solo las lista» / «Every rule drawn», «one topic per page», quiz de 3 preguntas como creativo.
- Duplicación: 3-4 copias por creativo («Part 107 Made Visual», «Sport Pilot Made Visual», «Private Pilot Made Visual») dentro de la cohorte.
- Catálogo (fábrica multi-SKU de guías ilustradas de examen oficial): FAA Part 107, Private Pilot, Sport Pilot, Instrument Rating, A&P Mechanic, Amateur Radio (General/Extra), CWI, Fire Alarm, Boiler, Plumbing, Contractor, marítimos (captain's license, six-pack, radar, DSC), UK PPL/Day Skipper/CPC/refrigeración/letting agent (GB), etc. Misma plantilla de landing.
- Score: ① longevidad 45+ = 0 · ② volumen 50+ en cohorte = 0 · ③ duplicación 10+ = 0 · ④ hueco de arbitraje = por verificar (no se barrió destino) → **≤1/4: observar**; pasa la vara de bandeja (≥10 en cohorte de un page_id) por poco y con las salvedades de arriba.
- `ad_snapshot_url` (cohorte, Part 107): https://www.facebook.com/ads/library/?id=1147141701128084 · ?id=2205547726841261 · ?id=1681892263383784 · ?id=1680652723771572 ; Private Pilot: ?id=1794061928546397 → ids 1794061928546397, 1382125994991351, 2037496756934312; Sport Pilot: 1175927261667571, 2144042779522220, 2240249939854445.

### Fenix Library — page_id 1455853117614278 — 🇺🇸 US (señal, sin tarjeta)
Mismo molde (guías de examen de certificación «drawn», 56-68 páginas: ICC B1/E1, NATE, CFOT, Network+, FAA IA, CAOHC, ultrasound, wastewater…). 119 activos US; los 50 más nuevos creados casi todos en las últimas ~24 h (todos entre 1795129313 y 1795131709). Cohorte 7+ = 0 visible; el slice `ICC` da 10 ads, todos de hoy. Lanzamiento reciente o copia de Visual Guide Lab; no se suma con la otra fanpage.

### Music Solved — page_id 1465563836630767 — 🇺🇸/🇬🇧 (señal, sin tarjeta)
«Master Your <instrumento> · System 365» (guías de instrumento, un SKU por instrumento). US 189 / GB 179 activos. Los 50 más nuevos US son todos ≤ 5 días. Slice `banjo`: 14 ads, cohorte 7+ = 4 (edades ~12 d). Fábrica multi-SKU de churn; por SKU no llega a 10. Embudo no verificado.

### Descartados del barrido (no pasan la vara o gate)
- Mariana Williams Creations (1249006671639277): 208 activos US, todo creado en los últimos 3 días, multi-SKU de miles (costura, crochet, lawyers AI prompts, afasia, capillas…) → fábrica de churn, cohorte 0; además mezcla religioso/manualidades (excluidos).
- Craft Room Co (1377944112064659): 13 activos US, un solo creativo «280+ Ready-to-Use Planners», cohorte 7+ = 4 → tester.
- World Prepared (710913458782727): 17 ads, todos ≤ 3 d, kit físico/preparación → churn.
- Pro Design Flow · Printable Planners: 5 ads de ayer, todos de la misma hora → churn.

## Veredicto provisorio
OBSERVAR / SUBNICHO-candidato: **guías ilustradas de examen oficial (certificaciones, licencias, exámenes) como PDF de US$ 27 con 2 bonos** — mismo molde repetido por dos páginas (Visual Guide Lab y Fenix Library), un SKU por examen. Par fuente → destino: US (oferta validada solo por 11 ads de 9 d, no por escalonamiento) → llevar a 🇬🇧 GB solo si se confirma (ellos ya anuncian UK PPL/Day Skipper/CPC en GB, ventana cerrándose) o traducir el molde a 🇧🇷 BR (exámenes ENEM/OAB/CNH/concursos) · 🇪🇸 ES · 🇮🇹 IT · 🇩🇪 DE. Nunca DESCARTAR.

## Cobertura
| Keyword | País | ACTIVE | ALL | Qué trajo |
|---|---|---|---|---|
| printable planner | US,GB | 700 est. (50 leídos) | — | fábricas de churn (Pro Design Flow, Mariana Williams, Music Solved, Craft Room Co) |
| payhip | US,GB | 716 est. (30 leídos) | — | ruido (regalos, cursos, libros); nada modelable |
| spreadsheet template | US,GB | 281 est. (30 leídos) | — | servicios/SaaS, plantillas de boda; nada que pase |
| study guide pdf | US,GB | 507 est. (30 leídos) | — | Visual Guide Lab, Fenix Library (origen del hallazgo) |
| page_ids 1249006671639277 / 1465563836630767 / 1377944112064659 / 710913458782727 | US | 208 / 189 / 13 / 17 | — | ver arriba |
| page_ids 1467890346400480 + `pilot` | US | 30 | — | cohorte 7+ = 11 |
| page_ids 1467890346400480 | US / GB | 168 / 94 | — | los 50 más nuevos < 5,5 d |
| page_ids 1455853117614278 (+ `ICC`) | US | 119 / 10 | — | todo de hoy |
| page_ids 1465563836630767 + `banjo` / `guitar` | US | 14 / 0 | — | cohorte 4 / 0 |

Trampas nuevas: (1) `page_ids` en páginas con >50 activos devuelve siempre los 50 más nuevos → la cohorte queda invisible; usar `search_terms` por SKU junto a `page_ids` + `countries` para ver la cola vieja. (2) `printable planner` en EN trae sobre todo fábricas multi-SKU que recrean todo cada 2-3 días (cohorte 0): contar por SKU. (3) El API no devuelve el link de destino: el `ad_snapshot_url` abierto con Firecrawl (`firecrawl_scrape` sobre la URL de la Biblioteca) sí muestra copy y link — sirve para verificar embudo desde la nube cuando WebFetch no llega.
Nodos nuevos propuestos para la cola: `exámenes-certificaciones/guias-ilustradas` (aparecido por huella el 2026-11-20; EN US/GB; `superficial`) con hijos aviación (Part 107, PPL), radioamateur, oficios (ICC, NATE, plomería, boiler), marítimo, TI (Network+), UK (PPL, Day Skipper, CPC).

## Lo que no se pudo verificar
- Cohorte total de la página (tope 50 de la API); solo el slice `pilot`.
- Checkout real (no recorrido; no se compra) y existencia de upsells.
- Snapshots de imágenes/videos (403 desde la nube salvo vía Firecrawl, que mostró el texto pero no el video).
- Hueco de arbitraje en destinos distintos de US/GB.
- Nombres/identidad del operador detrás de las dos páginas (Fenix Library y Visual Guide Lab parecen la misma mano).
