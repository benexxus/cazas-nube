# Caza automática — ESTE · huella (A) · 2026-11-21 (sábado, corrida de las 14:12 CET)

Mercado: RO PL CZ HU (cada keyword solo en el país de su idioma). Reloj: hoy ≈ ts 1795267100 (14:12 CET); sobreviviente = `ad_creation_time` ≤ 1794662299 (7+ d) y activo; en tandas justas se miró también `ad_delivery_start_time`. Evidencia: API + `firecrawl_scrape` de snapshot y landing (funcionó, `maxAge: 0`, `waitFor: 4000`).

## Shortlist
Dos ofertas pasan la vara de 10+ por oferta y país, ambas del mismo patrón (operador latino con landing en `*.impultienda.ar`, PDF, WhatsApp no, checkout propio, pago único):
1. **Atlas Terapeutic Vizual** (RO, `1408033785736088`): ≥ 23 sobrevivientes / 72 activos (piso, tope 50 con cola oculta).
2. **Anna Majewska — «120 Zajęć IPET»** (PL, `1463210366871740`): ≥ 15 / 79 activos (piso, tope 50).

## Veredicto
Pasan ambas (gate OK con salvedades anotadas en cada tarjeta). Par fuente → destino: RO y PL son destino y fuente; ver «Qué hacer» de cada tarjeta. Score ≤ 2/4 las dos (longevidad ~10-18 d, no 45+; volumen < 50).

## Embudo (NUBE.md §7)
- Etapa 1: **40 keywords** barridas, 4 subagentes Haiku (uno por idioma, 10 keywords cada uno, un país por keyword, `ACTIVE`, `limit 50`; cero → `ALL`). Todas las keywords salieron nunca usadas (grep en cola, semillas-usadas y RAW).
  - RO: `ghid pdf`, `ghid practic`, `ghid ilustrat`, `hărți mentale`, `acces imediat`, `caiet de exerciții`, `rezumat pdf`, `tabel excel`, `hărți mentale anatomie` (0 incluso con ALL), `ghid divorț`.
  - PL: `poradnik pdf`, `mapy myśli`, `natychmiastowy dostęp`, `arkusz excel`, `ilustrowany poradnik`, `ściąga pdf`, `notatki pdf`, `fiszki do druku`, `elektryk poradnik`, `szkolenie psa poradnik`.
  - CZ: `průvodce pdf`, `myšlenkové mapy`, `okamžitý přístup`, `excelová tabulka`, `ilustrovaný průvodce`, `tahák pdf`, `výpisky pdf`, `kartičky k tisku`, `autoškola testy`, `elektrikář příručka`.
  - HU: `pdf útmutató`, `gondolattérképek`, `azonnali hozzáférés`, `excel táblázat`, `illusztrált útmutató`, `puska pdf`, `jegyzetek pdf`, `tanulókártyák`, `jogosítvány tételek` (cero activo; `ALL` solo trae empleo y autoescuelas), `villanyszerelő útmutató`.
- ≈ 300 páginas distintas salieron en las tablas; 10 verificadas (paso rápido, una consulta por `page_id` + país):

