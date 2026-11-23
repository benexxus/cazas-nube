# Caza automática — ES · C operadores + 20 semillas · 2026-11-23 (lun, 04:05 Europe/Madrid)

Mercado: CO MX ES CL PE. Modo del día: C operadores (rotación vigente). Reloj: hoy − `ad_creation_time` ≥ 7 d (corte 2026-11-16 03:05 UTC); entrega no decide ningún caso límite.
Evidencia: API; snapshots y landings abiertos con Firecrawl (`maxAge: 0`) donde se indica.

## Embudo
- **Etapa 0 (ronda de operadores, 3 filas ES, todas)**: Estudia Sencillo (MX, 140 activos, tope 50 → cortes), Pautas Listas para Urgencias (ES, 128 activos, 50 visibles todos ≥ 11-20, mismo título «Búscalo en la app» / PDF según corrección Opus del 22-nov; sin cambio), Digi Aprende (PE, 40 activos < 50 → 19 sobrevivientes por API, sin cambio).
- **Etapa 1**: 40 keywords × CO MX ES CL PE (un país por llamada) en 4 subagentes Haiku. Lotes 2 y 4 volvieron incompletos y se repitieron con Sonnet (ver `log-nube.md`).
  - 20 propias (modo C: temas de operadores ya seguidos): mapas mentales farmacología · fichas enfermería · mapas mentales anatomía · fichas fisiología · fichas ISO · urgencias guía · bioquímica ilustrada · cuadernos contabilidad · kit contable · manual electricista · cuadernos de oficio · mapas psicología · fichas psicopatología · mapas mentales nutrición · fichas pediatría · guías visuales mascotas · mapas mentales derecho · farmacología ilustrada · guías oficiales fichas · fichas ingeniería.
  - 20 semillas (12 huellas + 8 molde × tema): por WhatsApp · solo hoy · $9.990 · S/ 39 · 17 € · ebook pdf · manual pdf · pack pdf · fichas listas · material descargable · pdf editable · guía completa (las huellas de `semillas.md` §1 ya estaban usadas en < 7 d salvo las 5 primeras; las otras 7 son huellas propias de entregable) + fontanero manual · mecánico automotriz fichas · soldadura manual · lactancia guía · peluquería canina · kit herencia · trámites jubilación · paneles solares guía.
- Páginas que salieron: ~70 con 3+ ads; las que tenían 10+ ads en la respuesta o cohorte visible: 14. Verificadas (paso rápido o completo): Estudia Sencillo, Mente Académica, Fichas Foto Pro, Magnus, Doctor PDF, Formula dg, TodoAprende, Lucía, Tienda Digital, Compra Express Online, Marly Lactancia, Atril Estudio (+ ronda: Digi Aprende, Pautas Listas).

## Verificadas — una fila por país
| Página (page_id) | País | Oferta | Sobrevivientes / activos | Veredicto |
|---|---|---|---|---|
| Estudia Sencillo (`113453315134646`) | MX | Farmacología Ilustrada / «Sin Memorizar» (cortes `Farmacología Ilustrada` 7 ads y `Sin Memorizar` 21 ads, ambos < 50; unión 25 ids, 21 de farmacología) | **13 / 21** (7 del 4-nov, 2 BRL del 24-jul, 4 de octubre) | **pasa** |
| | CO | idem (`Sin Memorizar` 20 ads) | 10 / 16 | pasa (borde) |
| | ES CL PE | apareció en las tablas (ES 13, CL 14, PE 8 ads en la respuesta de «mapas mentales farmacología») | no contado por país (costo) | — |
| Mente Académica (`1239880759219492`) | CO | «200 Mapas Mentales de Ingeniería Civil» (los 50 visibles, 338 activos en total: 29 de ingeniería civil de 11-12, 10 «210 Trastornos Mentales», 6 neuroanatomía del 11-13, 5 informática del 11-17) | **≥ 29 / 50 visibles** (piso; tope 50, no se pudo bajar) | **pasa por piso** (una sola fecha de tanda 11-12) |
| | MX ES CL PE | en las tablas con ≈ 25-32 ads de «150 Mapas de Anatomía Cardiovascular», más viejo 16-oct | no contado | — |
| Fichas Foto Pro (`1393955837139841`) | CO | «Sal del modo AUTO: 100+ fichas» (30 ads < 50) | **12 / 30** (+4 de «108 fichas…» del 7-nov = 16 del mismo kit) | **pasa** |
| | MX CL PE | ≈ 20 ads en cada una (tablas), más viejo 30-oct | no contado | — |
| Magnus – Recursos profesionales (`1447686328422547`) | PE | «Kit Contabilidad Sin Enredos» (WhatsApp, S/ 10) (22 ads < 50) | **10 / 22** | **pasa** (borde, 10 exacto) |
| Doctor PDF (`114914206902993`) | CO | fichas visuales para guardias (MXN) | 7 / 14 | cerca (re-conteo 11-30); ES también 14 ads |
| Formula dg (`1365224956675289`) | CO | portafolio: manuales visuales (economía, genética, biología molecular), baraja de constelaciones, recetas (excluido), iluminación, cenas navideñas | 8 / 46 repartidos en 4+ ofertas, ≤ 3 por oferta | no pasa (portafolio) |
| TodoAprende (`1393907173802691`) | ES | manuales visuales multi-SKU (subestaciones, transformadores, ecografía, hematología, concreto) | 0 / 50 visibles (88 activos, todo 11-21; cortes por `search_terms` devolvieron 0) | sin cohorte; re-conteo 11-30 |
| Lucía (`1088407207680523`) | MX | «300 fichas listas para imprimir» (infantil) | 0 / 28 (todo 11-21/22) | fuera (fichas infantiles, nicho excluido neurokids por contigüidad); sin tarjeta |
| Tienda Digital (`1246454168550729`) | PE | «OFERTA» / «Chatea con nosotros» / «SOLO HOY», sin producto en el copy | 0 / 50 visibles (55 activos) | cae (WhatsApp sin oferta en el copy) |
| Compra Express Online (`1019380191259044`) | CO | «Comprar guía en promoción desde WhatsApp» (guía de paneles solares, COP) | 27 / 27 pero **todas las creaciones entre 11-04 20:08 y 21:00 UTC** | **posible zombi / una sola fecha** (≥ 3 fechas no se cumple) → sin tarjeta |
| Marly Lactancia (`1213219015502585`) | ES | guía para destetar US$ 10 | 1 / 29 | < 4 |
| Atril Estudio (`1282575998279080`) | CO | creativo sin nombre de oferta («⭐ 4.9/5 Estrellas») + «La cocina del cuidado corporal natural» | 0 / 50 visibles (235 activos; los 50 son del 11-16 en adelante) | no identificable → «Para re-contar en la PC» |

