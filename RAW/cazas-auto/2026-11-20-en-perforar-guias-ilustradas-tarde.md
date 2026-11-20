# EN · 2026-11-20 (tarde) · B perforar · exámenes-certificaciones/guias-ilustradas

Corrida: 18:38 Europe/Madrid, viernes. Corte de cohorte 7+ = creación ≤ 2026-11-13 ~17:40 UTC (epoch 1794591592). Todos los nodos `superficial` con mercado EN estaban tocados hoy (idiomas por EN mañana; examenes-y-oposiciones por BR tarde), así que se perforó el nodo propio de EN por examen. Evidencia: API; ads, copy y landing leídos con Firecrawl (snapshot/landing); WebFetch no resuelve `quicklyguide.com` desde la nube.

## Keywords (paso 1, US+GB+CA+AU, ACTIVE)
1. `pilot exam study guide` — 124 resultados; Visual Guide Lab, Clearpage Books, Sporty's Pilot Shop (curso en video), Checkride Study Guide, Pilot Avabelle, Drone Training School, Ricardo Augusto (sectional chart).
2. `NCLEX study guide pdf` — 6 resultados; NurseNessa.com (2 ads), Nursing Nerds (3, guía gratis), healthcareheirlooms (Etsy). Nada que medir.
3. `electrician exam visual` — 18; Visual Journeyman Style, Visual Guide Lab (Red Seal, Home Inspector), Studio Facile.
4. `real estate exam cheat sheet` — 42; Stark Exam Prep, Realestateiq, ClearPass Exam Guides (moneda BRL: no es US), Sofia Martinez (mismos ads de Stark).

## Conteos (paso 2: `page_ids` + país; cohorte = sobrevivientes)
| Página | page_id | País | Activos | Sobrevivientes (creación / entrega) | Lectura |
|---|---|---|---|---|---|
| Visual Journeyman Style · «Journeyman Exam Made Visual» US$ 19 | `1517462271441246` | US | 10 | 9 / 9 (7 ads del 09-nov creados, 2 del 11-nov; entrega 10-12 nov). 1 de los 9 con «<100 impresiones» → 8 firmes | **CERCA** (7-9). GB CA AU: 0 activos. `ALL` US = 10 (nada apagado) |
| Stark Exam Prep · examen de real estate | `1320551981152367` | US | 28 | 0 / 28 (el más viejo creado 16-nov, 4 d) | tanda nueva; ALL = 28, nada apagado |
| Checkride Study Guide | `470054809533979` | US | 152 (50 devueltos, piso) | ≥ 20 en los 50 visibles, pero **producto físico** («ships to your door», decks de tarjetas) | Filtro D, fuera |
| Pilot Avabelle = AirlinesOnAutopilot | `842356615617987` | US | 37 | lesson plans CFI/CFII/MEI editables: 6 / ~6 (desde 05-oct, 46 d); study guides: 3; resto = Black Friday multi-oferta | **VIGILANCIA** en lesson plans; ver Filtros |
| Clearpage Books | `1452448654619131` | US | 119 | 0 (50 visibles, todos del 20-nov) | fábrica de tandas nuevas: 1 SKU por examen (PE Civil, FE Electrical, Part 107, Medical Coding, Notary CA, EV Charger, General Class…) con «+2 bonus books»; mismo molde que Visual Guide Lab; cohorte invisible por el tope |

## Gate de Visual Journeyman Style (no es tarjeta: conteo 9 < 10)
- A marca personal: página fantasma, sin cara ni nombre de persona; copy en voz de «estos mapas». OK.
- B embudo (verificado por Firecrawl): ad → landing `visual-journeyman-style-electrician-exam.quicklyguide.com` (venta directa) → `/checkout`; oferta «Launch offer — valid today only» con reloj (countdown 11:19:05). Checkout no recorrido, upsells no vistos. Imágenes en `cdn.impultienda.ar` → plataforma Impultienda.
- C back-end: vende solo el PDF + 4 bonos; sin back-end visible.
- D entregable: PDF de 100 mapas ilustrados NEC 2023 + 4 guías (Dwelling Service Calculation Cases, plan de 8 semanas, Spot the Violation, Formula Quick Sheet). Producible. US$ 19 (tachado 49; «valor 101,60»). Garantía 30 días.
- Score parcial: longevidad 10 d (<45), volumen 9-10 (<50), duplicación 7 veces el mismo creativo con 10 variantes de hook (H02…H10) → señal débil, hueco: sin barrer. ≤ 1/4.
- Mismo molde que Visual Guide Lab (guía «Made Visual», impultienda, +bonos). Las dos páginas son ghost-pages de una misma familia probable (no verificado).

## Pilot Avabelle / AirlinesOnAutopilot (no tarjeta)
Página «Pilot Avabelle» con la marca AirlinesOnAutopilot (tienda Shopify). Ofertas: lesson plans editables CFI/CFII/MEI (US$ 88-120), bundles de study guides ($36-60), y «un año de AOA Pilot Prep US$ 99» con **video lessons y quizzes (suscripción)**; copy «built by a former checkride examiner» (experto con credenciales). Filtros A-bis y D la dejan fuera como oferta modelable salvo los lesson plans editables; ese SKU suelto tiene ~6 sobrevivientes → vigilancia, re-conteo 2026-11-27.

## Descartes/hechos por eje × mercado (sin DESCARTAR)
- NCLEX/enfermería US: 6 resultados en 4 días de datos, 0 ofertas con cohorte; keyword `NCLEX study guide pdf` solo trajo gratis/Etsy; un nivel mirado. No concluye nada del mercado.
- Real estate exam US: Stark Exam Prep lanzó 28 ads en 4 días (0 sobrevivientes); re-conteo 2026-11-27.

## Cobertura
4 keywords (paso 1) × 4 países, 10 conteos por `page_id` (US; GB CA AU unión solo para Journeyman), 3 scrapes de snapshot, 1 scrape de landing. Subnichos mirados: aviación/piloto, electricista, real estate, enfermería. No miradas: radioaficionado, plomería, marítimo, UK PPL, TI (CompTIA), CDL/camión, bomberos, EMT — siguen abiertos. `guias-ilustradas` queda como `superficial` (4 de 12 examenes mirados).
