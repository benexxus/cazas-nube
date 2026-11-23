# Log técnico de la nube

| Fecha | Sesión | Qué pasó |
|---|---|---|

- 2026-11-20 18:50 EN tarde: WebFetch no resuelve `quicklyguide.com` desde la nube (host fuera de la red permitida); se leyó la landing con Firecrawl. Push `origin main` falla desde la rama local `main-d1oteb`: usar `git push origin HEAD:main`.

- 2026-11-21 ESTE (sáb 14:12): diacríticos resueltos en RO/PL/CZ/HU: `hărți mentale`, `ściąga pdf`, `notatki pdf`, `myšlenkové mapy`, `okamžitý přístup`, `gondolattérképek` y `azonnali hozzáférés` devuelven resultados con diacríticos; no hizo falta la variante sin tilde. `firecrawl_scrape` abre `ad_snapshot_url` y landings (`maxAge: 0`); con `formats: ["links","query"]` y `queryOptions` el snapshot sale corto (sin la lista de países). Un scrape falló por un id mal escrito mío (sin consecuencias). Sin fallas de conector ni de git.

- 2026-11-22 BR (dom 03:30): sin fallas de conector ni de git. `firecrawl_scrape` abre ad_snapshot_url (maxAge 0, waitFor 4000) y landings; la landing de Metaleitura (VSL) trae casi solo JSON del player. Los lotes 1-4 de Haiku devolvieron la tabla sin repetir; dos keywords (`passo a passo`, `receba no e-mail`) con asignación por orden (baja confianza).

- 2026-11-22 BR (2ª corrida del mismo día, dom ~03:36): la rutina BR se disparó dos veces y la primera ya había empujado el informe y la bandeja con las mismas 40 semillas; esta corrida solo aportó Aprovados Enem 2026 (9/9, posible zombi) y Ana Julia (8/31 portafolio, ya señalada). Sin fallas de conector ni de git.

- 2026-11-22 ES (dom 04:04): lint + semillas sin fallas de conector. Aviso técnico: los 4 subagentes Haiku reportaron que la atribución país/keyword de algunos bloques sale del orden de las llamadas (la respuesta no repite el input) y que el buscador no respeta símbolos de precio (`S/ 29.90`, `9,90 €`); las páginas verificadas se contaron por `page_ids` + país. `page_id` de Inglés en Mapas y Digital Guides (tomados de las tablas) devolvieron 0 con ACTIVE.
- 2026-11-23 EN: los lotes 1-3 de Haiku devolvieron tablas parciales (el país se infirió por orden); el lote 3 solo tabuló 2 de 10 keywords y se repitió con Sonnet (completo). Corrida de ~2 h, la mayor parte esperando subagentes.
- 2026-11-23 ES (lun 04:05): los lotes 2 y 4 de Haiku volvieron incompletos (tablas parciales, país inferido por orden de llamada; el lote 2 tabuló 4 de 10 keywords, el lote 4 5 de 10) y se repitieron con Sonnet (completos). Lotes 1 y 3 de Haiku útiles pero con conteos a mano ±1-2. Respuestas de `ads_library_search` muy largas (50 ads) y el scrape de snapshot de Mente Académica pasó los 70 k caracteres (se leyó con jq). Corrida de ~1 h 50 min, la mayor parte esperando subagentes.
