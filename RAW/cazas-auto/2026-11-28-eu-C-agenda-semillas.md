# EU · sáb 2026-11-28 · modo C agenda + 20 semillas (corrida 02:40 Europe/Madrid)

## Resumen
- 3 tarjetas: **KINEA IT** (`1304154212788791`), **KINEA DE** (`1417660961430039`) y **Thomas Bernard FR/BE** (`1257844197417780`, sube de señal 0 / 31 del 23-nov a pasa).
- Modo C: agenda vacía en `cazas/cazas.md` → operadores EU (5 filas más viejas de la ronda) + nodos `virgen` EU como keywords propias.
- Reloj de referencia: hoy 00:00 UTC = 1795824000; 7 d = `ad_creation_time` ≤ 1795225200 (aprox. 21-nov 08:00 UTC).

## Embudo
- Etapa 1: 40 keywords × IT CH FR BE DE AT PT NL, en 4 subagentes Haiku (los 4 devolvieron tabla completa; el de alemán necesitó reintentos con `ALL` por ceros). Observación de los subagentes: en `atlas anatomie yoga`/`fiches biologie médicale` la respuesta fue idéntica en FR, BE y CH (el filtro de país no separa siempre); se contó por `page_ids` + país en la Etapa 2.
- 20 propias (operadores + nodos virgen EU): `atlante anatomia`, `schede visive psicologia`, `mappe mentali inglese`, `kit successione`, `classificatore documenti` (IT/CH) · `atlas anatomie yoga`, `fiches biologie médicale`, `fiches troubles mentaux`, `classeur succession`, `cartes mentales anglais` (FR/BE/CH) · `Anatomie Atlas`, `Landkarten Physiotherapie`, `Mindmaps Psychologie`, `Dokumentenordner Erbfall`, `Sprachkarten Spanisch` (DE/AT/CH) · `atlas anatomia`, `fichas visuais psicologia` (PT) · `anatomie atlas`, `mindmaps psychologie`, `nalatenschap checklist` (NL/BE).
- 20 semillas, tal cual: `foglio excel`, `accesso immediato`, `kit digitale` · `guide pratique`, `tableau excel`, `accès immédiat` · `pdf download`, `sofortiger zugriff`, `digitales paket` · `pdf downloaden`, `complete gids` · `por apenas` (PT) · molde × tema: `cuccioli addestramento`, `primo soccorso schede`, `premiers secours fiches`, `échecs ouvertures`, `Hundetraining Anleitung`, `Erste Hilfe Karten`, `primeiros socorros guia`, `hondentraining gids`.
- Etapa 2: ronda de operadores (5 + 2 extra de PhysioAtlas) + 11 pasos rápidos + 3 completos + 4 `firecrawl_scrape` (3 snapshots/landings KINEA IT, Thomas Bernard, KINEA DE + 1 snapshot) .

