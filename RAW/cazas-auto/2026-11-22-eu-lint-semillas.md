# EU 2026-11-22 (dom) — lint de la cola + embudo con semillas

Sesión EU, una sola corrida por día. Domingo: lint de la cola de EU + embudo de dos etapas con 40 semillas de `semillas.md` (ninguna usada antes por EU; las huellas PT se eligieron entre las que BR no usó en los últimos 7 días).

## Resultado

**2 tarjetas:** Esprit Académique (`1229441186928180`, «210 Fiches Visuelles sur les Troubles Mentaux», FR/BE/CH) y Camille Dubois (`1077014278820945`, «La Carte de l'Anglais», FR/BE). Tercera que pasa la vara y queda como señal por el tope de 2: Camille Laurent (`1407481519105013`, «La Bibliothèque de Biologie Médicale», BE).

## Lint de la cola (EU)

- Ningún nodo EU lleva > 30 días sin tocar (el repo tiene 3 días). Ningún 🟡 vencido de EU.
- Re-conteos con fecha: Griffbereit (cerca el 11-21, re-conteo ~11-28) y Pharmacologie/«fichas visuales» CO (11-27) todavía no vencen. Nada que re-medir hoy.
- Altas a la cola: `salud-mental-visual` ya existe (ESTE); se agrega el tramo EU como nodo `virgen` nuevo (`salud/fichas-visuales-psicologia-medicina`), y `salud/biologia-medica-visual`.

## Embudo

**Etapa 1:** 40 keywords × 4 subagentes Haiku (10 c/u), solo en los países de su idioma (IT→IT,CH · FR→FR,BE,CH · DE→DE,AT,CH · PT→PT · NL→NL,BE). Ningún subagente falló; todos devolvieron la tabla. Cero activo con `ALL`: «checklist trasloco» CH, «addestramento cuccioli» CH.

| Idioma | Huellas | Molde × tema |
|---|---|---|
| IT | download immediato · pdf scaricabile · guida pratica · mappe concettuali · schemi riassuntivi | checklist trasloco · addestramento cuccioli · quiz patente |
| FR | téléchargement immédiat · pdf à télécharger · fiches de révision · cartes mentales · cahier d'exercices | check-list déménagement · dressage chiot · fiches permis |
| DE | sofort download · lernkarten pdf · vorlagen paket · arbeitsbuch pdf · zusammenfassung pdf | Umzug Checkliste · Welpentraining · Haushaltsbuch Vorlage |
| PT | acesso vitalício · receba no e-mail · 9,90 € · numa página · templates canva | carta de condução · exame código · ração natural cães |
| NL | direct downloaden · praktische gids · werkbladen pdf · kant-en-klare sjablonen · stappenplan pdf | verhuizing checklist · puppytraining · huishoudboekje |

(Son 40 en total: 25 huellas + 15 molde × tema; 5 idiomas × 8.) «Welpentraining» y «Haushaltsbuch Vorlage» sin la palabra de formato.

**Salió:** ~600 filas (páginas por keyword × país). Ruido grande: apps, servicios, físicos, cursos en video, religioso y recetarios (ignorados sin anotar como señal). Muchos operadores de infoproducto visual nuevos; ~35 `page_id` que nunca habían aparecido en `cazas/` ni `RAW/`.

**Etapa 2 — 10 páginas verificadas** (paso rápido: `page_ids` + país con más ads; `ACTIVE`, limit 50; cohorte = creados hace 7+ días; reloj de creación y de entrega).

| # | Página | Paso rápido | Resultado |
|---|---|---|---|
| 1 | Esprit Académique `1229441186928180` | CH, luego FR y BE | **≥ 50 / 59 CH · ≥ 50 / 97 FR · ≥ 50 / 85 BE** (tope 50 lleno, todos ≥ 7 d; piso) → **pasa**, paso completo |
| 2 | Camille Dubois `1077014278820945` | FR, luego BE | **≥ 14 / 50+ FR (270 est.) · ≥ 24 / 50+ BE (241 est.)** → **pasa**, paso completo |
| 3 | Camille Laurent `1407481519105013` | BE | «Biblioteca de Biología Médica» **≥ 18 / 50+ (73 est.)** → pasa (señal por tope 2) |
| 4 | Céline Moreau `1367953336410558` | FR | 3-5 / 27 («+300 cartes mentales», 2 de ellos con entrega < 7 d) → vigilancia |
| 5 | Download Studio `1344017652136102` | CH | 50 visibles / 118 est., el más viejo visible 16-17 nov → **cohorte indeterminada** |
| 6 | Bibliodor `1342066738997872` | BE | 0 / 25 (todo del 21-nov) |
| 7 | Table File `1465448983314663` | BE | 0 / 23 (todo del 21-nov) |
| 8 | Dra Laura Martin `1274719509066382` | DE | 5 / 5 («250 Lernkarten Pflegehilfe», 1-nov y 9-12 nov) → vigilancia |
| 9 | Sofía Herrera `1205419289331646` | DE | 6 / 6 («250 visuelle Lernkarten Kita-Wissen», 3 fechas) → vigilancia |
| 10 | Mesa Ligera `1219245414615500` | FR | 0 / 7 (todo del 21-nov) |

Páginas con paso rápido no hecho por no entrar en las 10 (solo tabla): Marco Bellini IT (8 ads, 21-nov), Miguel Ferreira PT (9, 21-nov), Cursos de Terapias Naturais PT (22, 20-nov, curso), Mundo Digital PT/CH (≈10, 20-nov), Kennis Formule NL (16, 19-nov, 200 piezas de piano en PDF), Gymspiratie BE (19, 20-nov), Klar & Fertig DE (Wichtel, 22-nov), Griffbereit/Studio Facile (ya cazados).

### Esprit Académique — detalle (filas por país)

| País | Apareció en tablas | Conteo `cohorte / activos` |
|---|---|---|
| CH | sí (fiches de révision, ≈14 en la tabla) | ≥ 50 / 59 (50 devueltos, el más reciente 6-nov) |
| FR | no (solo en CH/BE de la tabla; la medí igual) | ≥ 50 / 97 |
| BE | sí (fiches de révision, 5 ads en la tabla) | ≥ 50 / 85 |
| DE · AT · IT · PT · NL | no apareció | — (no medido: no es de su idioma) |

- Oferta única: «210 Fiches Visuelles sur les Troubles Mentaux» (+5 bonus), 9,99 €. Un solo creativo («🧠 210 Fiches Visuelles sur les Troubles Mentaux ! 📚») repetido ≥ 50 veces, 5 fechas de creación (9-oct, 12-13 oct, 26-oct, 1-nov, 6-nov); el más viejo ≈ 44 d (creación 9-oct) → ① a 1 día de los 45.
- Moneda de los ads: BRL (el anunciante factura en reales).
- Snapshot (Firecrawl, `maxAge: 0`, ad 1954173409023519): copy completo; CTA a `https://visuelles.lovable.app/`. Landing: página Lovable de una sola pieza; 210 fiches, 5 bonus, «9,99 € paiement unique», checkout `pay.hotmart.com/X107945722F`, garantía 7 días, pie «© 2026 — 210 Troubles Mentaux», CGV/mentions légales. **Sin persona, sin nombre propio, sin redes.** FAQ colapsada: no se ve si el material es PDF o app (dice «support 100 % numérique» y «espace numérique»).
- Marca personal: no. A-bis: no. Filtro D: entregable PDF/fichas (a confirmar el formato exacto en la PC). Back-end: la landing solo vende el kit (6 productos en un acceso).
- ALL no corrido (tope de tiempo; todas las ofertas visibles son la misma).
- Molde en otros mercados (señales): Mesa Ligera FR/PL/RO «Psychiatrie en fiches F00-F98» 0 / 7 FR (ya en bandeja ESTE 0 / ≈49); Psyacademy `944317715424068` «210 fiches visuelles de psychopathologie» BE 3 ads (15-nov), CO 0 / 7 (11-20); Mundo Digital `1438697565993676` «210 Perturbações Mentais · Guia Visual» 9,99 € PT ≈ 3 / CH ≈ 10, todo ≤ 3 d; Discover You CH 1.

### Camille Dubois — detalle

- Oferta: «La Carte de l'Anglais™» — 520 cartes mentales A1→C2 en 6 parcours + 6 bonus, 12,90 € (de 175 €), «jusqu'au 30 novembre» (Black Friday), 100 % PDF, garantía 30 días. Landing `https://academyaxon.com/cartedelanglais/` (WordPress/Elementor, «Axon Digital»), checkout `pay.hotmart.com/X107204956Y`. Sin persona; testimonios como capturas; «+4 127 apprenants».
- FR: 50 devueltos / 270 est.; 14 con creación ≤ 14-nov (13-nov): «520 cartes mentales en PDF», «12,90 € · paiement unique», «La plus facile pour un francophone»… (reloj de entrega también ≤ 14-nov). BE: 50 / 241 est.; 24 con creación 13-nov. CH: apareció en la tabla (≈ 12 ads, el más viejo 13-nov), cohorte no contada. Todo es piso (tope 50).
- Snapshot: ad 1988106355928314 «Started running Oct 19, 2026» (34 d) y 1842736406723988 (27-oct). Hermana: `academyaxon.com/carteespagnol` («La Carte de l'Espagnol», ads «Ser ou estar ?»).
- ③ duplicación: el creativo más repetido entre los sobrevivientes es «520 cartes mentales en PDF» ×4 → no llega a 10. Score ≤ 2/4 (② no llega a 50; ① 34 d).
- Page name «Camille Dubois» sin cara en los creativos; nombre probablemente de fachada: verificar en la PC que no haya persona real.

### Camille Laurent — detalle (señal)

- BE: 50 devueltos / 73 est. «La Bibliothèque de Biologie Médicale» ≥ 18 con creación 31-oct (una sola tanda), el más viejo 22 d. Los «150 fiches d'anatomie de la musculation» (≈ 21 ads, creación 13-14 nov) cuentan 0 por reloj de entrega (15-16 nov, < 7 d). Mezcla ofertas excluidas (religioso: «Et maintenant, que ferait Jésus ?», «Plus de 1 000 histoires bibliques», ignoradas).
- Landing `clinical-laboratory-library.online/fr/` (noindex): 9 € Essentielle / 17 € Complète (tachado 147 €), checkout `pay.snappcheckout.com`, «Élise Varenne» con foto en «À propos» (+ testimonios fechados en enero/febrero 2026, anteriores al dominio) → **posible marca personal / testimonios fabricados**: el gate lo pone en duda. Contenido: «PDF y una app de estudio». No va a tarjeta; se anota como señal con la duda de A.

## Otras señales de la Etapa 1 (sin verificar)

- «Fiches» FR: Pharmacologie Limpide `1384090748119855` (1 ad, 22-nov), Pharmacologie Simplifiée `1391162887408497` (BE 2, CH 2, 17-nov), Patricia Gutierres `1242614235604703` «Fiches Visuelles Aide-Soignant 250+» (1 ad, 21-nov); Fernanda Ribeiro / Claire Morel BE (1 ad, 17-nov).
- DE: Einfacheslernen `1402023712984001`, PhysioAtlas Visuell `1356253604249122` (320 visuelle Landkarten), The Visual Library `1416105361579932` (5 ads, 20-nov), Geldverdienen24 `1458291137361906` «Haushaltsbuch 2027 (Excel)» (2 ads, 8-nov): todo < 4 ads o ≤ 2 d.
- NL: Edu Digital `100629922105479` 6 PDF-boeken, Kennis Formule (16 ads, 19-nov), Spelend Rekenen, 90 CGT-werkbladen: chicos y nuevos.
- Altas a la cola con la regla de §0.4 (10+ activos de un tema que no está en la cola): Esprit Académique/Mundo Digital (psicología/medicina visual), Camille Laurent (biología médica visual). Ningún otro tema con 10+ nuevo y no excluido.

## Cobertura

- 40 semillas barridas, ~600 filas, 10 páginas con paso rápido (12 consultas por `page_ids`: 5 + 5 del paso rápido, más FR/BE de Esprit y BE de Dubois), 3 con paso completo parcial, 6 `firecrawl_scrape` (3 snapshots + 3 landings), 0 búsquedas `ALL` por tiempo (solo las 2 de cero en la Etapa 1).
- Límites: paso completo de Camille Dubois en CH y de Camille Laurent en FR/CH sin contar; `ALL` sobre los tres candidatos no corrido. Todas las cohortes son piso (tope 50).
