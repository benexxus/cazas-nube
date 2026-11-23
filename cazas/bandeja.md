# Bandeja — los ganadores del día, en tarjetas

Salida del programa de caza ([[automatizar-la-caza-de-winners]]). **Cada sesión deja acá una tarjeta por
cada página que pasa la vara** (sin tope desde el 2026-11-22; una línea por oferta si la página tiene varias). Diez líneas cada una, nada más. La evidencia
completa (keywords, conteos, descartes) queda en `RAW/cazas-auto/` y **no se le muestra a Carlos**
salvo que la pida.

> **Regla:** «pocos infoproductos ganadores por día y por mercado, por qué es ganador, qué se puede hacer
> con él, y el link de su biblioteca de anuncios. Nada de informes largos.» Si un día no sale ninguno que
> cumpla la vara, se escribe **una línea** («XX <fecha>: nada que pase la vara; se barrió X, Y, Z») —
> **nunca se rellena el podio**.

**Vara para tener tarjeta:** pasa el gate (no marca personal + embudo verificado o WhatsApp con la oferta
en el copy) **y** además la vara de `cazas/nube/CEREBRO.md` §1 — **10+ sobrevivientes** (desde el 2026-11-20), contados por oferta y por país, igual en todos los mercados; no se piden tandas. No se suman fanpages hermanas ni se compensa el volumen con la
longevidad de un ad suelto. **Cerca** (7-9) y **vigilancia** (4-6) van como línea de *señal* con fecha de
re-conteo, no como tarjeta. Se reporta el veredicto: «pasa», «cerca», «vigilancia».

**Cómo se revisa:** Claude muestra las tarjetas en el chat y **Carlos decide con palabras** — `Idea`
(se crea la ficha del producto) · `tirar` (a `descartados.md` con su motivo) · `re-cazar <fecha>` ·
`profundizar` (vuelve a [[cola]]). Nadie edita este archivo a mano. Las tarjetas decididas bajan al
histórico.

---

## Pendientes de revisión

### 🔎 Para re-contar en la PC
Lo que la API no puede cerrar: tope de 50 tras 3 cortes con piso < 10, alerta de relanzamiento o landing que
Firecrawl no abrió. **El re-conteo de la PC hace solo esta lista y las tarjetas nuevas** (script
`reconteo-library.js` de la skill `cazar`), no el día entero.
<!-- RECONTAR: cada sesión agrega acá una línea por página: fecha · sesión · página · page_id · países · motivo · search_terms usados · links por país -->

### 🔎 Correcciones del informe Opus 2026-11-22 (Library web, a pedido de Carlos)
Re-conteo de las 6 tarjetas y de las señales del día en la Library web ordenada por impresiones, con las versiones agrupadas contadas. Informe completo en el cerebro (`RAW/cazas/2026-11-22-cazas-nube-informe.md`). Tarjetas nuevas que salen de ahí (corregidas el mismo día: los conteos de la web con versiones agrupadas inflaban; donde la página tiene < 50 manda la API):