| Página | `page_id` | Dónde apareció | Cohorte / activos | Paso |
|---|---|---|---|---|
| Atlas Terapeutic Vizual | `1408033785736088` | solo RO (las 14 ads con `search_terms` en PL/CZ/HU son los mismos ids que RO) | **≥ 23 / 72** RO (6 + 6 + 6 + 5 visibles; 22 más viejos ocultos por tope 50; ALL = mismo set) | completo |
| Anna Majewska (120 IPET) | `1463210366871740` | solo PL | **≥ 15 / 79** PL con `search_terms: IPET` (el total de la página son 202; 50 visibles, todos de ≤ 7 d sin el corte) | completo |
| Digital Books | `1460770633775833` | RO (≈ 59), PL 44 | PL 10 / 44; RO 1 / 50 visibles + ~9 ocultos | snapshot: **recetario** (150 finger food) → nicho excluido, ignorado |
| Next Skill Studio | `148144215050419` | solo PL | 0 / 25 (todo del 20-21 nov, lote de hoy) | rápido |
| Coach Eva Natural | `149176424947116` | solo RO | 0 / 20 (todo del 20-21 nov) | rápido |
| Escuela Saludable | `100723261734448` | HU 30-46, CZ 4, RO 1 | HU 2 / 46 (dos ofertas sueltas); la oferta principal «33. kártya: hideg víz» 0 (tanda del 13-21 nov) | rápido |
| Joanna Zawadzka | `1446090091918778` | solo PL | 0 / 18 (un solo creativo, 16-17 nov: cumple 7 d el 11-23/24) | rápido |
| Fotó Puska | `1414912408371094` | solo HU | 0 / 20 (el más viejo del 14-nov, madura hoy; 9 del 14-16 nov cumplen 7 d el 11-23) | rápido |
| Știința Bunicilor / Textomat | `1385991297929264` | solo RO | 0 / 11 (14-16 nov) | rápido |
| ConocimientoDigital | `1200774293118311` | solo CZ | 0 / 10 (lote del 18-20 nov) | rápido |

- No contadas (aparecieron con volumen, sin paso rápido por tope de 10): Fenix Library `1455853117614278` RO 15 / HU 9+2 (ya en bandeja, molde de certificaciones en imágenes de EN/IT; país nuevo RO/HU: señal), Mesa Ligera CZ 22, Ready Resources RO 23 (ya vigilado), Printora PL 12, AI Sports CZ 25 (canal de tips/suscripción: no infoproducto), Handy Ebooks CZ 12 y Margit Kovács/Imagina y Crea HU (crochet: manualidades, ignoradas), Nora Holm CZ 14 / HU 9 / RO 5 (libros físicos «3 por 1»), Digital Master HU 10, Handy Guides RO 5, Impulso Digital RO 5 / PL 2 (300 mapas de enfermería).

## Verificación de las dos que pasan

### Atlas Terapeutic Vizual (RO)
- Sobrevivientes: 23 por creación (1794607405-1794607425 ×6, 1794525587-1794526293 ×6, 1794434813-1794436142 ×6, 1794351710-1794353756 ×5); por entrega 20 (3 de la tanda más joven empiezan a entregar el 14-nov, después del corte). Más 22 ocultos de ≥ 18 d (el ad más viejo visible con `search_terms` es del 2026-11-03, 18 d). Un solo `page_id`, una sola oferta (el título del ad es siempre el nombre de la página; el copy del ad sí nombra el producto).
- Snapshot (ad `1895120384735501`, empezó el 14-nov): «120 de hărți mentale ale emoțiilor… PDF gata de tipărit, acces pe viață, garanție de 7 zile», CTA → `atlasterapii.impultienda.ar`.
- Landing (`atlasterapii.impultienda.ar`, `noindex`): «120 de Hărți Mentale ale Emoțiilor» (240 págs, 12 áreas de 10 mapas), 32 metáforas visuales, 12 láminas comparativas, 12 flujogramas, 4 bonos (12 mapas de enfoques terapéuticos, 6 escalas, documentos psicológicos editables, actualizaciones); precio **US$ 19 pago único** (tachado 47), checkout `atlasterapii.impultienda.ar/checkout`, garantía 7 días. Texto de la landing menciona «250+ mapas» arriba y 120 abajo (inconsistencia del operador).
- Filtro A (marca personal): ninguna. Página = nombre de producto, sin firma, sin rostro, sin «sobre mí»; texto con imágenes de mockup alojadas en `recursos-pdf-hub.github.io` (CDN del operador). Referencias a Beck, Young, Linehan, Hayes, Bowlby, Gilbert con descargo de no-afiliación.
- Filtro B (embudo): landing de venta con checkout; OK. C: front-end único con bonos digitales, sin back-end visible. D (entregable): PDF → OK.
- Observaciones: moneda de los ads ARS y landing en `.ar`: operador argentino que localiza a rumano; el nombre del producto y la landing salen de la misma plantilla de la red Impultienda (como `120zajec.impultienda.ar`, `stol-pelen-przekasek.impultienda.ar` de Digital Books). Nicho = psicología/salud mental (público terapeutas y autoconocimiento), no está excluido.
- Molde en otros mercados: Escuela Saludable HU (tarjetas de sistémica familiar «60 sistemás kártya», 30-46 act., 0 cohorte), Mentális Zavarok Térképe HU / Harta Tulburărilor RO (ya operadores en la cola). No se midió Atlas en ES/PT/IT (no es de la sesión).

