# Log técnico de la nube

| Fecha | Sesión | Qué pasó |
|---|---|---|

- 2026-11-20 18:50 EN tarde: WebFetch no resuelve `quicklyguide.com` desde la nube (host fuera de la red permitida); se leyó la landing con Firecrawl. Push `origin main` falla desde la rama local `main-d1oteb`: usar `git push origin HEAD:main`.

- 2026-11-21 ESTE (sáb 14:12): diacríticos resueltos en RO/PL/CZ/HU: `hărți mentale`, `ściąga pdf`, `notatki pdf`, `myšlenkové mapy`, `okamžitý přístup`, `gondolattérképek` y `azonnali hozzáférés` devuelven resultados con diacríticos; no hizo falta la variante sin tilde. `firecrawl_scrape` abre `ad_snapshot_url` y landings (`maxAge: 0`); con `formats: ["links","query"]` y `queryOptions` el snapshot sale corto (sin la lista de países). Un scrape falló por un id mal escrito mío (sin consecuencias). Sin fallas de conector ni de git.

- 2026-11-22 BR (dom 03:30): sin fallas de conector ni de git. `firecrawl_scrape` abre ad_snapshot_url (maxAge 0, waitFor 4000) y landings; la landing de Metaleitura (VSL) trae casi solo JSON del player. Los lotes 1-4 de Haiku devolvieron la tabla sin repetir; dos keywords (`passo a passo`, `receba no e-mail`) con asignación por orden (baja confianza).
