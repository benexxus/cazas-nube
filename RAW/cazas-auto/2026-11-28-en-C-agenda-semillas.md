# Caza automática — EN · C agenda + operadores + 20 semillas — 2026-11-28 (sáb)

Reloj de corte: ahora = 1795824683 (unix) → 7 d = creación ≤ 1795219883. Todo conteo `ACTIVE` por `page_ids` + país, API.

## Etapa 0 — ronda de operadores (5 filas EN, todas con chequeo 11-24)
| Operador | page_id | País | Resultado |
|---|---|---|---|
| Ultimate Budget Planner | `485276957995076` | US | 28 activos, 27 con 7+ d; títulos nuevos = variantes del mismo producto (Debt Payoff 14 de 12-sep, Budget Planner 14); sin SKU nuevo. Ya tarjeta 11-22. |
| Visual Guide Lab | `1467890346400480` | US | 111 activos (194 el 11-23); 50 visibles todos de ≤ 4,2 d; SKUs nuevos (GD&T, CPC coding, A&P mechanic, fire alarm, ham radio, soldadura, reglas de navegación…): 0 sobrev. visibles. Re-conteo 12-01. |
| Digital books | `1324311660754895` | US | 161 activos, 50 visibles (NEUROMAP y FARMSTEAD, lote del 26-nov y del 20-21-nov); sin SKU nuevo en lo visible. Ya tarjeta 11-24. |
| Labdigital | `1332998043219880` | US | 346 activos, 50 visibles. SKUs nuevos (todos < 7 d): CONTAINER HOME BLUEPRINT 7, GLAMPING SITE BLUEPRINT 9, THE HANGAR ATLAS 10 (corte `HANGAR ATLAS`: 10 activos, 0 sobrev.), TAROT MAP 4; fuera de alcance: «Screen-Free Bible Year» (religioso) y «Home Care Atlas — Dementia» (cuidado de adulto mayor, no se sigue). VAN BUILD BLUEPRINT, PHYSIO QUICKMAPS y Anesthesia siguen. |
| Creativo Digital | `1291119130753272` | US | 120 activos, 50 visibles; corte `smoker`: 24 activos, **11 sobrev. de «Weld your own smoker»** (era 10 / 14 el 11-24): sigue pasando. SKUs nuevos < 7 d: sauna (30 planos), brick pizza oven (36), trailers, corral gate, livestock panels, forging press, power hammer (≈ 6 d). |

## Agenda vencida (modo C)
| Oferta | page_id | Resultado |
|---|---|---|
| Visual Journeyman Style | `1517462271441246` | **0 activos** en US (el 11-24: 10 / 10 cerca): apagada. |
| Spanish Made Visual | `1456443927546734` | **pasa** (ver Candidatos). |
| German Grammar Made Visual | `1469941799530737` | US 24 activos, **9 sobrev.** (6 del 19-nov + 3 del 15-nov); 3 más (lote del 20-nov) cumplen 7 d en horas → cerca, re-conteo 12-01. GB/CA solo vistos en barrido (24 / ≈21 activos). |
| Fluency Mapped | `1382560178271800` | US 119 activos. Corte `French Mapped`: 18 activos, todos del 11-21 (6,98 d): 0 hoy, cumplen 7 d el 28-nov a las ~02:00 (por entrega: 28-nov ~13:30). Corte `Spanish Mapped`: 101 activos, 50 visibles, **≥ 15 sobrev. visibles** (11 del 18-nov + 4 del 14-nov) → **pasa por piso** (Candidatos). Italian: 0. |
| Central Pack | `1178523422005192` | US 86 activos, 50 visibles; 3-4 por tema («Professional Edition»), ningún título ≥ 10 → vigilancia multi-tema. |
| Circuit Bench / Megan Hayes / Classroom Makers / Speak Clearly | — | no se re-contaron hoy (no están en la ronda; quedan para la próxima corrida). |