## Ronda de operadores (Etapa 0)
| Operador | País | Resultado |
|---|---|---|
| Esprit Académique `1229441186928180` | FR | 115 activos, tope 50. SKU nuevo «+300 Cartes Mentales pour Apprendre l'Espagnol»: 17 visibles, creados 25-26 nov (< 7 d) → re-conteo 12-02. «210 Fiches Visuelles»: 33 visibles de 13-oct a 06-nov (ya tarjeta). |
| Axon Academy / Camille Dubois `1077014278820945` | FR | 289 activos, tope 50. Tanda nueva 26-nov «520 cartes mentales · de A1 à C2» y «520 cartes + 6 bonus · 12,90 €» (≈ 33 ads, mismo producto) sobre la tanda «Black Friday 12,90 €» del 20-nov (17 visibles). Oferta conocida (La Carte de l'Anglais). |
| Camille Laurent `1407481519105013` | BE | 54 activos, tope 50. «150 fiches d'anatomie de la musculation» ≈ 28 activos desde 14-nov, sin SKU nuevo de infoproducto (resto del catálogo en nicho excluido). |
| Download Studio `1344017652136102` | CH | 41 activos: packs docentes, «The Complete Research Methods Course», «Black Friday $97 → $17» (13 ads) casi todo creado 26-27 nov (< 7 d); el más viejo 16-nov (4 ads). Re-conteo 12-02. |
| PhysioAtlas Visuell `1356253604249122` | DE, CH (+AT por el barrido) | **0 activos** en DE y CH con `ACTIVE`; `ALL` 73 ads en DE (el último creado 24-nov). Oferta apagada entre el 24 y el 28-nov. |

## Páginas verificadas
| Página | Oferta | Países (tablas) | Conteo `sobrev. / activos` | Veredicto |
|---|---|---|---|---|
| KINEA · Anatomia dello Yoga `1304154212788791` | Anatomia dello Yoga (120 asana + atlas 28 músculos + 6 clases + 4 bonos + app) US$ 19,99 | IT (apareció solo en IT) | 🇮🇹 **≥ 36 / 50** por creación (≥ 28 por entrega; 110 activos est., tope 50, título único repetido: no hay corte posible); más vieja 10-nov (18 d); 4 tandas | **pasa** (tarjeta) |
| KINEA Yoga Anatomie `1417660961430039` | Yoga-Anatomie für Lehrende (misma oferta en alemán) | DE | 🇩🇪 **27 / 27** (por creación y por entrega); más vieja 25-oct (34 d); 3 tandas (25-oct, 30-oct, 01-nov) | **pasa** (tarjeta) |
| Thomas Bernard `1257844197417780` | 160+ Cartes Visuelles de Neuroanatomie, 9,99 € | BE, CH (tablas); FR (re-conteo) | 🇫🇷 **32 / 32** con corte `Neuroanatomie` (29 por entrega; más vieja 17-nov, 10 d); 🇧🇪 ≥ 19 visibles en la consulta de 50 + `ALL` «Neuroanatomie» 26; 🇨🇭 3 | **pasa** (tarjeta). 310 Cartes Mentales d'Informatique: 🇧🇪 25 / 31 con corte `Informatique` (+ 12 ads «SEULEMENT 9,99 €» de ≈ 74 d que entran por el término; oferta sin confirmar) |
| Le trauma `1396189266918590` | 100 cartes visuelles (trauma) | BE | 🇧🇪 **8 / 41** (8 ads creados 18-19 nov; el resto 23-27 nov) | **cerca** → señal, re-conteo 12-01 |
| Allenamenti Calcio Pronti `1264730710065283` | sedute di calcio pronte, desde 9,90 € | CH | 🇨🇭 **6 / 22** (4 «Solo oggi» + 2 «Mister Pro») | vigilancia, re-conteo 12-01 |
| Visiva · Psicologia e Medicina `1442146142313710` | Psicopatologia Visiva 200 schede / Psicologia dello Sviluppo | IT | 🇮🇹 5 / 18 repartidos en 3 ofertas (≤ 2 por oferta) | [<4] por oferta |
| Inglese Facile `1475948585604153` | 520 mappe mentali + 5 bonus (molde Lingua Chiara / Camille Dubois) | IT | 🇮🇹 0 / 28 (tanda 26-nov; 5 ads «4,9/5» cumplen 7 d el 28-nov) | señal, re-conteo 12-02 |
| STEM in Classe `1346477118548768` | Robotica in classe | IT | 🇮🇹 1 / 21 | [<4] |
| Le Classeur de Succession `1493182943869296` | classeur de succession (herencia y papeles) | FR | 🇫🇷 0 / 18 (25-26 nov) | señal, re-conteo 12-02 |
| Premium Digital `879829245224581` | 150 schede de anatomía en frases | IT | 🇮🇹 1 / 18 | [<4] |
| BFS Academy `505995965919909` | 630 Cartes Mentales anglais | FR | 🇫🇷 0 / 5 | [<4] |
| Elena Marini `102211338515426` | portafolio (infancia, nutrición, pareja) | IT | 22 activos, todo 26-27 nov, multi-vertical | no verificada (portafolio) |

## Gate (landing por Firecrawl)
- **KINEA IT**: ad 2543367602814932 → `kyit.didactalab.online` (Impultienda, `cdn.impultienda.ar`). 120 asana con músculos en color, atlas de 28 músculos, 6 lecciones de 60 min, 4 bonos (embarazo, columna, suelo pélvico, kit docente), PDF A4 imprimible + **app de regalo**; US$ 19,99 pago único, garantía 30 d; «KINEA» sin persona, ilustraciones generadas con IA; sin WhatsApp. Filtro A ✅, B ✅, D con salvedad (PDF + app de regalo, igual que la tarjeta BE·FR del 23-nov).
- **KINEA DE**: ad 1525873779380268 → `kyde.didactalab.online`; resumen Firecrawl: misma oferta traducida, 120 Haltungen, Atlas 28 Muskeln, 6 Stunden, 4 Boni y App. Precio y checkout no leídos en detalle (resumen) → «mismo molde que kyit».
- **Thomas Bernard**: ad 1175658195415663 → `neuroanatomie.netlify.app` → checkout Hotmart `pay.hotmart.com/K108541723R`; 160+ cartas ilustradas, 12 módulos, 4 bonos, formato digital + imprimible, **9,99 €** (tachado 29,99), pago único, garantía 7 d; sin nombre ni foto de persona en la landing (el nombre «Thomas Bernard» es solo el de la página); sin WhatsApp. Filtro A ✅ (parcial por el nombre de página), B ✅, D ✅.

## Dónde ya se probó y falló (ALL)
- Thomas Bernard BE `ALL` «Neuroanatomie»: 26 ads, sin apagados que se vean (misma lista que `ACTIVE`).
- KINEA IT `ALL` «yoga»: 196 ads, tope 50 (los 50 más nuevos coinciden con `ACTIVE`).
- PhysioAtlas DE/AT/CH: ver ronda (apagada).

## Señales y molde en otros mercados
- Molde «atlas de anatomía para profesores de yoga» ya en 5 idiomas: KINEA IT/DE (pasan), Didactalab FR/BE (tarjeta 11-23), Piccoli Artisti (`1436378079551836`) FR/BE/CH 10 ads cada una creados 24-nov, Yoga Anatomy Atlas PT (`1346454768560529`) 2, Maria Antônia PT (`597983353401665`) «+300 Fichas Ilustradas de Músculos» 3.
- Studio Facile (`1272162682644374`, ya seguido): 35 activos BE / 25 NL «Psychologie in beeld» creados 24-nov (< 7 d).
- Logomap (`1431700070027701`, DE/AT/CH, «Logopädie visuell erklärt», 4 ads del 25-nov), Emito (`557352500802762`, «Mathestunden fertig vorbereitet», DE/AT/CH ~4 desde 13-nov), Punctum Atlas (`1436741269530533`, NL/BE, 102 triggerpointkaarten, 2).
- Ceros: `Dokumentenordner Erbfall` y `Sprachkarten Spanisch` 0 también con `ALL` en DE/AT/CH; `classificatore documenti` y `kit successione` IT/CH sin infoproducto (CH solo series cortas); `Landkarten Physiotherapie` solo PhysioAtlas apagada.
- Descartes de gate: ninguno por gate (la nube no descarta); páginas de recetarios (Recetas para Peques + BLW, Apericena di Festa, Maribelle Montaciel), religioso (Oratorio Pronto, resto de Camille Laurent) y neurokids-adyacente (Ludika, Therapy Toolkit) ignoradas por nicho excluido; STL de impresión 3D (Sabines, Markus Weber, L'Atelier des Makers) fuera del molde (archivos para impresora).

## Fallas técnicas
- Ninguna de Meta. Los 4 lotes Haiku tardaron 4,5-6,5 min y devolvieron tabla; los conteos `~` del lote DE/AT/CH son lecturas aproximadas. El subagente FR marcó «no re-contado» en BE/CH de varias keywords.
- Huellas FR e IT/DE: quedan 9 nunca usadas por idioma (aviso del script); huellas nuevas agotadas en alemán y francés casi.
