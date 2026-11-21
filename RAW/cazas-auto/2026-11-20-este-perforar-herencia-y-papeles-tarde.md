# Caza automática — ESTE · B perforar · herencia-y-papeles (tramo Este) — 2026-11-20 (tarde)

Reloj: ahora ≈ 2026-11-20 17:55 UTC (epoch ≈ 1795197000); corte 7 d = epoch 1794592200. Evidencia: API; snapshot y embudo **no verificados desde la nube** (los ads no traen URL de landing en el copy).

## Shortlist
**Mente que sana** (page `1090738757452147`) — «Dosarul Familiei» 🇷🇴 RO (ganchos: «5 telefoane pe care va trebui să le dea copiii», «Ce face banca când află de deces», «caietul gol», «Două familii. Aceeași săptămână. Doar una are un dosar»).
- RO `ACTIVE`: 59 activos (limit 50 lleno → piso). Entre los 50 más nuevos: **11 sobrevivientes** (creación ≤ corte, y también por entrega: 11/11 con `ad_delivery_start_time` ≤ corte; edades 7,2-8,6 d). Los ≥ 9 restantes (más viejos) quedan fuera del tope: **≥ 11 / 59 (piso)**. Dos tandas: 12-nov (≈3 ads, ~8,6 d) y 13-nov (≈8 ads, ~7,6 d); luego tandas del 15, 17, 18, 19 y 20-nov (todo < 7 d). Veredicto: **pasa (≥ 10)**, con salvedad: margen de 1 punto, tandas apenas cruzando 7 d.
- Mismo operador, misma oferta/ángulo en otros mercados: página en CZ («Rodinný šanon», ALL 228 ads PL+CZ de la página, `ACTIVE` CZ = 0 y PL/HU = 0 — inconsistencia ALL/ACTIVE anotada, ver trampas); `Klidné předání` (page `1251607391377130`, CZ, «Celá složka: 60 stran a 3 dárky», plan 5-30-6): ALL ≈ 130, ACTIVE 2 (6,3 d) → **0 sobrevivientes, apagó casi todo**; `Querida Familia` (page `1337262539475727`, HU, «5 hívás… sorrendben»): ALL 48, ACTIVE 0 → probó y apagó. `Aurevia` (page `695152860353061`, «sistemul 5-28-6»): 1 ad antiguo, 0 activos en los 4 países.
- Página fantasma (sin persona en nombre ni títulos). Pero la página es multi-vertical (también «Pregătit, atenție, TATĂ – primul an de paternitate» en CZ): el conteo es solo sobre la oferta Dosar.
- Formato del entregable **no verificado**: «Așa arată Dosarul Familiei pe dinăuntru — pagină cu pagină» y «Celá složka: 60 stran a 3 dárky» sugieren carpeta PDF imprimible de 60 págs + 3 bonos; también compite contra «caietul gol» (cuaderno físico). Filtro D (físico) a confirmar en la PC.
- Precio/moneda: ads en USD (la moneda del anunciante no dice el país).

## Veredicto provisorio
ENTRAR → ya está en RO (destino y fuente); observar re-conteo 2026-11-27. Llevarlo a 🇵🇱 PL/🇭🇺 HU: HU y CZ ya probados y apagados por el mismo operador (dónde falló: HU Querida Familia 0 activos, CZ Klidné předání 2 activos). Nunca DESCARTAR.

## Descartes de esta corrida (por eje × mercado)
- Twoja Czerwona Teczka (page `1166102073252078`, PL): «kompletny organizer», «z darmową dostawą» → **carpeta física**, 3 activos (7-8 d) → Filtro D, 3 sobrev.
- Ordino (RO) y Vivva RO: productos físicos de hogar / organizador magnético → fuera.
- Wydawnictwo Dobrze Wiedzieć (page `1325462587327331`, PL): «Testament i spadek — 39,99 zł» y e-books a 39,99 zł (PDF), pero los 6 ads de la oferta son de 2,6 d → 0 sobrev.; portafolio (recetario/calendario lunar/piedras) → señal.
- ESET, Dubai Connect, Future Insight Center, Hot Off the Press, Morefic003, funerare24ro: ruido/otras ofertas.