## Etapa 1 — barrido ancho
40 keywords × US GB CA AU en 4 subagentes. **Haiku devolvió tablas incompletas en los 4 lotes** (lote 1: 18 de 40 combinaciones tabuladas; lote 2: 7 de 10 keywords sin reparto por página; lotes 3 y 4 completos pero con conteos a ojo). Se repitieron con Sonnet: lote 1 en dos mitades (completas) y las 7 keywords incompletas del lote 2 (completo). Los subagentes mandaron `client_model` de Haiku; sin consecuencias para los datos.
- 20 propias (modo C: temas de operadores y agenda): build blueprint · camper van build · smoker build plans · welding project plans · neurology study system · anatomy quickmaps · spanish made visual · german grammar maps · language mind maps · pilot study guide · ham radio exam · debt snowball planner · budget by paycheck · tiny house plans · chicken coop plans · heavy equipment guide · diesel troubleshooting · electrician exam visual · homestead blueprint · ECG study guide.
- 20 semillas (nunca usadas): word-for-word scripts · copy and paste scripts · plug-and-play templates · SOP templates · printable charts · printable guided journal · study pack · practice tests · exam cram · pass on the first try / pass first time · revision pack · only $12 + 8 molde × tema: contractor estimate templates · small business bookkeeping · CBT worksheets · motorcycle repair diagrams · medical coding cheat sheet · HVAC certification study · credit repair templates · shadow work prompts.
- Páginas que salieron con interés: Van Build Made Visual `1353418764530851` (GB 13 / CA 9 / AU 9, todo del 22-nov), Shop Plans `1354104621129963`, Daniel Brooks `1365061430024484`, Alisson Drusk `1455127851013740`, Master Crafts DIY `945872361934854`, The Weekend Fabricator `964653193405481`, Fluent Maps `1291488517375234`, Med Ops Manuals `847783225082919`, Natsai R `108606542277341`, Lumera `1372320049290124`, Smart Digital `1383014634885117`, Studio Facile, Debt Free Progress Pack `1498244013374495`, FocusFlow `1128641823676223`.

## Etapa 2 — verificación

| Página | País | Paso | Resultado |
|---|---|---|---|
| Spanish Made Visual · French Made Visual | US | ACTIVE 40 | 17 por creación / **12 por entrega** (6 del 16-nov, 6 del 13-nov) + 5 del 20-nov (6,6 d por entrega) |
| | GB | 41 | igual: 17 / 12 |
| | CA | 41 | igual: 17 / 12 |
| | AU | 33 | 15 / **10** (borde) |
| Fluent Maps · German Illustrated | US GB CA AU | 19 activos en cada país (los mismos 19 anuncios corren en los 4) | **19 / 19** (más viejo 13-oct, 46 d; último lote 6-nov) |
| Shop Plans · Welder's Treasure Pack | US | 122 activos, 50 visibles (todos creados 20-nov, ≥ 7,9 d) | ≥ 50 por creación / ≥ 23 por entrega (piso) |
| | CA | 110 activos, 50 visibles | ≥ 50 por creación / ≥ 27 por entrega (piso) |
| | GB | 9 activos | otra oferta («Budget-Friendly House Plans») |
| Fluency Mapped · Spanish Mapped | US | ver arriba | ≥ 15 (piso, 101 activos «Spanish») |
| Med Ops Manuals | US | 43 activos | 4 sobrev. (los «How many SOPs» del 27-oct); lote nuevo «Black Friday $2,499» < 7 d; ticket US$ 2.499 → vigilancia |
| Natsai R | CA | 25 activos | 5-6 sobrev. («CRA Is NOT Your Friend» 4, resto < 7 d); persona + contabilidad → vigilancia, gate A dudoso |
| Van Build Made Visual | GB | 13 activos | 0 (todos del 22-nov); re-conteo 12-01 |
| Daniel Brooks | US | 164 activos, 50 visibles | portafolio («Psalms in Blues» religioso/música, «350 Farm Building Plans», «200 PVC Pipe Projects»); oferta «4,000+ Welding Plans» de la misma familia que Shop Plans |
| ALL (Spanish Made Visual, «French») | US | 218 con tope 50 | tests apagados: lotes del 9, 11 y 15-nov (decenas) |
| ALL (Fluent Maps) | US | 191 vs 19 ACTIVE | 172 apagados: churn alto, renuevan creativos; nada nuevo en los últimos 5 d |

