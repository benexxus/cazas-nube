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