## Cobertura
| Keyword | País | ACTIVE | ALL | Qué trajo |
|---|---|---|---|---|
| dokumenty rodzinne segregator | PL | 3 | — | Twoja Czerwona Teczka (físico) |
| spadek dokumenty poradnik | PL | 1 | — | Dobrze Wiedzieć (39,99 zł) |
| testament wzór pdf | PL | 0 | — | nada |
| po śmierci bliskiego dokumenty | PL | — | 36 | ruido (webnovelas, abogados) |
| organizator documente | RO | 14 | — | Ordino, Vivva (físicos) |
| după deces documente ghid | RO | — | 16 | **Mente que sana**, funerare24 |
| moștenire acte ghid / testament model succesiune | RO | — | 5 / 1 | Aurevia, ruido |
| pozůstalost dokumenty / dědictví pozůstalost průvodce / závěť vzor | CZ | 2 / — / — | — / 0? / 2 | ESET (ruido), Klidné předání |
| hagyaték iratok / öröklés végrendelet útmutató / végrendelet minta / halál után teendők mappa | HU | 0 / — / — / — | — / 8 / 24 / 48 | The Dubai Connect, ruido, **Querida Familia** |
Conteos por page_id: Twoja Czerwona Teczka PL (ALL 26/ACTIVE 3), Ordino RO, Dobrze Wiedzieć PL (ALL 19), Klidné předání CZ (ACTIVE 2, ALL ≈130), Querida Familia HU (ACTIVE 0), Mente que sana RO (ACTIVE 59 / ALL 63 con `Dosarul Familiei`), PL+CZ+HU de Mente que sana (ACTIVE 0), Aurevia (0).

Trampas nuevas: (1) `ALL` con `page_ids` en CZ/PL de Mente que sana trae 228 ads pero `ACTIVE` en CZ/PL/HU da 0: contradice ads con `delivery_start` de hoy → no confiar en `ALL` para estado y repetir con otro corte (país suelto) antes de decir «apagado». (2) `search_terms` con diacríticos (`šanon`) devolvió 0 aun con ads que lo traen en el título: usar el término sin tilde o el título entero. (3) `HU` keywords de herencia traen noticias (Lehoczki végrendelete) y «News for every day»: ruido.

## Lo que no se pudo verificar
Landing y precio de «Dosarul Familiei» (sin URL en el copy; snapshots 403 desde la nube); si es PDF o carpeta física; los ≥ 9 sobrevivientes cortados por el tope de 50; el conteo CZ real de la página Mente que sana.

## Actualización 2026-11-21 — landing verificada (Firecrawl)
Snapshot del ad `1148100024861027` abierto con `firecrawl_scrape`: «Dosarul Familiei este un fișier pe care îl primiți pe e-mail și îl tipăriți acasă», 89 lei, garantía 14 días, Ediția pentru România. Landing `productsgitals.store/pages/dosarul-familiei` (Shopify «Digital Boost», marca «Totul la zi»): advertorial de 7 motivos → CTA a `/go/ro-dosar`; oferta tachada 259 → 89 lei (−66 %); entregable 100 % digital (ghid ~30 págs, 10 fișe, 87 preguntas, 26 documentos, 8 cartas, mapa digital, ficha «Dacă mi s-ar întâmpla ceva»); ayuda por e-mail. Sin cara de dueño. Resuelve la duda de Filtro D: es PDF. Pendiente: checkout y upsells. La primera redacción decía «no verificado» por no haber probado Firecrawl.

## Actualización 2026-11-21 (2) — mismo producto que Leave It Sorted
Carlos confirmó que Dosarul Familiei = Leave It Sorted. Verificado con `firecrawl_scrape` de https://leaveitsorted.com/ (Shopify): mismo advertorial «7 reasons», mismo plan 48-30-6, checklist de 26 documentos, carta «In Case Something Happens», soporte por e-mail; edición US 57 págs / 21 secciones / US$ 53 (98 tachado); la tienda lista también una edición alemana (Der Notfallordner, US$ 39) y la marca declara ediciones British/American/Australian. El operador localiza el mismo kit por país; RO (89 lei) es otra localización. La búsqueda por texto «Leave It Sorted» en `ads_library_search` (GB, CH) devolvió ruido (matcher por token): hay que buscar por page_id de la marca, que no tengo.