### Gate (landings con Firecrawl `maxAge: 0`)
- **French Made Visual** (`french-made-visual.impultienda.ar`, snapshot del ad `4599759286937866`): «100+ Printable French Mind Maps (A1→C2)», US$ 19 tachado 97, pago único, PDF imprimible «también en el celular», checkout propio `/checkout`, garantía 30 días «It Clicks», contacto `ebooksgestion@gmail.com`, sin persona ni redes ni WhatsApp. Hermana: `spanish-made-visual.impultienda.ar`. A ✅ B ✅ C ✅ D ✅ (red Impultienda; mismo operador que Atlas Terapeutic Vizual / PhysioAtlas / Edu Digital, ya cazados en otros mercados).
- **FluentMaps** (`german.fluentmaps.com`, `spanish/korean/japanese.fluentmaps.com`): «+500 visual mind maps», US$ 17 pago único (tachado 47), 4 bonos, imprimible o en pantalla, checkout `pay.hotmart.com/K106628822B`, garantía 30 días, sin persona, sin footer ni redes. A ✅ B ✅ (checkout Hotmart) C ✅ D ✅ (mapas PDF/imprimibles; no se pudo ver si se entrega en área de miembros de Hotmart → verificar en la PC). Es la versión en inglés del mismo producto que Sprachfluss-Karten (EU, `1173721545831519`).
- **Welder's Treasure Pack** (`welders-treasure.online/en-us/`, snapshot del ad `1438664154557129`): «4,000+ metalworking plans» con lista de materiales, cortes y dimensiones; Basic US$ 9 / Professional US$ 17 / add-on US$ 12; 4 bonos; acceso de por vida por correo; checkout en el mismo dominio; garantía 7 días; sin persona (reseñas con nombre), sin footer ni about. A ✅ B ✅ D ✅. **Pero:** la misma oferta «4,000+ Welding Plans / Build & Profit» corre en al menos 4 páginas distintas (Shop Plans, Daniel Brooks, Alisson Drusk, Master Crafts DIY, The Weekend Fabricator con «1,500+ plans») → probable pack con derechos de reventa/PLR (patrón que ya cayó en el cerebro). Va a tarjeta con la advertencia.
- **Fluency Mapped / Spanish Mapped** (`oakguides.com/spanish-mapped/`, verificada el 11-20): 520 mapas PDF + área de miembros + 5 bonos, US$ 14,90, Hotmart. **D dudoso** por el «área de miembros» (contenedor de PDFs). No se reabrió hoy.

## Señales sin tarjeta
Ver bandeja («Señales del día EN (28-nov)»).

## Trampas nuevas
`word-for-word scripts` · `copy and paste scripts` · `plug-and-play templates` · `only $12` · `pass on the first try` (EN): novelas y short-dramas (Romance Novel, Endless Stories, Novels Lover), gadgets, gimnasios; cero infoproducto. `credit repair templates`: servicios. `tiny house plans` / `chicken coop plans`: novelas (Click to Read). `budget by paycheck`: short-dramas y agencias. `study pack`: novelas. `exam cram` solo da Stelloway (libro). `build blueprint` y `heavy equipment guide`: coaching y vacantes. Rindieron: `welding project plans` (red «4,000+ Welding Plans»), `camper van build` (Labdigital, Van Build Made Visual), `smoker build plans`, `language mind maps` (Fluent Maps), `spanish made visual`, `SOP templates` (Med Ops Manuals, Dragon Fire Method, Kit Online), `printable charts` (Lumera).

## Cobertura / lo que no se pudo verificar
- Haiku incompleto en los 4 lotes (ver Etapa 1); `ham radio exam` GB/CA/AU devolvió los mismos 3 anuncios.
- Conteos de subagentes a ojo ±1-2; todo lo que llegó a tarjeta se recontó por mí con `page_ids`.
- Checkout no recorrido; longevidad por API, snapshot no verificado desde la nube más allá de Firecrawl.
- No se contó GB/CA/AU de Fluency Mapped ni AU de Shop Plans en profundidad.