## Gate de las que pasan (landing con Firecrawl)
- **Estudia Sencillo** — snapshot `1602531711645856` + landing `es.farmaciamapeada.com.br/farmacologia-v2`: Kit Farmacología Ilustrada = 8 módulos + 2 bonos en PDF de alta resolución, US$ 13 (tachado 91), pago único Hotmart, acceso inmediato por email. Filtro A: la landing cierra con «Moisés Santos, Farmacéutico y CEO de Estudia Sencillo» (foto y nombre) pero los anuncios son de marca, sin cara; el producto no se vende por él → pasa con reserva (decide Carlos). Filtro D: PDF ✅. Operador brasileño (dominio .com.br), «+11.000 estudiantes».
- **Mente Académica** — landing `ingenieriacivil200.lovable.app`: 200 mapas mentales en 10 módulos + 4 bonos, «material digital descargable», US$ 9,99 (tachado 29,99), pago único Hotmart, 7 d garantía; marca «Ingeniería Civil Visual», sin persona. Filtro D: PDF/imagen descargable ✅ (el catálogo es de Lovable pages por tema: trastornos, neuroanatomía, anatomía cardiovascular, informática, casos endocrinológicos).
- **Fichas Foto Pro** — snapshot `29504164675868692` + landing `fichas-foto-pro.quicklyguide.com`: pack de 108 fichas en 4 PDF (cámara + celular), US$ 14,90 (tachado 99), pago único, PDF al email; tienda Impultienda (`cdn.impultienda.ar`); sin persona. Filtro D ✅.
- **Magnus** — snapshot `1165203402729442`: «Kit Contabilidad Sin Enredos» = libro 1 (110 págs teoría) + libro 2 (ejercicios) + 2 bonos Excel, S/ 10, acceso por Google Drive, venta por WhatsApp. Test del copy: pasa (producto, precio y entrega escritos). Sin persona visible. La landing es `api.whatsapp.com` (no abre); no se le escribió.

## Alertas
- Estudia Sencillo: 8 de 21 anuncios de farmacología son del 11-20 (38 %); no llega a 70 % → sin «posible relanzamiento».
- ALL sobre Estudia Sencillo MX (`Sin Memorizar`): 841 en total con `ALL`; la oferta corre desde julio en BRL, con muchas copias apagadas (dónde ya se probó: ediciones en BRL de jul-ago y oct).

## Señales sin tarjeta
Ver bandeja. Pendientes de PC: Atril Estudio, Cuaderno de Medicina / Derecho / Psicología (nombre «APP»: landing no abierta, no se descarta), Mente Académica MX ES CL PE y Fichas Foto Pro MX CL PE.

## Cobertura
40 keywords × 5 países (ver Embudo). Ceros con `ALL`: mapas mentales nutrición (CO MX ES CL: cero activo; con ALL NutriMapa 10 + 7, Mente Académica 6-12, Nexora 6), fichas pediatría ES, guías oficiales fichas ES CL, fontanero manual (todas), bioquímica ilustrada ES.

Trampas nuevas: `kit herencia` = novelas, quizzes y regalos (cero infoproducto de herencia); `trámites jubilación` = asesorías y AFP; `por WhatsApp`, `solo hoy` = retail y clínicas; `guía completa` = 3.185-5.701 resultados, todo de hoy; `fontanero manual` = cero activo en los 5 países; `fichas ISO` mezcla fotografía (ISO de cámara) con normas ISO.
Nodos nuevos propuestos para la cola: `fotografia/fichas-camara-celular` (ES) y `mente-academica/biblioteca-lovable` (ES).

## Lo que no se pudo verificar
Antigüedad de ads ocultos tras el tope de 50 en Mente Académica y Atril Estudio; conteo por país de Mente Académica, Fichas Foto Pro y Estudia Sencillo fuera de CO/MX; precio y contenido final de Magnus (WhatsApp); web de la Biblioteca (403).