## Actualización 2026-11-21 (3) — dónde corre el molde Leave It Sorted (conteos ACTIVE por API)
Corte 7 d ≈ epoch 1794620000. Hecho de hoy, no veredicto.
| Página (page_id) | País | Activos | Edad | Nota |
|---|---|---|---|---|
| My Estate Kit (1091977304009213) | 🇬🇧 GB | 37 (todos ≥ 7 d, exacto < 50) | de jun-2026 a 31-oct | «5-28-6»/«8-28-6», «Scottish family», USD → **sobrevivientes ≥ 37** |
| Plainleaf Publishing (1391989857327505) | 🇨🇭 CH | 33 | todos de 17-18 nov (≤ 4 d) | «Notfallordner zum Ausfüllen», CHF; 0 sobrev., recién lanzado |
| Leave It Sorted (1273987602462473) | 20 países en una consulta | 7 | 5 de ≤ 4 d, 2 de ≈ 43 d | no desglosado por país (EUR) |
| The Family Folder (487465484456721) | US (sin desglose) | ≥ 6 | hasta 3 semanas | «48-30-6 plan» |
| The Estate Kit (1215301468337012) | AU (sin desglose) | ≥ 5 | ago-2026 | «Australian family» |
| unterlagio.privat (1452299261289834) · Wichtige Sachen (1564720296718249) | 🇩🇪 DE | 1 / 1 | ≤ 3 d | Notfallordner |
| Mente que sana (1090738757452147) | 🇷🇴 RO | 59 | ≥ 11 de ≥ 7 d | Dosarul Familiei; CZ/HU/PL = 0 hoy |
Otros operadores del molde: The Estate Folder (1341538612387056, US), Joan Pruitt (1343705248835882, US). Nota: la API no desglosa país en consultas multi-país; el GB sale de una consulta por `page_id` + `GB`.

## Actualización 2026-11-21 (4) — conteos limpios por `page_id` + país (ACTIVE, corte 7 d ≈ epoch 1794620000)
| Página | País | Activos | Sobrevivientes (≥ 7 d) | Veredicto |
|---|---|---|---|---|
| My Estate Kit (1091977304009213) | 🇬🇧 GB | 37 (< 50, exacto) | 37 (de jun a 29-oct) | **pasa** (≥ 10), un solo page_id |
| My Estate Kit | 🇺🇸 US · 🇦🇺 AU | 0 · 0 | 0 | solo corre en GB |
| The Estate Kit (1215301468337012) | 🇦🇺 AU | 9 | 9 (todos de ago-sep, 80+ d) | **cerca** (7-9), re-conteo 2026-11-28 |
| The Family Folder (487465484456721) | 🇺🇸 US | 13 | 4 (el resto de 3-4 d) | vigilancia, re-conteo 2026-11-28 |
| Leave It Sorted (1273987602462473) | 🇺🇸 🇬🇧 🇦🇺 (y al menos uno de CA/IE/NZ) | 7 (la misma lista en cada país) | 2 (de ≈ 43 d: «What My Advisor Won't Tell You») | señal; 0 en DE/CH/AT; 5 anuncios nuevos de ≤ 4 d |
| Plainleaf Publishing (1391989857327505) | 🇨🇭 CH | 33 | 0 (todos del 17-18-nov) | recién lanzado; re-conteo 2026-11-28 |
| unterlagio.privat (1452299261289834) · Wichtige Sachen (1564720296718249) | 🇩🇪 🇨🇭 🇦🇹 (sin separar) | 7 (portafolio: Nebenkosten, Steuerbelege) · 1 | 0 | señal; Notfallordner = 1 ad de ≤ 4 d |
| Joan Pruitt (1343705248835882) | 🇺🇸 US | 3 | 0 (6 d) | señal |
Conclusión: el molde está **probado en 🇬🇧 GB (My Estate Kit 37/37)**; AU en «cerca»; US en vigilancia; DE/CH recién lanzados (≤ 4 d) por operadores distintos; RO es la edición de Mente que sana (≥ 11/59). Las consultas multi-país de la API no separan país: el US/GB/AU de Leave It Sorted devolvió la misma lista de 7. Pendiente: GB para The Family Folder y The Estate Kit, IE/NZ/CA sueltos, y landing de My Estate Kit.
