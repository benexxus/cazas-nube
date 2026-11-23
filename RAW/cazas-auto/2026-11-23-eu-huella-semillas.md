# EU · lunes 2026-11-23 · modo A huella + 20 semillas (corrida desatendida)

Sesión EU (IT FR DE PT AT CH NL BE). Hora Madrid 08:09. Reloj de la API: hoy ≈ epoch 1 795 420 000; corte de 7 días ≈ 1 794 815 000 (se cuenta por `ad_creation_time`; entre paréntesis el reloj de entrega cuando discrepa).

## Embudo
- **Etapa 0 (ronda de operadores EU, las 4 filas de la tabla):** Esprit Académique FR ≥ 50 / 97 (sin cambio, 1 solo título); Axon Academy («Camille Dubois») FR: tanda Black Friday del 19-nov (La Carte de l'Anglais, mismos títulos), sin SKU nuevo; Camille Laurent BE: «150 fiches d'anatomie de la musculation» (conocido) + «Bibliothèque de Biologie Médicale» (conocido) + «histoires bibliques» (religioso, se ignora); Download Studio CH: 50 visibles todos ≤ 6 d, mismos SKUs (gimnasia, patinaje, 6 volúmenes) → sin título nuevo con 10+. Filas actualizadas a 2026-11-23.
- **Etapa 1:** 40 keywords (20 propias del modo A: huellas de CEREBRO §6 en IT/FR/DE/PT/NL; 20 semillas nunca usadas de `semillas.md`: 12 huellas + 8 molde × tema), 4 subagentes Haiku. Lotes 2 y 3 volvieron incompletos (2 de 29 y ~4 de 10 keywords con tabla fiable, país inferido por orden de llamada) → repetidos con Sonnet (lote 2 en dos mitades, 3b). El lote 1 de Haiku tardó 12 min; se relanzó con Sonnet y se detuvo al llegar el de Haiku. PT: 4 huellas del CEREBRO (`para imprimir`, `imprimível`, `apostila`, `planilhas`) estaban usadas el 11-23 por BR → se cambiaron por `fichas estudo`, `modelo pronto`, `checklist completo`, `guia ilustrado`.
- **Etapa 2:** páginas con 10+ activos en las tablas: ~40; descartadas por grep/gate/no-infoproducto las excluidas (recetarios, manualidades, religioso, neurokids-adyacente) y las ya vistas. Pasos rápidos (11): PhysioAtlas CH, Visueller Therapie-Atlas DE, Didactalab BE, Sprachfluss-Karten BE, Equilia CH, Camille Laurent CH, Beatriz Laurent CH, Therapy Toolkit DE, Où jouer la balle FR, Camille Autonomie FR, Idiomas em Mapas PT, Thomas Bernard FR (cortado por «Neuroanatomie»). Completos: PhysioAtlas (DE, CH), Visueller Therapie-Atlas (DE, AT), Didactalab (BE, FR), Sprachfluss-Karten (BE, DE), Equilia (CH, corte «sauraient-ils»). 10 `firecrawl_scrape` (5 snapshots + 5 landings). `ALL` no corrido en ningún candidato (tiempo): pendiente de la PC.

## Páginas verificadas (una fila por país)

| Página (`page_id`) | Oferta | País: cohorte / activos | Veredicto |
|---|---|---|---|
| PhysioAtlas Visuell (`1356253604249122`) | 320 visuelle Landkarten + 6 Boni (PDF, US$ 17, `physioatlas.impultienda.ar`) | 🇩🇪 18 / 40 (16 por entrega) · 🇨🇭 17 / 38 (15 por entrega) · 🇦🇹 no contado | **pasa** · más viejo ≈ 10-nov (13 d) |
| Visueller Therapie-Atlas (`1489239604267149`, antes «Helder Beeld Radiologie») | 120 Emotionale Mindmaps + 32 Metaphern + 12 Therapieansätze (PDF, US$ 19, `therapieatlas.impultienda.ar`) | 🇩🇪 24 / 36 · 🇦🇹 22 / 31 (19 por entrega) · NL/BE/CH: aparece (13 / 10 / ≥ 26 visibles), no contado | **pasa** · más viejo ≈ 11-nov |
| Didactalab = KINEA (`1263109316890203`) | L'atlas d'anatomie du professeur de yoga (PDF A4 + app de regalo, US$ 19,99, `yoga-fr.oqumi.shop`) | 🇧🇪 21 / 23 (19 por entrega) · 🇫🇷 21 / 24 (19 por entrega) | **pasa** · más viejo ≈ 6-nov (17 d) |
| Sprachfluss-Karten (`1173721545831519`) = `*.fluentmaps.com` | «Sprich sie. Nicht nur büffeln» · 500+ Mindmaps de idiomas (€ 17, Hotmart; landing abierta = `spanisch.fluentmaps.com`; existen subdominios `italienisch/franzoesisch/arabisch/englisch`) | 🇧🇪 35 / 35 · 🇩🇪 ≥ 49 / 50 (piso; 90 est.) · NL, AT, CH no contados | **pasa** (⚠️ cohorte contada por página, no por idioma) · más viejo ≈ 30-sep (54 d) |
| Equilia (`1372790255922822`) + Equilia Swiss (`1302396209634757`, 13 ads DE/CH) | Le Classeur Si Demain (PDF a imprimir, CHF 34,90; upsell pack CHF 99,90; Shopify `equilia.ch`) | 🇨🇭 ≥ 15 / 50 en el corte «sauraient-ils» (111 est.; piso) | **pasa** con salvedad A (ver tarjeta) · más viejo ≈ 11-nov |
| Camille Laurent #2 (`105398399244253`) | Atlas visuel de l'évaluation orthopédique | 🇨🇭 0 / 16 (todo del 22-nov) | señal, re-conteo 11-30 |
| Beatriz Laurent (`1237914569412320`) | 120 fiches impression 3D | 🇨🇭 0 / 22 (todo ≤ 6 d) | señal |
| Où jouer la balle (`1412588681932114`) | pickleball | 🇫🇷 0 / 18 | señal |
| Camille – Autonomie au quotidien (`1437006726155191`) | guide illustré 239 p. 17 € | 🇫🇷 0 / 11 | señal |
| Thomas Bernard (`1257844197417780`) | 160+ Neuroanatomie / 310 Informatique | 🇫🇷 0 / 31 (Neuroanatomie, todo ≤ 5 d) | señal, re-conteo 11-30 |
| Idiomas em Mapas (`1466836846510822`) | Inglês visual | 🇵🇹 3 / 22 | [<4] |
| Therapy Toolkit (`102506312071455`) | kits de terapia infantil / teen / «21 Mental Reprogramming» multi-SKU, 176 est. DE | no verificada (portafolio, 6+ visibles de 18-oct; roza neurokids) | no tarjeta |

## Gate (landings abiertas con Firecrawl)
- PhysioAtlas: PDF alemán, sin persona, sin About, checkout propio Impultienda, garantía 14 d. Filtros A/B/C/D ✅.
- Visueller Therapie-Atlas: PDF, sin persona (autores citados solo como bibliografía), garantía 7 d, 3 títulos de anuncio → una sola landing (un solo SKU). ✅. Familia hermana (mismo molde, otras páginas): Therapeutische Mindmaps `1368548086349696`, PsiOS `111707335304926`, Valentina Gomez `111306911997481`.
- Didactalab/KINEA: PDF A4 imprimible + «application» de regalo (Filtro D: la app es bono, el entregable es PDF), sin persona, «KINEA» como marca, garantía 30 d. ✅ con nota.
- Sprachfluss-Karten: Hotmart, sin persona, sin pie. ✅. Mismo molde que «Spanisch Illustriert» (`1387308257802291`, 4 ads) y Lingua Chiara (ficha del cerebro).
- Equilia: PDF a imprimir enviado por e-mail, TWINT/tarjeta/factura, tienda Shopify multi-SKU (≈ 40 productos, entre ellos recetarios, que no cuentan). Texto en primera persona «J'ai créé ce classeur… Fait par une Suisse», «relu par Julie»: persona anónima sin cara ni apellido → **Filtro A parcial**, a confirmar en la PC.

## Dónde ya se probó y falló / contexto
- Camille Dubois (Axon Academy) y Esprit Académique sin cambios. Kennis Formule NL, Marco Bellini IT: no revisados hoy.
- Ceros con `ALL` (ya probados por subagentes): `samenvatting pdf` BE (42 ads con ALL, 0 activos), `erfenis checklist` NL (36 con ALL, 0 activos), `eserciziario pdf` CH (0 también con ALL).

## Cobertura
40 keywords × países de su idioma: IT/CH ×8 (da stampare, stampabile, modelli, schede, eserciziario pdf, modelli pronti, accesso a vita, kit eredità) · FR/BE/CH ×9 (à imprimer, imprimable, fiches, classeur, guide illustré, modèles prêts, accès à vie, kit succession, atlas anatomie) · DE/AT/CH ×9 (zum Ausfüllen, druckfertig, Arbeitsblätter, Komplettset, excel vorlage, checkliste pdf, ratgeber pdf, Erbschaft Checkliste, mindmaps pdf) · PT ×6 (kit herança, manual ilustrado, fichas estudo, modelo pronto, checklist completo, guia ilustrado) · NL/BE ×8 (visuele gids, mindmaps ×2 listas, printables, werkboek pdf, samenvatting pdf, oefenvragen pdf, erfenis checklist). Países sin una sola página que pase: 🇮🇹 (nada nuevo con cohorte; Biblioteca Práctica IT 15 y Edizioni Favilla 20 son de ≤ 2 d; los patrones de punto/ganchillo son manualidades, ignorados), 🇵🇹 (solo 3 / 22), 🇳🇱 (la oferta que corre en NL/BE es la alemana de Sprachfluss/Atlas, sin landing neerlandesa).

## Molde en otros países
Atlas visual de terapeutas: DE, AT, NL, BE, CH. Atlas anatomía de movimiento: FR, BE, CH (Didactalab, Pilates Atlas, PhysioAtlas CH 🇨🇭 31 ads en una keyword). Idiomas en mapas: DE, BE, NL, FR (Axon), IT (Lingua Chiara).

## Falla técnica
Ver `cazas/nube/log-nube.md`.