### 🎯 Pautas Listas para Urgencias (guía PDF de 288 págs + app de bono, 19,99 €) 🇪🇸 ES · `salud/urgencias-guias` · 2026-11-22 · corrección Opus
- **Qué es:** guía digital de urgencias ordenada por motivo de consulta (Método 3P, genérico y marca española) + 5 bonos; la app en el móvil es un bono, el producto es el PDF. 19,99 € (tachado 98 €), Impultienda.
- **Por qué es ganador:** **≥ 29 sobrevivientes** en 🇪🇸 (piso: tarjetas de la web sin contar versiones; 52 contándolas), ~130 activos, más viejo 25-oct (28 d), 16 fechas de creación. Por API no se puede: con «Pautas Listas» sigue en 50, todo del 19-21 nov. **La sesión ES lo había tirado por «app» (Filtro D): mal descartado.**
- **Ads Library:** [🇪🇸](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ES&view_all_page_id=1358096157393957&search_type=page&media_type=all) · **Landing:** [urgencias.ebookky.com](https://urgencias.ebookky.com/)
- Gate: A sin persona (solo testimonios con inicial) · B ✅ · D ✅ PDF · Score 0-1/4 (② sin confirmar) · Decisión: —

### 🎯 Farmácia Mapeada en español — 4 ofertas que pasan (PDF US$ 13-15, Hotmart) — Estudia Sencillo 🇨🇴🇲🇽 · `salud-farmacologia-mapas` · 2026-11-22 · corrección Opus
- **Qué es:** guías PDF ilustradas para estudiantes y profesionales de salud: Urgencias y Emergencias para Enfermería (US$ 13), Kit Farmacología Ilustrada (US$ 13), GLP-1 en Consulta (guía de 149 págs, US$ 15), Bioquímica Ilustrada (US$ 13). Operador brasileño (`es.farmaciamapeada.com.br`, CNPJ 47.918.823/0001-64).
- **Por qué es ganador (por oferta):** Urgencias 🇨🇴 33 / 33 · 🇲🇽 32 / 33 · Farmacología 🇨🇴 31 / 38 · 🇲🇽 33 / 41 (más viejo 24-jul) · GLP-1 🇨🇴 42 / 50 · 🇲🇽 44 / 54 · Bioquímica 🇲🇽 12 / 12 · 🇨🇴 9 / 9. La sesión ES lo dejó «cohorte indeterminada».
- **Ads Library:** [🇨🇴](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=CO&view_all_page_id=113453315134646&search_type=page&media_type=all) · [🇲🇽](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&view_all_page_id=113453315134646&search_type=page&media_type=all) · **Landings:** [Urgencias](https://es.farmaciamapeada.com.br/urgencias-enfermeria/) · [Farmacología](https://es.farmaciamapeada.com.br/farmacologia-v2/) · [GLP-1](https://es.farmaciamapeada.com.br/glp1/) · [Bioquímica](https://es.farmaciamapeada.com.br/bioquimica/)
- Gate: A ✅ con salvedad (en Brasil la marca tiene ~300 k seguidores en una cuenta de marca; el fundador Moisés Santos es marketero, 1,5 k) · D ✅ PDF · Score 1/4 (① 45+ d en Farmacología; ninguna oferta llega a 50 en un país) · Decisión: —

### 🎯 La Bibliothèque de Biologie Médicale (PDF + app, 9 € / 17 € + upsell 8 €) — Camille Laurent 🇧🇪 BE · `salud/biologia-medica-visual` · 2026-11-22 · corrección Opus
- **Por qué:** **22 / 22** en 🇧🇪, una sola tanda del 31-oct (22 d). Misma página corre ofertas religiosas (excluidas) y «150 fiches d'anatomie» 13 / 22 todo del 15-16 nov (al borde de los 7 d, re-conteo 2026-11-25).
- **Ads Library:** [🇧🇪](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BE&view_all_page_id=1407481519105013&search_type=page&media_type=all) · **Landing:** [clinical-laboratory-library.online](https://clinical-laboratory-library.online/fr/) (snappcheckout)
- Gate: **A por verificar** («Élise Varenne» con foto, sin redes ni fechas) · Decisión: —

**Señales corregidas por Opus (22-nov):** Céline Moreau 🇫🇷 «Anglais Visuel» **5 / 26 por API → vigilancia** (la web daba 10 contando versiones agrupadas con la fecha del anuncio que las agrupa: infla; Sonnet tenía razón), [landing](https://anglaisvisuel.site/), US$ 17, re-conteo 2026-11-29 · Dra Laura Martin 🇩🇪 **5 / 8 por API → vigilancia** (mismo error de versiones), [landing](https://pflegehilfe.map-visio.com/), PDF 9,95 / 14,95 € · Sofía Herrera 🇩🇪 6 / 12 (vigilancia, [landing](https://kita.map-visio.com/), mismo operador `map-visio.com`) · Download Studio 🇨🇭 portafolio, máx. 9 por landing (gimnasia FR 9 / 19, prépa physique 9 / 22): cerca · Fer Rendon 🇲🇽 0 / 160, todo lote nuevo · Facilitaê 🇧🇷 «Guia Reforma» 6 / 18 vigilancia · Aprovados Enem 🇧🇷 0 en la web = zombi confirmado.


<!-- TARJETAS-EN: la sesión EN inserta sus tarjetas del día justo debajo de esta línea -->

EN 2026-11-23 (lun, modo A huella + 40 semillas): nada que pase la vara; se barrió print-ready, instant pdf, worksheets, fillable, no-prep, done-for-you, binder, answer key, pdf bundle, digital planner, study notes, revision notes, exam prep, practice questions, lesson plans, flashcards pdf, visual cards, reference sheets, checklist template, printable bundle, printable pdf, cheat sheet, study guide, mind maps, checklist pdf, visual guide, explained visually, in pictures, on one page, lifetime access, cdl study guide, carpentry cheat sheet, aws cheat sheet, excel cheat sheet, houseplant care guide, car maintenance checklist, phone photography guide, lawn care schedule, home energy savings checklist, cat care guide (US GB CA AU).

**Señales del día EN (23-nov)**
- My Nurse Notes (`107734932379817`, 🇺🇸🇨🇦🇦🇺): «NCLEX Review Cheat sheet 400 pages» ≥ 26 sobrevivientes / 58 activos en US (piso: 50 visibles de 58), 16-18 activos en CA y AU. Landing abierta con Firecrawl (`shop.mynursenotes.com/products/handwritten-nurse-notes-offer`): libro **impreso espiralado** US$ 99,99 («Physical Book», envío gratis, también en Amazon) y descarga digital US$ 69,99; marca en primera persona de una enfermera («My Story»). Falla Filtro D (físico) y el ticket no es bajo. Sin tarjeta.
- Go CDL Pro (`1066314876557111`, 🇺🇸): ≥ 30 sobrevivientes / 61 activos (50 visibles), tandas de ago-oct. Snapshot y `gocdlpro.com` abiertos: **tarjetas físicas** («Physical cards you keep», envío gratis) + 5 guías PDF de bono, tienda Shopify sin persona nombrada. Falla Filtro D (el mecanismo es el objeto). Sin tarjeta.
- Acordes en Claro (`1205940002609789`, 🇺🇸🇬🇧🇨🇦🇦🇺): guitarra, PDF «226 pages, 92 exercises with answers», 215 activos en US, pero los 50 visibles son todos del 22-nov; corte `search_terms: "guitar theory"` = 11 (solo 2 anteriores, de oct, de otra oferta). ⚠️ tanda masiva nueva / posible relanzamiento, <4 sobrevivientes hoy. Landing no abierta (no llegó a 4). Re-conteo 2026-11-30 con el mismo corte.
- Packs pro (`832557806611141`, 🇬🇧 20 / 51; también US CA AU) «5 Modules + 4 Bonuses | Visual Manual», un manual por industria (textiles, químicos, alimentos, cosméticos, pinturas…): **4-5 sobrevivientes por industria** → vigilancia (portafolio, no una oferta de 10+). Zonaebook.pro (`858351214021820`, 🇦🇺 63 activos) «<tema> Student Visual Atlas» / «200 drills + lesson plans»: 5-6 por tema (natación, karate, enfermería, contabilidad, mecánica) → vigilancia. Smart Digital (`1383014634885117`, 🇬🇧 65 activos) «<tema> Professional Edition — 6 Volumes + 5 Bonuses»: 3-4 por tema, corte `Visually Volumes Bonuses` = 14. Los tres, mismo molde multi-tema; re-conteo 2026-11-30.
- Visual Guide Lab (ronda de operadores, `1467890346400480`): SKUs nuevos de 1-2 días, 194 activos en US: lanchas y fuera de borda, bicicletas, notaría y corretaje inmobiliario, tratamiento de agua, pesca, bordado (títulos «Iron nail, wet sand…», «Needle first, then rethread»). 0 sobrevivientes todavía; re-conteo 2026-11-30. Ultimate Budget Planner (`485276957995076`): 28 activos en US, sin ofertas nuevas.
- Sin cohorte (todo de 1-2 días o < 4): Daniel Mercer «1,000 novel studies» (0 / 12), The Toolbox Talk Kit (0 / 3), Cirkit Maker GB (0 / 35, tanda del 17-nov = 5-6 d), DigitalCenter.pro «Biology Student Visual Atlas», SkillForge, Precise Prep, Tilouni, Pawzuma. Marca personal o excluidos, ignorados: Tyler Tometich (VFX), Jennifer Mitchell PhD, Quest, Sajada, Hindu Wisdom, Icancrochet.
- Sin conteo (no verificadas por tiempo): Nursing Cheat Sheets (`1506295449223124`), Kinesiology Deck (`1254414497764436`), Jessica Taylor «138 Visual Skincare Reference Sheets» (`1394431100426775`), The Visual Library (`1416105361579932`), Pack de Plantillas (`108486535276295`), Easymaptax (`1161672967038413`), learndigital.shop (`1053888401135256`): candidatas a paso rápido mañana.

### 🎯 Planillas de finanzas personales en Excel + Google Sheets (US$ 9, dos ofertas) — Ultimate Budget Planner 🇺🇸 US · `finanzas-personales/planillas` · 2026-11-22 · sesión EN
- **Qué es:** dos planillas de pago único **US$ 9** (tachado US$ 297), entrega por email, Excel + Google Sheets: (1) «Ultimate Budget Planner», 28 pestañas (transacciones, 12 meses, calendario de pagos, vista por sueldo, 50/30/20, deudas, patrimonio) + PDF de instalación + tutorial en YouTube; (2) «Debt Snowball Avalanche», hasta 40 deudas, bola de nieve vs avalancha, calendario de pagos y fecha libre de deudas. Dos dominios `*.site` bajo la misma página.
- **Por qué es ganador:** **pasa la vara en 🇺🇸 🇨🇦 🇦🇺 y 🇬🇧** (un `page_id`, `ACTIVE`, tope 50 no alcanzado): oferta «Debt Snowball Avalanche» **13 / 13** (US CA AU; GB 11 / 11), la más vieja del 12-sep (**70 d**, 13 ads en ≥ 3 tandas de la misma tarde); oferta «Ultimate Budget Planner» **11 / 15** (US CA AU; GB 11 / 13), tandas del 4 y 7-oct (46-49 d) + 4 ads de 17-21 nov. Página fantasma (sin cara), operada por «Cosmo Suite Limited, UK». Salvedades: copy de ads muy variados (pocas copias de un mismo creativo), 113 ads en `ALL` en US contra 28 activos = mucho churn; mercado de planillas de deuda/presupuesto con decenas de competidores de 1-3 ads (ninguno cerca de 10).
- **Qué hacer:** modelar la planilla de deuda (nicho más angosto, 13 / 13) y/o el planner de presupuesto en Excel + Sheets, **US$ 9-17** pago único, tutorial en video como bono · destino: 🇺🇸 🇬🇧 (ya vivo, ticket alto) o llevarla a 🇧🇷 🇪🇸 🇩🇪 🇫🇷 🇮🇹 (planilla de deudas/«planilha de controle» en idioma nativo) · ángulo: «ordená qué deuda pagar primero» + «fecha libre de deudas».
- **Ads Library:** 🇺🇸 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&view_all_page_id=485276957995076&search_type=page&media_type=all · 🇬🇧 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=GB&view_all_page_id=485276957995076&search_type=page&media_type=all · 🇨🇦 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=CA&view_all_page_id=485276957995076&search_type=page&media_type=all · 🇦🇺 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=AU&view_all_page_id=485276957995076&search_type=page&media_type=all
- **Landing:** https://www.debtpayoffplanner.site/ (US$ 9, venta directa) · https://www.ultimatebudgetplanner.site/ (US$ 9, venta directa)
- Score 1/4 (longevidad 70 d ✓; volumen 13-15 < 50; duplicación baja; arbitraje sin medir) · Decisión: —
- Evidencia: API; snapshot (no abierto) y landings verificadas vía Firecrawl (no WebFetch); checkout no recorrido, upsells no vistos; longevidad por API, snapshot no verificado desde la nube.
- **Re-conteo Opus 22-nov (Library web, por impresiones):** confirmado sin zombis — Debt Snowball 🇺🇸 13 / 13 · 🇬🇧 11 / 11; Budget Planner 🇺🇸 11 / 15 · 🇬🇧 11 / 13. Checkout propio recorrido hasta el precio (`/checkout/`, US$ 9, sin bump). Gate 5/5 · score 1/4 (① 71 d). ✅ pasa.

EN 2026-11-22 (dom, lint de la cola + 40 semillas): una tarjeta (arriba); se barrió instant access, emailed instantly, gumroad, etsy digital, video course, 30-day plan, printable journal, only $7, only $9, just $17, $27 today, £9 today, £17 only, plumbing cheat sheet, welding cheat sheet, pharmacy technician study guide, phlebotomy study guide, insurance license exam, part 107 study guide, roofing estimate template, esthetician templates, newborn schedule, pregnancy checklist, breastfeeding checklist, debt payoff planner, freelance invoice template, linkedin profile templates, interview questions answers, guitar chords chart, fishing knots, camping checklist, yoga sequences, aquarium cycling guide, dog grooming guide, funeral planning checklist, layoff severance guide, first apartment checklist, college dorm checklist, car accident checklist e identity theft recovery (US GB CA AU).

**Señales del día EN (22-nov)**
- Quinn Morrissette Studio (`101975594666133`, 🇺🇸🇬🇧🇨🇦🇦🇺): ≥ 50 activos (est. 542) de «1 Day Welder» US$ 58 / «Learn welding right at home» = curso en video de la fundadora (marca personal + video, Filtros A y D); los «cheatsheets» son carnada. Sin tarjeta.
- Upleaf Studio (`1349687651563870`, 🇺🇸): «$17 once, budget by paycheck» (planilla de sueldo), 5 / 6 → vigilancia, re-conteo 2026-11-29. The Paycheck Plan (`1381188005083313`) 0 / 3 y Plum & Pencil (`1357650247441173`) 1 / 3 (planner 2027 US$ 14,99): testers de hoy.
- The Family Folder (`487465484456721`, 🇺🇸, ya visto en herencia-y-papeles): 4 / 10 → vigilancia, re-conteo 2026-11-29. Checkride Study Guide (`470054809533979`): ≥ 22 / 50 pero flashcards físicas (Filtro D), ya anotado.
- Spreadsheetables (`110233751896223`, 🇺🇸): ≥ 50 activos de «15 tools for $27» = plantillas para revender (PLR / reventa), sin tarjeta; Create Your Digital Dream «117 Done-For-You Products $17» y Appisi «300 mini apps to resell» idem.
- Visuals Loop (`632093113327237`): «Black Friday Mega Bundle $47», 2 / 5, bundle de promo; Debt Free Progress Pack, Fresh Start Studio, LogicExcel, Tre Renee Plans: 1-2 ads de planillas de deuda cada uno (competidores de Ultimate Budget Planner, sin cohorte).
- Visual Guide Lab (`1467890346400480`): ya con tarjeta; sumó «Part 107 Explained Visually», «Knots, rigs and reels, one page each» (pesca, CA AU, 3 ads del 20-nov) y 7 ads de Part 107 US.
- Cero activo / ruido: `layoff severance guide` (0 ACTIVE en GB CA AU, GuideLyra 3 ads en `ALL`), `first apartment checklist`, `college dorm checklist`, `identity theft recovery` (DramaBox/novelas), `$27 today` / `£9 today` / `£17 only` (DramaBox, Black Friday físico). Páginas de «Ready Nation» (survival, camping checklist) = libros/físico, sin tarjeta.

EN 2026-11-21 (3ª corrida, C con huellas nuevas): nada que pase la vara; se barrió instant download, digital download, workbook pdf, printable flashcards, template bundle, illustrated guide, step-by-step guide, notion template, canva templates, mini course, hvac cheat sheet, citizenship test pdf, moving checklist pdf, security guard exam, lifeguard study guide, resume template pdf, wedding planner pdf, chess openings pdf, visa checklist pdf y tattoo aftercare pdf (US GB CA AU).

**Señales del día EN (21-nov, 3ª corrida)**
- Live Well & Fully (`447372159049335`, 🇬🇧): «Love Another Way Jumpstart Guide» (familias de adictos), **≥ 50 sobrevivientes / 284 activos** en GB (piso, tope 50), pero **falla el gate**: fundadora con credencial (Barbara Decker, CFRS) vende con su historia, programa de 5 módulos «under $200» (curso/coaching). Sin tarjeta; la hermana `2025115757540683` corre el mismo copy.
- Megan Hayes (`1462418793620408`, 🇺🇸): «Illustrated Guide to the CIA Exam Part 1», 0 / 10 (lote único del 20-nov; GB/CA/AU ~6-9 del mismo lote). Molde de examen ilustrado en PDF, página nueva: re-conteo 2026-11-28.
- Classroom Makers (`1365252206677904`, 🇺🇸): guía de robótica para el aula «half price», 3 / 21 (18 ads del 21-nov). Speak Clearly Academy (`1295219996997308`, 🇺🇸): workbook PDF US$ 1,99, 1 / 17. Ambas vigilancia sin cohorte → re-conteo 2026-11-28.
- Viral Content Design (`101868528855890`, 🇺🇸🇬🇧🇨🇦🇦🇺): 20-32 activos por país de «700 Canva Posts for <vertical>», todo del 20-nov y multi-vertical (portafolio de plantillas): sin cohorte.
- Carlos Medina «VRF Field Manual for HVAC Techs» (`570406022821396`): 0 activos en GB, ~19 ads en `ALL` (GB CA AU) = oferta apagada.
- Cero activo / ruido: `hvac cheat sheet` (solo `ALL`), `mini course` y `security guard exam` = short-dramas.

EN 2026-11-21 (tarde, C con huellas nuevas): nada que pase la vara; se barrió quick reference pdf, on one page pdf, stan store pdf, systeme io pdf guide, starter kit pdf, toolkit pdf, puppy training pdf, divorce checklist pdf, family budget template y first time home buyer checklist (US GB CA AU).

**Señales del día EN (21-nov, tarde)**
- Central Pack (page 1178523422005192, 🇺🇸): fábrica de «<tema> — Professional Edition» / «Master <tema> Visually — 6 Volumes + 5 Bonuses» (carnicería, náutica eléctrica, BMS, pizza, sailing, gelato, aquarium, floristería, cerámica…), ~124 activos estimados en US, **0 sobrevivientes en los 50 visibles** (creados 18-21 nov, ≥ 15 temas, 2-4 ads por tema). Páginas hermanas del mismo molde con dominio `*.shopsmartdigital.com`: Smart Digital `1383014634885117`, Kit Online `694829257056991`. Portafolio, no una oferta; vigilancia sin cohorte → re-conteo 2026-11-28. Embudo no verificado (no se scrapeó). Alta a la cola como nodo `virgen`.
- Business Explained (`105964635528739`, 🇺🇸): ~104 activos estimados, 70 productos de negocio con «Black Friday 70 % off» + «Instant PDF Download»; 0 sobrevivientes visibles (todo del 20-21 nov). Promo de temporada; re-conteo 2026-11-28.
- Skillsbeyondschool.com (`370943336753200`, 🇺🇸): «Pass the NREMT» 3 libros (guía + 245 preguntas + memory pack), 12 ads del 21-nov = 0 sobrevivientes; 3 ads de plantillas de cerámica del 18-nov (manualidades, se ignora). Molde de examen en PDF, oferta de hoy.
- Budgetdog (`103422968063947`, 🇺🇸): 552 activos pero es lead-gen de inversión/retiro (workshop gratis), no infoproducto; Aportino Puppy Training (`1427212830477353`): 12 ads de «Free SOS cheat sheet» del 17-nov, lead magnet gratis (PLN) = 0 sobrevivientes y sin oferta paga visible.
- Cero activo con `ALL`: `divorce checklist pdf` US/GB (12-13 ads solo en `ALL`, páginas de personas) — sin hallazgo; `first time home buyer checklist` solo inmobiliarias con lead magnets gratis.

EN 2026-11-21 (C operadores/agenda): nada que pase la vara; se barrió Visual Journeyman Style, Energy Profitable, Spanish Made Visual, Nara Costa, James Carter, Markus Schneider, Fernanda Oller, Rowan House Press y Diagram Books.

**Señales del día EN (21-nov)**
- Visual Journeyman Style (page 1517462271441246, 🇺🇸): «Journeyman Exam Made Visual» US$ 19, **10 / 10 por API → cerca, no tarjeta**: 8 ads creados en 3 minutos del 9-nov + 2 del 11-nov (solo 2 fechas distintas, falla el filtro de ≥ 3 fechas de NUBE §4) y el 20-nov un ad tenía < 100 impresiones (9 con esa regla; gana el reloj que lo deja afuera). `ALL` = `ACTIVE` = 10, 0 en 🇬🇧🇨🇦🇦🇺. Embudo verificado el 20-nov. Re-conteo 2026-11-28.
- Energy Profitable (ya en el cerebro, 720903437767543): un solo creativo «Wire any control circuit», **🇺🇸 ≥ 30 / 50 (est. 101 activos) y 🇬🇧 ≥ 33 / 50 (est. 92)**, 4-5 fechas de creación, desde el 11-12 nov; sin oferta nueva. Pasaría la vara en conteo, pero es operador ya cazado (ficha «observar»): sin tarjeta. Sin snapshot ni embudo re-verificados.
- Fernanda Oller (ya en el cerebro, 1262265860313000): oferta nueva «The Wiring Regs in Pictures» (UK) **15 / 15 en 🇬🇧**, 4 fechas, desde el 4-nov; 🇺🇸 «84 Sheets» 3 / 6. Building Defects Atlas sigue en 3 ads de 17-nov (0 sobrev.). Operador ya cazado: señal, embudo no verificado desde la nube; candidata a ficha propia si Carlos lo pide.
- Spanish Made Visual (1456443927546734, 🇺🇸): 19 / 24 (el 20-nov: 8 / 23), pero la página migró a **francés** («The French past on one page», «102 French rules») + kit español; 2 ads por título como máximo → portafolio, no una oferta. Re-conteo 2026-11-28.
- Lanzamientos sin cohorte: Rowan House Press 🇬🇧 15 ads del 17-nov (≥ 4 productos, 0 sobrev.); Diagram Books 🇬🇧 0 con `ACTIVE`, 50 en `ALL` (≥ 11 productos de examen, todos del 17-nov); Markus Schneider 🇬🇧 7 / 0; James Carter 🇺🇸 «Cybersecurity Mind Maps» 4 / 0; Nara Costa 🇺🇸 2 / 7 en 3 productos (linfático nuevo del 17-nov, radiografía y aviación con 1 sobreviviente c/u).

EN 2026-11-20 (tarde, B perforar `exámenes-certificaciones/guias-ilustradas`): nada que pase la vara; se barrió pilot exam study guide, NCLEX study guide pdf, electrician exam visual y real estate exam cheat sheet.

**Señales del día EN (tarde)**
- Visual Journeyman Style (page 1517462271441246, 🇺🇸): «Journeyman Exam Made Visual», PDF de 100 mapas NEC + 4 bonos, US$ 19 (tachado 49); **cerca (9 sobrevivientes, 1 con <100 impresiones)**, 10 días, 0 en 🇬🇧🇨🇦🇦🇺; página fantasma, embudo verificado por Firecrawl (landing directa → checkout, plataforma Impultienda). Mismo molde que Visual Guide Lab. Re-conteo 2026-11-27.
- AirlinesOnAutopilot / Pilot Avabelle (842356615617987, 🇺🇸): lesson plans editables CFI/CFII/MEI (US$ 88-120), **vigilancia (≈6, 46 d)**; el resto de la página es suscripción en video y «ex-examinador» (Filtros A-bis/D). Re-conteo 2026-11-27.
- Stark Exam Prep (1320551981152367, 🇺🇸): examen de real estate «32 páginas color», 28 activos, 0 sobrevivientes (todo de ≤ 4 d); re-conteo 2026-11-27. Clearpage Books (1452448654619131): 119 activos, un SKU por examen con «+2 bonus books», todo del 20-nov; cohorte invisible. Checkride Study Guide: flashcards físicas, fuera por Filtro D.

### 🎯 Guías ilustradas de examen oficial en PDF (Part 107 / PPL / radioaficionado / oficios) — Visual Guide Lab 🇺🇸 US · `exámenes-certificaciones/guias-ilustradas` · 2026-11-20 · sesión EN
- **Qué es:** PDF de 79 páginas «un tema por página, cada regla dibujada» + 2 bonos (checklist del día del examen y glosario), **US$ 27** pago único (tachado US$ 95,80), garantía 30 días, entrega por email; un subdominio-landing por examen (Part 107, Private/Sport/Commercial Pilot, Amateur Radio, CWI, plomería, marítimo, UK PPL…).
- **Por qué es ganador:** cohorte 7+ ≥ 11 / 30 en el slice «pilot» (edades 7 y 9 días, 3-4 copias por creativo), 168 activos en US; página fantasma (sin cara); embudo verificado (ad → landing directa → checkout). Salvedad: casi todo el resto de la página es de < 4 días (fábrica multi-SKU que recrea tandas), sin escalonamiento largo; Fenix Library (119 activos, mismo molde, todo de hoy) corre lo mismo.
- **Qué hacer:** modelar el molde (guía de examen ilustrada, 56-80 págs, quiz de 3 preguntas como creativo, bonos, precio ~US$ 27) en un examen propio · destino sugerido: 🇧🇷 BR (CNH/OAB/concursos) o 🇪🇸/🇮🇹/🇩🇪 con examen oficial masivo; US/GB ya tiene dos operadores · ángulo: «la guía solo lo lista, aquí cada regla está dibujada».
- **Ads Library:** 🇺🇸 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&view_all_page_id=1467890346400480&search_type=page&media_type=all · 🇬🇧 (cohorte 0 visible) https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=GB&view_all_page_id=1467890346400480&search_type=page&media_type=all
- **Landing:** https://drone-pilot-made-visual.visualguidelab.com/ (venta directa, US$ 27)
- Score ≤1/4 (longevidad 9 d, volumen 11, duplicación baja, hueco sin barrer) · Decisión: —
- Evidencia: API; snapshot y embudo verificados vía Firecrawl (no WebFetch); checkout no recorrido, upsells no vistos.

**Señales del día EN**
- Fenix Library (page 1455853117614278, US): mismo molde de guías «drawn» de certificaciones (ICC, NATE, CFOT, Network+…), 119 activos, todos de las últimas 24 h; sin cohorte aún.
- Music Solved (page 1465563836630767, US/GB): «System 365» un SKU por instrumento, 189/179 activos, churn; slice banjo cohorte 4.
- Mariana Williams Creations (208 activos US) y Craft Room Co (13, cohorte 4): fábrica de churn y tester; sin tarjeta.

EN 2026-11-20 (2ª corrida, B perforar `idiomas`): nada que pase la vara; se barrió spanish workbook, french grammar pdf, italian visual guide, german vocabulary printable, learn spanish pdf, french maps, japanese cheat sheet, italian printable, german grammar pdf, korean alphabet, italian mind maps, japanese grammar maps, portuguese visual maps.

**Señales del día EN (idiomas)**
- Familia «mapas visuales de idiomas» (6 páginas fantasma, mismo molde, 5 idiomas, todo lanzado/recreado en los últimos 9 días, todo en 🇺🇸): Spanish Made Visual (page 1456443927546734) **8 / 23 · vara 🇺🇸 20** (nivel 1, 4 tandas hasta 30 d, ahora vende francés + kit Spanish a US$ 19); German Grammar Made Visual (1469941799530737) 6 / 30; Fluency Mapped (1382560178271800) 0 / 50 ≥ (tandas a 2 y 6 d); Italian Made Visual (1345879781951055) 0 / 5; Japanese Mapped (1515773991610387) 0 / 17 (lanzó ayer). Re-conteo con fecha: 2026-11-27.
- Fluency Mapped = Spanish Mapped™, 520 mapas PDF + 5 bonos, US$ 14,90 (tachado 146) con oferta de Black Friday, checkout Hotmart, landing oakguides.com/spanish-mapped/ verificada vía Firecrawl; es el molde a mirar si algún operador de la familia cruza 20.
- Jessica Lee (102387828377781) y red de ~10 páginas-persona: 14 / 43 por creación (9 por entrega), una sola tanda; vende curso en video + audio (US$ 37) → cae por Filtro D y marca ficticia, no por número.

<!-- TARJETAS-BR: la sesión BR inserta sus tarjetas del día justo debajo de esta línea -->

BR 2026-11-22 (dom, lint de la cola + 40 semillas): nada que pase la vara; se barrió pdf completo, apostila pdf, resumo visual, e-book completo, passo a passo, curso gravado, minicurso, acesso vitalício, receba no e-mail, fichas para imprimir, checklist completo, modelo pronto, templates canva, manual ilustrado, guia ilustrado, numa página, R$ 19,90, R$ 37, adestramento filhote, aquarismo iniciante, fotografia celular, xadrez aberturas, violão cifras, nós de pesca, checklist mudança, checklist casamento, enxoval bebê, apostila soldador, apostila refrigeração, apostila energia solar, apostila mecânica automotiva, banho tosa, design sobrancelha, oratória guia, leitura dinâmica, primeiros socorros, abrir MEI, imposto de renda, aposentadoria INSS e treino casa (BR).

**Señales del día BR (22-nov)**
- Guedes Serviços (`1315091175012794`, 🇧🇷): «Apostila de Montagem e Manutenção de Ar-Condicionado Split» + videoaulas, R$ 10, venta por WhatsApp (copy: «recebe tudo primeiro e paga depois»), «Apenas 10 reais»; **8 / 24 por creación → cerca**, un solo creativo, 5 ads más cumplen 7 d el 11-24/25 → **re-conteo 2026-11-25** (embudo WhatsApp válido; bundle PDF + video, Filtro D por revisar). Alta a la cola como nodo `virgen`.
- Facilitaê (`220873114449117`, 🇧🇷): «Guia Visual da Reforma Tributária» + «Faça seu IR 2027 sem travar» + «Emita, declare e cadastre você mesmo»; **≥ 51 activos (tope 50)**, pero «Guia Visual» = 5 sobrevivientes (todos del 9-nov, una fecha) → **vigilancia**, re-conteo 2026-11-25; embudo no verificado. Alta a la cola como nodo `virgen`.
- Metaleitura (`118151775445527`, 🇧🇷): «LEIA + RÁPIDO E MEMORIZE» **≥ 31 sobrevivientes / 224 activos** (tope 50), pero **falla el gate**: VSL gratuita → checkout Hotmart de «vaga» en el método de leitura dinâmica (curso en video, Memory Academy; Filtros C y D). Sin tarjeta.
- Chuva de Papel (`272254086228745`, 🇧🇷): «Planner do Nosso Casamento», **7 / 18 → cerca**, pero es agenda **física** de papelería (Shopify `chuvadepapel.com.br`) con 22 archivos bonus: Filtro D salvo que el dolor se resuelva con el PDF; re-conteo 2026-11-29.
- Easy Mapas (`1310056155527139`): 4 / 8 repartidos en 4 ofertas (comandos elétricos, DPS, off grid, projete seu sistema solar) = portafolio, vigilancia sin oferta > 3. Resumos Animados (`1454128997777436`): 4 / 13 en 5 concursos distintos (CETESB ≤ 2) = portafolio. Ana Julia (`1296281160245173`): 8 / 31 repartidos en SUS, emendas, conselho tutelar, patrimonio = portafolio de «120 Mapas Visuais»; sin oferta > 4.
- Fundação Refrigeração (`1230876866767299`): 8 / 29 pero una sola fecha de creación (30-jun) + lote del 20-nov = posible zombi, curso; Ingriddomkt (`1425362393995318`) «Packs Canva» 0 / 20 y Atlas residente (`1367343386472876`) «PDF R$ 97» residência médica 0 / 8: lotes de hoy sin cohorte, re-conteo 2026-11-29 (Atlas residente: SUS-SP / UNIFESP, PDF R$ 97 pago único, embudo no verificado).
- Cero con ruido: `nós de pesca`, `treino casa`, `primeiros socorros` (short-dramas DramaBox), `checklist mudança` (portafolios de mapas visuales), `banho tosa`, `aposentadoria INSS`, `imposto de renda` (petshops y abogados). Nichos excluidos ignorados.
- Aprovados Enem 2026 (`1287009421164355`, 🇧🇷): «pack» de mapas mentais/resumos ENEM, **9 / 9 sobrevivientes por creación** (8-9 sep), mismo creativo ×9 (duplicación ×9) → «cerca» en número, pero **posible zombi**: solo 2 días de creación distintos, ningún ad de los últimos 30 días, y el snapshot dice «Ad isn't in the Ad Library» (sin impresiones). Sin tarjeta; embudo no verificado; re-conteo 2026-11-29 (segunda corrida BR del 22-nov, mismos 40 barridos).

BR 2026-11-21 (A huella): nada que pase la vara; se barrió guia prático pdf, planilha pronta, material digital, mapas mentais, ebook completo pdf (todas con `countries: BR`) y 7 conteos por page_id.

**Señales del día BR (A huella)**
- Mentagrama Mapas Mentais (page 395083497020515, 🇧🇷): cards ilustrados para concursos a R$ 10 («INSS: 800 cards ilustrados», «800 Cards Banestes»); **8 / 16 por creación (7 por entrega)** pero **una sola tanda (2026-11-13)** y mezcla 2 ofertas (INSS 5 + «Apenas R$10» 3) → por oferta ≤ 5 = **vigilancia**; re-conteo 2026-11-28. Evidencia: API; snapshot y embudo no verificados desde la nube.
- Mapa do Aprovado (1188080441064364): «Por Apenas R$10,00» **5 / 36 · vigilancia** (tandas 10-09, 10-16, 11-08); los 28 ads «200 Mapas Mentais para o TJSP» son una sola tanda de ayer (0 sobrev.). Re-conteo 2026-11-28.
- Vistoria Pro (874002919132130): «+290 ferramentas para inspeção predial» (checklists/laudo) 0 / 8 en la oferta actual; la línea anterior «+300» 1 sobrev. (09-22); 3 sobrev. en toda la página, 3 ofertas distintas → señal.
- Descomplica em Mapas (1348952658292622): «Revise cada tema em 5 minutos», 0 / 4, nacido ayer. Lucro Certo (planilha R$ 37), Garimpo Digital (orquídeas), Luiz Tenório (Kit R$ 47): 0 sobrev., todo de ≥ 11-18.

BR 2026-11-20 (tarde, B perforar `profesiones/examenes-y-oposiciones`): nada que pase la vara; se barrió resumo OAB pdf, mapas mentais concurso, prova CNH simulado pdf y resumos enfermagem pdf.

**Señales del día BR (tarde)**
- Maria (page 1303528502850034, 🇧🇷): «1.000 Questões Comentadas de Enfermagem + Bônus» R$ 10, **8 / 27 · vigilancia→cerca (vara 10)**, 33 d, 4 tandas; re-conteo 2026-11-27. Embudo y entregable no verificados desde la nube.
- O Concurseiro Aprova (1113714935158012): «Edital Ilustrado OAB», 79 activos, los 50 visibles de ≤ 5,5 d (0 / 50 ≥ piso); cola vieja invisible por el tope de la API. Re-conteo 2026-11-27.
- Carlos Santos (268341876371967): cards de enfermagem 5 / 22 en la oferta, página multi-SKU (fisioterapia, simulador); sin tarjeta.

BR 2026-11-20 (C operadores): nada que pase la vara; se barrió Packs & Moldes Pro, Arquiteta Clara Finelon, Nova Mind, «manual eletricista pdf» y 3 páginas nuevas (Atlas Digital, Pronto Para Usar, Elétrica King).

**Señales del día BR**
- Packs & Moldes Pro (page 1227856100409706, ya en el cerebro): «Manual do Eletricista Residencial» **29 / 29 · vara 🇧🇷 30**, 3 tandas (27-ago, 06-sep, 14-sep; 67-85 d), ratio 100 %; cerca de la vara. Re-conteo 2026-11-27. Embudo no verificado desde la nube.
- Arquiteta Clara Finelon (1282745681595572) y Nova Mind (1372898352562817): 0 ads en 🇧🇷 con `ALL` hoy (2026-11-20); hecho de esta fecha, no descarte.
- Atlas Digital (1342175415650748, 🇧🇷): fábrica multi-SKU (27 ads con `ALL`; diagramas de bomba, diagnósticos de injeção, AEE); casi todo de las últimas 48 h, cohorte 7+ ≤ 3 por oferta. Sin tarjeta.

<!-- TARJETAS-ES: la sesión ES inserta sus tarjetas del día justo debajo de esta línea -->

### 🎯 +350 mapas mentales de farmacología ilustrada (PDF por WhatsApp) — Digi Aprende 🇵🇪 PE · `salud-farmacologia-mapas` · 2026-11-22 · sesión ES
- **Qué es:** pack PDF a color, descargable e imprimible, de +350 mapas mentales ilustrados de farmacología (mecanismos, indicaciones, efectos adversos, dosis, antibióticos, antihipertensivos…) para estudiantes de Farmacia, Medicina, Enfermería y Nutrición, con 3 bonos; entrega por WhatsApp «en 2 minutos». Precio no dicho en el copy (piso n/e).
- **Por qué es ganador:** **19 / 39 sobrevivientes en 🇵🇪** (ACTIVE = ALL = 39, ninguna oferta apagada); cinco fechas de creación (11-oct, 22-oct, 4-nov, 19-nov, 21/22-nov), ad más viejo ~41 d; el mismo creativo «Descárgalo HOY / en 2 minutos» repetido ~29 veces; sin marca personal (solo logo de página); el molde también lo corren Estudia Sencillo (CO/MX), Vitus y Salud en un Minuto (MX) y Farmacología Esencial/Simone Longo/FarmMaps (BR).
- **Qué hacer:** modelar tal cual (cuaderno ilustrado de mapas, formato que ya rinde en el cerebro) · WA: arbitraje de embudo (landing con checkout a 3-4× el piso) · destino sugerido 🇲🇽 🇨🇴 y, por ticket, 🇺🇸 🇪🇸 🇮🇹 🇧🇷 🇵🇹 (IT/PT comparten la keyword: leer el idioma del creativo) · ángulo «farmacología sin memorizar».
- **Ads Library:** 🇵🇪 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=PE&view_all_page_id=308598599011471
- **Landing:** WA: ficha reconstruida (vende pack PDF de mapas · bonos sin nombrar · mensaje prellenado no visible) · no se sabe: precio, contenido exacto, escalera, garantía.
- Score 1/4 (③ duplicación) · escalera n/e · Decisión: —
- Evidencia: API; snapshot verificado por Firecrawl (2 ads); landing de WhatsApp no abre desde la nube, embudo = ficha WA del copy.
- **Re-conteo Opus 22-nov:** 🇵🇪 **19 / 39 por API** (el número de Sonnet es el bueno; la web con versiones daba 21). Todo va a WhatsApp; el precio solo sale escribiendo al chat (no se hizo). ✅ pasa.

**Señales del día ES (22-nov, dom — lint + semillas)**
- Lint de la cola ES: sin hallazgos. Embudo: 40 semillas nunca usadas (24 huellas + 16 molde × tema) × CO MX ES CL PE, 10 páginas nuevas pasadas por paso rápido, 1 paso completo.
- **Estudia Sencillo** (page 113453315134646, molde farmacología, USD): 🇨🇴 130 y 🇲🇽 138 activos, tope 50 con la cola vieja oculta (7 ads de farmacología de 18 d visibles); mezcla con guía GLP-1 clínica → cohorte indeterminada (tope 50, solo se ven los nuevos): verificar en la PC, 🇨🇴 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=CO&view_all_page_id=113453315134646 · 🇲🇽 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=MX&view_all_page_id=113453315134646
- **Fer Rendon** (1977647735819349, 🇲🇽): plantilla Excel «Costeo de Menú» y «Finanzas Constructoras» (MXN), 159 activos, 0 / ≥ 50 visibles todo < 2 d → cohorte indeterminada (tope 50); nombre de persona, posible marca personal; re-conteo 2026-11-29.
- **Estudio Contable Online** (1216662331539709, 🇨🇴🇲🇽🇨🇱): «Método Contabilidad Práctica · 7 cuadernos + 8 bonos» (US$), 0 / 12 en CO, todo del 20-nov; oferta no validada, re-conteo 2026-11-29.
- **Ana Laura** (114860084961404): «10 guías visuales» de acuario, 13 activos en CO/MX/CL/PE y 9 en ES, 0 / 13 en CO (4 d); oferta no validada, re-conteo 2026-11-29.
- Negocio en Regla (1382378091630921, 🇲🇽) «Carpeta de Seguridad e Higiene» 0 / 21 · Cocina en Regla (1516759901509982, 🇲🇽) «+50 documentos para tu cocina» 2 / 30: vigilancia ninguna, re-conteo 2026-11-29 (mismo operador, USD).
- Pautas Listas para Urgencias (1358096157393957, 🇪🇸): 134 activos, 0 / ≥ 50, los ads mandan «Búscalo en la app» → Filtro D (app), sin tarjeta.
- Veterinario Lucas (🇨🇱) «180 mapas de emergencias equinas» US$ 12,90 0 / 4. `test autoescuela` = cero activo en CO/MX/PE (también con ALL); solo 🇪🇸 tiene activos (Amezti Academia 10, academia online).

ES 2026-11-21 (mañana, B perforar `profesiones/examenes-y-oposiciones` tramo ES): nada que pase la vara; se barrió temario oposiciones esquemas, resúmenes oposiciones PDF, psicotécnicos oposiciones PDF (ES), examen ICFES guía (CO), guía examen COMIPEMS y guía UNAM PDF (MX).

**Señales del día ES**
- FemBooks (page 1428908536975654, 🇪🇸): cuadernos de oposición por especialidad («Oposiciones de Primaria/PT/AL/Infantil · 57-59 páginas», «EIR sin farmacología»), 33 activos, **0 sobrevivientes** (todo del 19-20 nov, muchas copias por creativo); oferta no validada, re-conteo 2026-11-28. Evidencia: API; snapshot y embudo no verificados desde la nube.
- Fichas Visuales · Administrativo del Estado (1432806236580374, 🇪🇸): «157 fichas del Administrativo C1», 5 activos, todos de hoy; misma plantilla que la red AprendIA; re-conteo 2026-11-28.
- Matemáticas con Toxqui (325078871561169, 🇲🇽): 27 activos «Curso UNAM/IPN 2027», ≥ 18 sobrevivientes, pero es curso en vivo con profesores (verificado por Firecrawl) → Filtro D/A, sin tarjeta. Tu Examen (1095731520298677, 🇲🇽): guías COMIPEMS/UNAM/ENARM, 2 sobrevivientes → señal.

ES 2026-11-20 (tarde, B perforar `fichas-visuales-aprendia`): nada que pase la vara; se barrió las 4 fanpages hermanas de AprendIA (🇲🇽), `fichas ISO 9001`, `fichas guía visual` (🇨🇴) y Psyacademy (🇨🇴 🇲🇽 🇪🇸).

**Señales del día ES (tarde)**
- Red AprendIA, perforada por página (🇲🇽, sin sumar hermanas): Aprende Hoy (page 1365055716696947) 36 / 62 por página pero ~25 SKUs distintos, ninguno con más de 3 ads (ISO 9001: 3); Guías Paso a Paso (1381808071689792) 13 / 77; Aprende Ya (1288181344388955) y Aprende Más (1390929764102651) 0 / ≥50 con todo de < 7 d (cola invisible). Sigue siendo portafolio: sin tarjeta. Re-conteo por SKU 2026-11-27.
- Psyacademy (page 944317715424068): «210 fichas visuales de psicopatología», mismo molde que el mapa de trastornos del Este; 🇨🇴 **0 / 7** (más viejo 4,8 d), 🇲🇽🇪🇸 0 / 14 en conjunto, creativos también en FR/EN. Oferta no validada; re-conteo 2026-11-27. Embudo no verificado desde la nube.
- 🇨🇴 `fichas guía visual`: Smartia y Sofi (WhatsApp «Chat with us», oferta no visible en el copy, todo de hoy) y Vida Saludable; no se pudo identificar qué venden. Sin tarjeta.

ES 2026-11-20 (A huella): nada que pase la vara; se barrió acceso inmediato PDF, moldes imprimir PDF, plantillas editables PDF, diagnósticos manual técnico, guía PDF WhatsApp, paso a paso PDF, oposiciones temario esquemas, plantillas Excel, fichas listas docentes imprimir.

**Señales del día ES**
- Red AprendIA (🇲🇽, `aprendia.shop`, nodo nuevo `profesiones/manuales-de-oficio/fichas-visuales-aprendia`): catálogo de 826 guías PDF «N fichas · ~70 págs» a US$ 19,90, venta por WhatsApp; Aprendia: Guías Oficiales (page 1453826204471738) **49 / 55 · vara 🇲🇽 30**, ≥ 10 tandas, 33 d; Guías Expertas Aprendia (1347816741752269) 29 / 56; Aprende Fácil con Guías (1372902832576549) ≥ 26 / 90. No es tarjeta: cada ad vende un SKU distinto (portafolio, 1-3 ads por tema) y las fanpages hermanas no se suman; además el ad de Vías férreas enlaza a una landing con 404. Re-conteo por SKU: 2026-11-27. Precio del copy: no dicho (WA).
- Centro Digital Terapéutico (page 100254106155552, 🇲🇽🇨🇴🇪🇸): Megapack Terapeuta Ocupacional, 6 / 8 · vara 🇲🇽🇨🇴 30 (nivel < 8), tandas a 29 d; sin tarjeta.
- Grupo Futura (801245319736733, 🇨🇴): ≥ 50 ads «Primero recibe, luego paga», cohorte 8; oferta no identificada (parece contra-entrega, probable físico); sin tarjeta.

<!-- TARJETAS-EU: la sesión EU inserta sus tarjetas del día justo debajo de esta línea -->

### 🎯 210 fiches visuelles sur les troubles mentaux (psicología/medicina, PDF 9,99 €) — Esprit Académique 🇫🇷🇧🇪🇨🇭 FR·BE·CH · `salud/fichas-visuales-psicologia-medicina` · 2026-11-22 · sesión EU
- **Qué es:** kit digital de 210 fichas visuales de trastornos mentales (síntomas, criterios diagnósticos, diagnóstico diferencial, casos clínicos) para estudiantes de Psicología y Medicina, + 5 bonus (diferencial, anamnesis/examen mental, psicotrópicos, 50 casos clínicos, repaso exprés); 9,99 € pago único vía Hotmart.
- **Por qué es ganador:** **≥ 50 sobrevivientes en cada uno de 🇫🇷 (97 act.), 🇧🇪 (85) y 🇨🇭 (59)** (piso: tope 50 lleno, todos ≥ 7 d); un solo creativo repetido ≥ 50 veces, 5 fechas de creación (9-oct → 6-nov), más viejo ≈ 44 d; sin persona en ads ni landing; moneda de facturación BRL.
- **Qué hacer:** modelar tal cual (cuaderno ilustrado, «fichas» por trastorno) · el molde ya corre en 🇩🇪 (Gracie Williams `1316868038177272`, Pflege), 🇵🇹 (Mundo Digital `1438697565993676` «210 Perturbações Mentais», todo ≤ 3 d) y 🇨🇴🇲🇽 (Psyacademy, 0 / 7) · destino sugerido 🇺🇸 🇬🇧 🇩🇪 🇮🇹 🇪🇸 (hueco: sin oferta equivalente vista en esos idiomas) · ángulo «révise sans relire des chapitres entiers» / diferencial lado a lado.
- **Ads Library por país:** 🇫🇷 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=FR&view_all_page_id=1229441186928180 · 🇧🇪 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BE&view_all_page_id=1229441186928180 · 🇨🇭 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=CH&view_all_page_id=1229441186928180
- **Landing:** `visuelles.lovable.app` (página Lovable de una pieza) · 9,99 € único, garantía 7 d, CTA a `pay.hotmart.com/X107945722F` · sin nombre propio ni redes · no se sabe: formato exacto (PDF vs app: la FAQ no abrió), contenido de las fichas, upsell.
- Score 2/4 (② 50+ en un país, ③ duplicación; ① a 1 d de los 45) · Filtros A (sin persona), B (checkout Hotmart), D (entregable «fichas»): confirmar formato PDF en la PC · Decisión: —
- Evidencia: API; snapshot (ad 1954173409023519) y landing verificados por Firecrawl; ALL no corrido, `limit: 50` = piso.
- **Re-conteo Opus 22-nov:** 🇧🇪 **84 / 85** · 🇨🇭 **59 / 59** · 🇫🇷 ≥ 60 / 97 (la página no cargó entera). Más viejo 9-oct (44 d). Formato: «espace numérique» de Hotmart con las fichas, pago único 9,99 €, sin upsell ni persona. Gate 5/5 · score 2/4 (② ③). ✅ pasa, la más fuerte del día.

### 🎯 La Carte de l'Anglais — 520 cartes mentales A1→C2 para francófonos (PDF 12,90 €) — Camille Dubois 🇫🇷🇧🇪 FR·BE · `idiomas` · 2026-11-22 · sesión EU
- **Qué es:** 520 mapas mentales de inglés en 6 recorridos (base, construcción, tiempos, conversación, autonomía, avanzado) + 6 bonus (falsos amigos FR-EN, pronunciación, 120 phrasal verbs, 250 frases, planner 30 d, expresiones profesionales); 100 % PDF, 12,90 € (tachado 175 €) «hasta el 30 de noviembre» (promo Black Friday), garantía 30 d.
- **Por qué es ganador:** **≥ 14 sobrevivientes en 🇫🇷 (270 act. est.) y ≥ 24 en 🇧🇪 (241 est.)** de la misma oferta (piso, tope 50; reloj de creación y de entrega coinciden); ads de la misma oferta desde el 19-oct (34 d) con rotación continua de creativos; hermana en español (`academyaxon.com/carteespagnol`, «Ser ou estar ?»).
- **Qué hacer:** modelar el molde «tu idioma en cartes mentales» (cuaderno ilustrado, ya rinde) · idiomas es nodo 🟢: elegir par de lenguas libre (p. ej. inglés para hispanohablantes / alemán / italiano) · destino sugerido 🇮🇹 🇩🇪 🇪🇸 con el par local, y 🇺🇸 🇬🇧 con español/francés · ojo: es oferta de promo, el piso real del precio podría ser mayor.
- **Ads Library por país:** 🇫🇷 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=FR&view_all_page_id=1077014278820945 · 🇧🇪 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BE&view_all_page_id=1077014278820945
- **Landing:** `academyaxon.com/cartedelanglais/` («Axon Digital», WordPress) · 12,90 € de 175 €, «+4 127 apprenants», testimonios como capturas · checkout `pay.hotmart.com/X107204956Y` · sin persona visible: el nombre de página «Camille Dubois» no aparece con cara en los ads (confirmar en la PC) · no se sabe: precio fuera de promo, upsell, CH (apareció ≈ 12 ads, sin contar).
- Score 1/4 (④ hueco) · Filtros A (sin persona visible), B (checkout), D (PDF imprimible) · Decisión: —
- Evidencia: API; snapshot (ad 1988106355928314) y landing verificados por Firecrawl; ALL no corrido, `limit: 50` = piso.
- **Re-conteo Opus 22-nov:** **dos ofertas que pasan**, no una — Carte de l'Anglais 🇫🇷 ≥ 84 / 280 · 🇧🇪 ≥ 44 / 240; **Carte de l'Espagnol** (`academyaxon.com/carteespagnol/`, 520 mapas, 12,90 €, Hotmart) 🇫🇷 ≥ 33 · 🇧🇪 15 / 15. La landing `-bf` (Black Friday) es lote del 20-nov. 100 % PDF, sin persona, sin footer. ✅ pasa.

**Señales del día EU (22-nov, dom — lint + semillas)**
- Camille Laurent (`1407481519105013`, 🇧🇪🇨🇭🇫🇷): «La Bibliothèque de Biologie Médicale» **≥ 18 / 50+** en 🇧🇪 (73 act. est., una sola tanda del 31-oct, 22 d) → **pasa la vara**, queda fuera por el tope de 2 tarjetas y porque el «À propos» muestra «Élise Varenne» con foto y testimonios fechados antes de la existencia del dominio (posible marca personal / fachada); 9 € / 17 € (tachado 147 €), `clinical-laboratory-library.online/fr/`. Misma página corre ofertas excluidas (religioso) y «150 fiches d'anatomie de la musculation» (0 por reloj de entrega, < 7 d). Re-conteo + gate en la PC.
- Download Studio (`1344017652136102`, 🇨🇭🇮🇹🇫🇷): paquetes de coaching/clases (gimnasia, patinaje, incienso, 6 vol. por US$ 17) en IT/FR/EN, **118 act. en CH**, 50 visibles todos ≤ 6 d → **cohorte indeterminada (tope 50, solo se ven los nuevos): verificar en la PC** · https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=CH&view_all_page_id=1344017652136102 · portafolio multi-SKU, no marca personal a la vista.
- Céline Moreau (`1367953336410558`, 🇫🇷): «+300 cartes mentales · De A1 à C2» ≈ 3-5 / 27 → vigilancia, re-conteo 2026-11-29 (molde idéntico al de Camille Dubois, otra red).
- Dra Laura Martin (`1274719509066382`, 🇩🇪): «250 Lernkarten Pflegehilfe + 8 Boni» 5 / 5 → vigilancia, re-conteo 2026-11-29 (hermano del molde de Gracie Williams, ya cazado). Sofía Herrera (`1205419289331646`, 🇩🇪): «250 visuelle Lernkarten Kita-Wissen» 6 / 6 en 3 fechas → vigilancia, re-conteo 2026-11-29.
- Molde «210 fiches / Perturbações»: Mundo Digital (`1438697565993676`, 🇵🇹 ≈ 3, 🇨🇭 ≈ 10, 9,99 €, todo ≤ 3 d, 0 sobrev.); Psyacademy (`944317715424068`, 🇧🇪 3 ads de 15-nov); Mesa Ligera (`1219245414615500`, 🇫🇷 0 / 7, todo del 21-nov).
- 0 / n y nuevos del 21-nov (sin tarjeta): Bibliodor (`1342066738997872`, IA/ebooks, 0 / 25), Table File (`1465448983314663`, juegos de misterio, 0 / 23), Marco Bellini IT (proyectos de madera/cuero, 8 ads, 21-nov), Kennis Formule NL (200 piezas de piano en PDF, 16 ads, 19-nov, re-conteo 2026-11-26), Gymspiratie BE (19, 20-nov). Nada de IT/PT/NL con 10+ sobrevivientes.

EU 2026-11-21 (mañana, C operadores): nada que pase la vara como tarjeta nueva; se barrió Concorsi in Mappe, Studio Facile, Pagine Chiare, Fenix Books, Nova Mind, Furgo Libre, Griffbereit, Giulia Ferraresi, Amélie Boissieu, Lorenz Varen, Lingua Chiara, Atelier Horizon, Smart Living Hub y Gracie Williams.

**Señales del día EU (21-nov)**
- Concorsi in Mappe (ya en la bandeja del 11-20, page 1350053468191248, 🇮🇹): re-conteo **23 / 49** (antes 25 / 40), pasa la vara con 9 fechas de creación, más viejo 27 d, ninguno a 45+; titulares nuevos y concurso OSS. La hermana `133896043148377` 0 / 7 (todo ≤ 2 d), no se suma. Sin cambio de veredicto; embudo no re-verificado.
- Amélie Boissieu (ya en el cerebro, 1363004406903385, 🇫🇷): «Kit Comptable Pratique 2027» **≥ 44 / 50** (piso, 74 est.), 13 fechas, 25 d; Giulia Ferraresi (1299765756564104, 🇮🇹): mismo kit **≥ 18 / 50** (142 est.), 7 fechas, 12 d. Operadores ya cazados: sin tarjeta; la edición FR está más madura que la IT.
- Lorenz Varen (ya en el cerebro, 1351005084760173, 🇮🇹🇫🇷): «60 Esercizi / 60 Exercices pour Cyclistes» 29 / 29 activos, 49 d, 4 a 45+; sigue vivo. Griffbereit (1395192210344917, 🇩🇪): «Die ganze Bibliothek» 7 sobrev. de una sola tanda (10-nov) + 3 nuevos del 17-nov = cerca; re-conteo 2026-11-28.
- Pagine Chiare (1362170890322476, 🇮🇹): portafolio de manuales ilustrados «una pagina alla volta» (motosega, carroponte, antincendio boschivo, apicoltura, agrumi, ulivo, tappezziere, Legge 104), 61 activos, todo ≤ 4 d, ningún SKU con cohorte; re-conteo por SKU 2026-11-28. Fenix Books (1311482932059218, 🇮🇹): 242 ads con `ALL`, todo ≤ 5 d, `ACTIVE` devuelve 0 (trampa), cohorte invisible; Studio Facile (740 est., IT+FR) y Lingua Chiara (340 est., todo reiniciado el 20-nov) y Atelier Horizon (341 est.) también sin cohorte visible.
- Furgo Libre (🇫🇷🇮🇹): ofertas nuevas «Cahier de l'Échographie» y «…Installateur Réseaux» (6 ads del 19-20 nov) y «Il Quaderno del Contabile» (3 de 17-18 nov), 0 sobrev.; Nova Mind IT 1 / 4; Smart Living Hub PT/IT 0 / 9 (formación = curso); Gracie Williams DE 4 / 4 sin cambio.

### 🎯 Concursos administrativos en mapas + quiz (105 mapas, PDF €17) — Concorsi in Mappe 🇮🇹 IT · `profesiones/examenes-y-oposiciones` · 2026-11-20 · sesión EU
- **Qué es:** PDF de 105 mapas visuales «un tema por página» de las 5 materias comunes de concursos públicos (L.241/90, TUEL, código de conducta, principios constitucionales, trasparencia) + 160 quiz comentados + kit de preselectiva + 3 bonos e-book; **€17** pago único (tachado €106), Black Friday €29 «con 7 extras»; garantía 30 días; entrega por email, sin área de miembros.
- **Por qué es ganador:** **pasa la vara: 25 sobrevivientes / 40 activos en IT** (un solo page_id, una oferta, 8 tandas, la más vieja 26 d; con los dos relojes ≥ 10); página fantasma (sin cara, testimonios genéricos); embudo verificado: ad → landing directa → checkout Hotmart. Salvedades: ninguno a 45+ días, hay 350 ads en `ALL` (mucho churn de creativos), checkout no recorrido, y existe una página hermana «Concorsi in Mappe» `133896043148377` (5 ads de hoy, no sumada).
- **Qué hacer:** modelar el molde (mapa por tema + glosario + quiz comentado + flashcards, €17-29) para un concurso masivo propio · destino sugerido: 🇪🇸 ES (oposiciones de auxiliar/administrativo) o 🇫🇷 FR/🇵🇹 PT, o 🇮🇹 IT mismo · ángulo: «el manual de 600 páginas sirve para consultar, no para repasar». **Cruzar antes:** `descartados.md` tiene «Concorso Docenti in Mappe» 🔴 (IT, motivo no anotado), mismo molde; y el dominio de Black Friday dice `studioinmappe` (posible parentesco con Studio Facile).
- **Ads Library:** 🇮🇹 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=IT&view_all_page_id=1350053468191248&search_type=page&media_type=all
- **Landing:** https://concorsi-in-mappe.site/ (venta directa, €17; checkout Hotmart `pay.hotmart.com/V107906944N`)
- Score 1/4 (duplicación por título 15/25; longevidad 26 d, volumen 25 < 50, arbitraje sin medir) · Decisión: —
- Evidencia: API; snapshot y embudo verificados vía Firecrawl (no WebFetch); checkout no recorrido, upsells no vistos.

**Señales del día EU (tarde)**
- Familia «La Mappa <concurso> <año>» (🇮🇹, fanpages por concurso: ASMEL 2026 `1476622288866758` 0 / 16, 4 ads cumplen 7 d hoy; ASL Roma 2027 `1527503950440006` y Assistente ASL 2027 `1492168480635775` todo de ≤ 7 d): una fanpage por concurso, no se suman; mismo molde de mapas. Re-conteo 2026-11-27.
- Pflege Ausbildung / pflegelernzettel.de (`111313235043678`, 🇩🇪): 20 ads de una sola tanda a ~131 d aún activos, 29 activos, pero tienda Shopify multi-SKU (€9,99-50,99, bundle €275,99) y «Hey ich bin Laura» → marca personal (Filtro A); sin tarjeta.
- Pilote Autrement (`107304295317415`, 🇩🇪): ATPL-Lernzettel 13 Fächer / PPL 9 Fächer, 14 activos, ≤ 4 sobrevivientes en toda la página y ofertas partidas; señal.
- Martina Rossi (`782531528270117`, 🇮🇹): 200 mappe di infermieristica 0 / ~25 (creado hoy-ayer), multi-SKU y con «storie bibliche» (religioso, excluido); sin tarjeta. Belle Plume (🇫🇷, docentes CRPE/lecture) = portafolio, ningún SKU > 5 ads; Amélie Boissieu sin cambios.
- 🇵🇹 `exame ordem concurso` y `mapas mentais concurso` con 0 activos (hecho de hoy, 2 keywords, sin `ALL`); 🇩🇪 `Prüfungsvorbereitung PDF Lernkarten` 0. Tramo FR/DE/PT sin cubrir del todo.

<!-- TARJETAS-ESTE: la sesión ESTE inserta sus tarjetas del día justo debajo de esta línea -->

### 🎯 «Mintea celor 6 mari genii» (6 libros PDF: Platón, Aristóteles, Nietzsche, Freud, Lacan, Jung «explicados simple», US$ 22,99) — Edu Digital 🇭🇺🇨🇿🇷🇴 HU·CZ·RO · `filosofia-psicoanalisis-pdf` · 2026-11-22 · sesión ESTE
- **Qué es:** colección de **6 libros digitales en PDF** (≈ 60+ págs cada uno, 388 en total, «sin jerga académica», con ejercicios y frases clave): un pensador por libro (realidad, lógica, libertad, inconsciente, deseo, arquetipos); **US$ 22,99** pago único (tachado 45,99, «precio de lanzamiento»), descarga inmediata por e-mail, garantía 7 días; tienda de la red Impultienda con checkout propio.
- **Por qué es ganador:** **pasa** la vara en tres países con una sola oferta y un solo `page_id`: **27 / 28 en 🇭🇺**, **15 / 34 en 🇨🇿**, **15 / 38 en 🇷🇴** (0 / 6 en 🇵🇱, todos del 18-nov); ad más viejo 17 d (2026-11-05); lotes de 10 anuncios iguales por fecha, traducidos a cada idioma. Salvedad: nada cruza los 45 d y no hay variante de precio visible.
- **Qué hacer:** modelar la colección «los 6 pensadores en un PDF cada uno» (tema evergreen de dominio público, carátula por autor, tono «para entender sin ser filósofo») · destino: 🇭🇺 🇨🇿 🇷🇴 ya vivos; el mismo operador ya la corre en 🇳🇱 (señal del EU) y tiene versión inglesa en `en.mentisclassics.com` → 🇺🇸 🇬🇧 🇮🇹 🇩🇪 🇫🇷 🇪🇸 sin mirar · ángulo «repertorio intelectual en dos tardes».
- **Ads Library:** 🇭🇺 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=HU&view_all_page_id=100629922105479&search_type=page&media_type=all · 🇨🇿 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=CZ&view_all_page_id=100629922105479&search_type=page&media_type=all · 🇷🇴 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=RO&view_all_page_id=100629922105479&search_type=page&media_type=all
- **Landing:** https://edudigital-ro.impultienda.ar/ (checkout `/checkout`; sin persona, rostro ni firma; `noindex`).
- Score ≤ 2/4 (longevidad 17 d, volumen 27 en HU, duplicación sí, hueco sin medir) · Decisión: —
- Evidencia: API; snapshot y landing verificados vía Firecrawl (`maxAge: 0`); checkout no recorrido. Es PDF → no cae por Filtro D. Contenido de divulgación sobre autores de dominio público: ver cómo trata cada autor antes de modelar.
- **Re-conteo Opus 22-nov:** 🇭🇺 **26 / 37 por API** (landing `edudigital-hu.impultienda.ar`) · 🇷🇴 21 / 21 · 🇨🇿 20 / 20. La misma página lanzó «estrategas» y «estoicos» (`mentisclassics.com`) el 18-20 nov: 0 sobrevivientes. Sin persona. ✅ pasa.

### 🎯 «Příručka ztracených dovedností» (manual ilustrado de 246 habilidades de autosuficiencia, PDF + 2 libros de regalo, 449 Kč) — Paul Miller 🇨🇿 CZ · `supervivencia-autosuficiencia` · 2026-11-22 · sesión ESTE
- **Qué es:** manual en **PDF** de «habilidades perdidas» (246 según el anuncio, «220+» según la landing), cada una ilustrada en una página vertical con material, tiempo, dificultad y error común: agua, fuego, comida sin heladera, primeros auxilios, reparaciones, huerta en balcón, ahorro; paquete **3 en 1** con «Spíž, která se nikdy nevyprázdní» (60 técnicas de conservación) y «Amišské tajemství» (60 recetas de pan, manteca y queso); **449 Kč** pago único (tachado 1 499 Kč), PDF por e-mail, garantía 7 días «Dědovo slovo».
- **Por qué es ganador:** **pasa** en 🇨🇿: **14 / 28** sobrevivientes, un solo `page_id`, una sola oferta, 3 fechas (7, 12 y 19-nov), ad más viejo 15 d, 14 anuncios con el mismo título; la misma oferta en **8 / 14 🇷🇴** y **8 / 14 🇭🇺** (cerca) y 0 en 🇵🇱. Salvedad: nada cruza los 45 d.
- **Qué hacer:** modelar el manual de habilidades ilustradas «una página por habilidad» (la parte de oficios/reparaciones/primeros auxilios pesa más que las recetas) · destino: 🇨🇿 ya vivo, 🇷🇴 🇭🇺 ya vivos; el molde «habilidades de los abuelos» es de origen anglo y probablemente existe en 🇺🇸 🇬🇧 (no buscado) · ángulo «cuando se corte la luz sabés qué hacer» + bonos de conservación.
- **Ads Library:** 🇨🇿 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=CZ&view_all_page_id=547086365144888&search_type=page&media_type=all · 🇷🇴 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=RO&view_all_page_id=547086365144888&search_type=page&media_type=all · 🇭🇺 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=HU&view_all_page_id=547086365144888&search_type=page&media_type=all
- **Landing:** https://dovednosti.digitalnivedeni.com/ (checkout `dovednosti.impultienda.ar/o/prirucka-dovednosti-cesko`, red Impultienda; sin foto ni bio; cuenta regresiva de plantilla).
- Score ≤ 2/4 (longevidad 15 d, volumen 14, duplicación sí, hueco sin medir) · Decisión: —
- Evidencia: API; snapshot y landing verificados vía Firecrawl (`maxAge: 0`); checkout no recorrido. Es PDF → no cae por Filtro D. «Paul Miller» es solo el nombre de la página (sin persona detrás en la landing): revisar `facebook.com/61570286909993` antes de decir `Idea`. Dos de los tres libros del paquete rozan recetario (nicho excluido): el producto principal no.
- **❌ Re-conteo Opus 22-nov: CAE.** Los 14 «sobrevivientes» de la API están **apagados** en la Library web (6-12 nov → 17-19 nov, estado «Inactivo»). Activos en 🇨🇿: 14, todos del 18-19 nov → **0 / 14**. 🇷🇴 y 🇭🇺: todo inactivo. Lo apagaron y relanzaron: re-conteo 2026-11-25. No llega.

**Señales del día ESTE (22-nov, corrida del domingo)**
- Edu Digital: el EU anotó el mismo operador en 🇳🇱 como «chicos y nuevos»; hoy cruza 10+ en HU, CZ y RO. Molde en otros países: 🇵🇱 0 / 6 (todo del 18-nov), re-conteo 2026-11-29.
- Miłosz Sadowski (`1340709525788261`, 🇵🇱, EUR): portafolio de lecciones y guías (historia 4 / 6, 120 diagnósticos de splits, 1000 GIF de ejercicios, «Niezbędnik studenta»), 4 / 22 por oferta de historia = vigilancia → re-conteo 2026-11-29.
- Trade Pro Kit (`1437484146115003`, 🇭🇺 0 / 17), Złoty Tydzień (`1497253373462050`, 🇵🇱 0 / 8, planillas de presupuesto en Hojas de Google), Knihovna dovedností (`1451064928086229`, 🇨🇿 0 / 6, «173 stran elektro praxe»), Elektronika w schematach (`1086864684514383`, 🇵🇱 0 / 3, «200 map diagnostycznych»), Muzica pe înțeles (`1481694865025481`, 🇷🇴 0 / 3): lotes de 20-22 nov → re-conteo 2026-11-29 (Złoty Tydzień y Trade Pro Kit el 11-28).
- So Follow (`139515539234030`, 🇵🇱 0 / 14, plantillas Canva para cosmetólogas, todo del 17-nov) cumple 7 d el 2026-11-24 → re-conteo 2026-11-24 (plantillas de redes: formato fuera del núcleo, mirar solo si cruza 10).
- Veronica Rose (`1342395585621504`, 🇭🇺 2 / 21; «60 kész feladat» de hoy 0; sus 2 antiguos son un «toolkit sistémico» en neerlandés) = señal, re-conteo 2026-11-29.
- Cero activo en: `planner printabil` y `dresaj cățeluș` (RO), `checklista przeprowadzka` (PL), `checklist stěhování` y `akvaristika průvodce` (CZ), `nyomtatható planner` y `kiskutya nevelés` (HU).

### 🎯 «Atlas Terapeutic Vizual» (120 mapas mentales de emociones para terapia, PDF) — Atlas Terapeutic Vizual 🇷🇴 RO · `salud-mental-visual` · 2026-11-21 · sesión ESTE
- **Qué es:** atlas visual **en PDF imprimible**: 120 mapas mentales de emociones (240 págs, 12 áreas de 10: ansiedad, autoestima, apego, límites, duelo, agotamiento…) + 32 metáforas visuales + 12 láminas comparativas + 12 flujogramas de sesión + 4 bonos (mapas de enfoques terapéuticos, escalas, documentos psicológicos editables, actualizaciones); **US$ 19** pago único (tachado 47), acceso de por vida, garantía 7 días; ángulo «una biblioteca terapéutica visual para quien trabaja con comportamiento humano o lo estudia».
- **Por qué es ganador:** **pasa** la vara: ≥ 23 sobrevivientes / 72 activos en RO (piso, tope 50; 22 más viejos ocultos; ad más viejo visible del 03-nov, 18 d), un solo `page_id`, una sola oferta. Salvedad: todo es de 18 d o menos (no cruza los 45 d) y los 72 son un solo producto sin variantes de precio.
- **Qué hacer:** modelar el atlas de mapas emocionales (formato «un mapa por página», mismo molde ganador de mapas mentales) · destino: 🇷🇴 RO ya vivo; mirar 🇮🇹/🇪🇸/🇩🇪 (público terapeutas/psicología, el molde de mapas ya está validado en el cerebro) · ángulo «tema en minutos desde el índice» y bonos de documentos psicológicos editables.
- **Ads Library:** 🇷🇴 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=RO&view_all_page_id=1408033785736088&search_type=page&media_type=all
- **Landing:** https://atlasterapii.impultienda.ar/ (checkout propio `/checkout`, tienda de la red Impultienda; operador con anuncios en ARS; sin firma ni rostro; landing `noindex`).
- Score ≤ 2/4 (longevidad ~18 d, volumen 23+, duplicación sin medir, hueco sin barrer) · Decisión: —
- Evidencia: API; snapshot y landing verificados vía Firecrawl (`firecrawl_scrape`, `maxAge: 0`); checkout no recorrido. Es PDF → no cae por Filtro D. La landing dice «250+ mapas» arriba y 120 abajo.

### 🎯 «120 Zajęć IPET» (120 fichas de actividades para docentes de apoyo en educación especial, PDF) — Anna Majewska 🇵🇱 PL · `profesiones/material-de-clase-listo/educacion-especial` · 2026-11-21 · sesión ESTE
- **Qué es:** 120 fichas listas («cel, materiały, przebieg krok po kroku» + versión fácil/difícil) para **nauczycielki wspomagające** (docentes de apoyo), ordenadas en los 5 áreas del IPET polaco (cognitivo, motricidad, comunicación, emocional-social, autonomía); **PDF** a e-mail, celular o imprimir; **29 zł** (solo fichas, tachado 89) o **59 zł** con 6 bonos (plantilla IPET, 20 fichas AAC, hoja de progreso, kit sensorial, guía para padres, calendario anual), upsell de salida +10 zł, BLIK o tarjeta, garantía 7 días.
- **Por qué es ganador:** **pasa** la vara: ≥ 15 sobrevivientes / 79 activos en PL con `search_terms: IPET` (piso, tope 50; tanda del 11-nov, 10 d; 29 más viejos ocultos), un solo `page_id`, una sola oferta con muchos creativos; la misma página abre además un SKU nuevo («muzykogramy», 25 por 29 zł, de hoy). Salvedad: todo es de ≤ 10 d.
- **Qué hacer:** modelar el repertorio por áreas con cabecera de objetivos y plantilla del documento de plan individual · destino: 🇵🇱 PL ya vivo; el plan individual existe en otros países (EHCP/IEP/PEI/PDP) → 🇺🇸/🇬🇧/🇮🇹/🇪🇸/🇧🇷 · ángulo «llegás el lunes con algo en la mano» + objetivos escritos en el lenguaje del documento oficial.
- **Ads Library:** 🇵🇱 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=PL&view_all_page_id=1463210366871740&search_type=page&media_type=all
- **Landing:** https://120zajec.com/ (checkout `120zajec.impultienda.ar/o/podstawowy` y `/kompletny`; empresa BALTASCA LLC, Hialeah FL, en el pie).
- Score ≤ 2/4 (longevidad ~10 d, volumen 15+, duplicación media, hueco sin barrer) · Decisión: —
- Evidencia: API; snapshot y landing verificados vía Firecrawl (`maxAge: 0`); checkout no recorrido. Es PDF → no cae por Filtro D. **Salvedad de gate A:** el nombre «Anna Majewska» firma la garantía y es la página, pero la landing no trae foto ni bio y el pie es una LLC de Florida (persona de fachada de red de operadores, no audiencia propia): Carlos debe abrir `facebook.com/annamajewska.nauczycielka` antes de decir `Idea`.

**Señales del día ESTE (21-nov, corrida del sábado)**
- Las dos tarjetas son de la misma red de operadores (tiendas `*.impultienda.ar`, anuncios en ARS/USD, PDF, pago único): vale mirarla como fuente de moldes del Este.
- Escuela Saludable (`100723261734448`, 🇭🇺 30-46 act., 🇨🇿 4, 🇷🇴 1): tarjetas de sistémica familiar para terapeutas («33. kártya», «60 rendszerkártya»), 2 / 46 por oferta suelta, la principal 0 (tanda del 13-21 nov) = vigilancia → re-conteo 2026-11-28; mismo público que Atlas.
- Joanna Zawadzka (`1446090091918778`, 🇵🇱): un creativo único ×18 (16-17 nov), 0 / 18; cumple 7 d el 2026-11-23/24 → re-conteo 2026-11-24 (producto no identificado, landing no abierta).
- Fotó Puska (`1414912408371094`, 🇭🇺): fichas de fotografía con el celular + hoja para impresión 3D «magyarul», 0 / 20; 9 ads del 14-16 nov cumplen 7 d el 2026-11-23 → re-conteo 2026-11-24.
- Știința Bunicilor/Textomat (`1385991297929264`, 🇷🇴): guías de autosuficiencia («Ce faci când se ia curentul»), 0 / 11 (14-16 nov) → re-conteo 2026-11-24; ConocimientoDigital (`1200774293118311`, 🇨🇿): «200 ilustrovaných karet» de oficios, 0 / 10 (18-20 nov) → re-conteo 2026-11-28.
- Next Skill Studio (`148144215050419`, 🇵🇱 0 / 25) y Coach Eva Natural (`149176424947116`, 🇷🇴 0 / 20): lote de 25 y 20 ads iguales del 20-21 nov, producto no identificado; re-conteo 2026-11-28.
- Fenix Library (`1455853117614278`, ya en bandeja EN): apareció en 🇷🇴 (15 ads: macaragiu ISCIR, ADR) y 🇭🇺 (9-11: targonca, emelőgép) con el mismo molde de exámenes ilustrados: país nuevo, sin contar.

### 🎯 «Dosarul Familiei» (carpeta de papeles para la familia: banco, contraseñas, quién llama a quién) — Mente que sana 🇷🇴 RO · `herencia-y-papeles` · 2026-11-20 · sesión ESTE
- **Qué es:** «Dosarul Familiei» (ediție România): **PDF por e-mail para imprimir** (ghid ~30 págs + 10 fișe con 87 preguntas + lista de 26 documentos + 8 cartas de aviso de deceso + mapa digital + ficha «Dacă mi s-ar întâmpla ceva»), plan 48 h-30 días-6 meses; **89 lei** pago único (tachado 259), garantía 14 días; ángulo «el cuaderno vacío / 5 llamadas que harán tus hijos / qué hace el banco al saber del deceso».
- **Por qué es ganador:** ≥ 11 sobrevivientes / 59 activos (piso; limit 50 lleno), 7,2-8,6 d, dos tandas (12 y 13-nov), un solo `page_id`, página fantasma. Salvedad: el margen sobre la vara es de 1 y todo lo demás es de < 7 d; el mismo operador ya probó la oferta en CZ y HU y la apagó.
- **Ya conocido:** es el molde de **Leave It Sorted** (leaveitsorted.com, confirmado por Carlos 2026-11-21): mismo advertorial de 7 motivos, mismo plan 48-30-6, misma lista de 26 documentos y misma carta «si me pasara algo»; la edición US es de 57 págs, 21 secciones, US$ 53 (tachado 98); la tienda ya lista una edición alemana («Der Notfallordner», US$ 39) y declara ediciones UK/AU. El Dosarul Familiei es la **edición Rumanía** del mismo operador (89 lei, ~30 págs, 10 fichas): no es un producto nuevo, es su localización a RO. Cruzar con la ficha local de Leave It Sorted antes de decidir.
- **Qué hacer:** modelar la carpeta digital + hooks «llamadas en orden / qué pide el banco» · destino: 🇷🇴 RO ya vivo; 🇮🇹/🇩🇪 (herencia ya validada en el cerebro) · ángulo: «el cuaderno está vacío, esto no».
- **Ads Library:** 🇷🇴 https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=RO&view_all_page_id=1090738757452147&search_type=page&media_type=all
- **Landing:** https://productsgitals.store/pages/dosarul-familiei (advertorial de 7 motivos «Totul la zi» → botón a `productsgitals.store/go/ro-dosar`; Shopify, tienda «Digital Boost»; checkout y upsells no recorridos).
- Score ≤1/4 (longevidad 8 d, volumen 11, duplicación media, hueco sin barrer) · Decisión: —
- Evidencia: API; snapshot y landing verificados vía Firecrawl (no WebFetch; el snapshot cargó con `firecrawl_scrape`, `maxAge: 0`); checkout no recorrido, upsells no vistos. Es PDF → no cae por Filtro D.

**Señales del día ESTE (tarde)**
- Klidné předání (page 1251607391377130, 🇨🇿): «Celá složka: 60 stran a 3 dárky», plan 5-30-6, mismo ángulo; ALL ≈ 130, `ACTIVE` 2 (6,3 d) → 0 sobrevivientes, apagó casi todo. Querida Familia (1337262539475727, 🇭🇺): mismo molde, ALL 48, 0 activos. Probaron y apagaron; re-conteo 2026-11-27.
- Wydawnictwo Dobrze Wiedzieć (1325462587327331, 🇵🇱): e-book «Testament i spadek» 39,99 zł, 6 ads de 2,6 d, página multi-SKU (e-books de recetas, calendario lunar); 0 sobrevivientes. Twoja Czerwona Teczka (1166102073252078, 🇵🇱): carpeta física con envío, 3 sobrev.; Filtro D.

ESTE 2026-11-20 (C operadores): nada que pase la vara; se barrió Mentális Zavarok Térképe (HU), Harta Tulburărilor (RO), Mapa duševních poruch (CZ), 365 Aktywności Bez Ekranu (PL), Visualia Books, Learning Fast, Illustrated SYP, Verde Guides, Studio Facile (RO PL CZ HU) y Nova Mind.

ESTE 2026-11-21 (A huella): nada que pase la vara; se barrió `PDF do druku`/`karty pracy PDF` (PL), `PDF de printat`/`fișe de lucru` (RO), `PDF k vytištění`/`pracovní listy hotové` (CZ), `nyomtatható PDF`/`munkalapok nyomtatásra` (HU) + 9 conteos por page_id.

**Señales del día ESTE (2026-11-21, mañana)**
- Ready Resources 🇷🇴 (`1440348585824077`, «Biologie clasa a IX-a», material docente listo, «Doar 79 de lei!»): **vigilancia / casi cerca** — 1 sobreviviente hoy de 40 activos, pero un lote de 11 ads cumple 7 d el 2026-11-23 y otro de ≈15 el 11-25 → **re-conteo 2026-11-25**. Portafolio (también «Socio-umane IX–XII»).
- ProKit Digital 🇭🇺 (`868401433027837`): «Egész évi magyar» 5 / 5 (11 d, una tanda) y electricidad 4 / 4 (10 d, oferta distinta) = **vigilancia**; resto (fizika, kémia, matek, testnevelés) 1-3 d. Multi-SKU; re-conteo 2026-11-28.
- Edulabs Resources 🇭🇺🇨🇿 (`1057793390758198`): 12 ads de 7+ d repartidos en 6 ofertas; «ÓVODA KÉSZ» 4 / 4 = **vigilancia**. Mismo molde que ProKit/Ready Resources (red de material docente listo en 4 idiomas, USD); re-conteo 2026-11-28.
- Mesa Ligera 🇵🇱🇷🇴 (`1219245414615500`): PDFs médicos/oficios («Psychiatria w kartach», «Atlas punktów spustowych», «Ściąga Elektryka», «Ściąga ratownika») **0 / ≈49**, el más viejo de 4,4 d; EUR, multi-SKU; re-conteo 2026-11-28.
- Hravá příprava 🇨🇿 (299 Kč, «5 000 aktivit»): 0 / 3 (≤ 3,4 d). Skill Hub Teachers, Easy Notes Studio 🇷🇴: 0 sobrev. (< 3 d).

**Señales del día ESTE**
- Mapa de trastornos (misma oferta «210 cartas, 40 pares, 1 PDF» en 3 países): Mentális Zavarok Térképe 🇭🇺 **0 / 8 · vara 🇭🇺 30**; Harta Tulburărilor 🇷🇴 **0 / 10 · vara 🇷🇴 30** (el más viejo, 12-nov, a 6,6 d); Mapa duševních poruch 🇨🇿 0 activos hoy (ALL ≥ 50 en tandas 04-18 nov, todo apagado). No validada; re-conteo 2026-11-27. Embudo no verificado desde la nube.
- Visualia Books, Learning Fast, Illustrated SYP y Verde Guides (🇷🇴🇭🇺🇨🇿🇵🇱): 0 activos hoy con `ACTIVE`; con `ALL` traen ≥ 50 ads cada una (ofertas de oficios, exámenes, Hashimoto). Hecho de hoy: pausaron o apagaron; no es descarte.
- Studio Facile (ya en el cerebro): 🇷🇴 27 / 41 en toda la página pero portafolio multi-SKU (Contabilitatea 5, Teoria muzicii 5, Navigația 4; ninguna oferta > 8); 🇵🇱 ≥ 50 de los últimos 4 d y 🇨🇿🇭🇺 todo de hoy, cohorte invisible.

---

## Revisiones

| Fecha | Tarjetas revisadas | `Idea` | `tirar` | `re-cazar` | `profundizar` | Tasa |
|---|---|---|---|---|---|---|
| | | | | | | |

> Tasa = `Idea` / revisadas. Por debajo de 20 % se sube la vara; por encima de 70 % se baja.

## Histórico (decididas)

| Fecha | Sesión | Producto | Decisión | A dónde fue |
|---|---|---|---|---|
| | | | | |