### Anna Majewska — «120 Zajęć IPET» (PL)
- Sobrevivientes: 15 visibles con creación ≤ 1794662299 (todos de la tanda del 11-nov, 1794423303-1794423345) con `search_terms: IPET` + `page_ids` + PL; entrega ≤ corte también (1794475xxx-1794522878). El total es piso: 79 estimados, 50 visibles, 29 más viejos ocultos. Mismo producto en todos los creativos («120 gotowych zajęć», «Nic do zamawiania», «Karta zmiany planu»). Aparte, la página corre otro SKU hoy (25 «muzykogramów» a 29 zł, 21-nov, 0 cohorte) y un «Pakiet Kompletny».
- Snapshot (ad `1347503477392677`): «120 gotowych zajęć dla nauczycielek wspomagających… 5 obszarów IPET… Natychmiastowy dostęp. Płacisz raz… BLIK lub karta», CTA → `120zajec.com`.
- Landing (`120zajec.com`): dos paquetes, **29 zł** (solo 120 fichas, tachado 89) y **59 zł** (con 6 bonos: plantilla IPET, 20 AAC, hoja de seguimiento, kit sensorial, guía de padres, calendario anual), checkout `120zajec.impultienda.ar/o/podstawowy` y `/o/kompletny`, upsell de salida (bonos por 10 zł más), garantía 7 días, PDF alta resolución a e-mail. Pie: **BALTASCA LLC, Hialeah FL**, mail `ebooksgrowthcontacto@gmail.com`.
- Filtro A: el nombre «Anna Majewska» firma la garantía y es el nombre de la página y del handle `annamajewska.nauczycielka`, pero la landing no trae foto, bio ni credencial; los testimonios son capturas con cuentas de Instagram de otro idioma (`pfreitasm_pl`, «Lucyna Da Rocha») y la empresa es una LLC de Florida: parece una **persona de fachada de una red de operadores, no una marca personal con audiencia**. Salvedad explícita: Carlos debe mirar la página `facebook.com/annamajewska.nauczycielka` (no abierta) antes de decir `Idea`.
- B/C/D: embudo de venta con checkout y upsell; front-end con bonos, sin back-end; entregable PDF. OK.
- Contexto: IPET = Indywidualny Program Edukacyjno-Terapeutyczny (educación especial en Polonia); público: nauczyciel wspomagający, terapeuta, rodzic.

## Lo que no pasó ni va a señal
- Digital Books (recetario) y Margit Kovács / Handy Ebooks / Imagina y Crea (crochet): nichos excluidos, ignorados.
- AI Sports CZ (25 ads «canal privado») y Coach Eva Natural (lote de hoy sin cohorte; copy de guía no identificado, landing no abierta).

## Cobertura
Las 40 keywords de arriba (4 subagentes) + 25 consultas propias: 10 pasos rápidos, 4 pasos completos (Atlas ACTIVE y ALL RO; Atlas PL/CZ/HU; Atlas `search_terms`; Digital Books PL; Anna `search_terms: IPET`) y 5 `firecrawl_scrape` (3 snapshots, 2 landings; 1 scrape fallido por id mal escrito, sin consecuencias). Diacríticos (`hărți`, `myšlenkové`, `ściąga`, `gondolattérképek`, `okamžitý`) funcionaron sin problemas en los cuatro idiomas.
