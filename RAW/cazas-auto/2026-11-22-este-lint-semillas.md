# Caza ESTE · domingo 2026-11-22 · lint de la cola + embudo con semillas

Sesión ESTE (RO PL CZ HU), una sola corrida del día (06:07-~06:50 Europe/Madrid). Conector de Meta presente. Sin fallas de git.

## Lint de la cola (nodos ESTE)
- Nodos ESTE: `profesiones/material-de-clase-listo/este`, `salud-mental-visual`, `.../educacion-especial`, `fotografia-celular`, `herencia-y-papeles` (tramo Este). Todos tocados entre 2026-11-20 y 11-21: ninguno sin tocar > 30 días, ningún 🟡 vencido.
- Re-mediciones con fecha cumplida hoy: ninguna (la primera es 2026-11-24: Joanna Zawadzka, Fotó Puska, Știința Bunicilor). Sin hallazgos.

## Embudo
### Etapa 1 — 40 semillas nunca usadas (grep en cola, semillas-usadas y RAW: 0 apariciones), 10 por idioma, 4 subagentes Haiku, un país por keyword
- **RO:** descărcare imediată · modele editabile · pachet digital · fișe de recapitulare · șabloane editabile · planner printabil · checklist mutare · dresaj cățeluș · buget familial · ghid acvariu
- **PL:** gotowe szablony · planer do druku · szablony canva · ćwiczenia pdf · zestaw szablonów · kompletny poradnik · checklista przeprowadzka · tresura szczeniaka · budżet domowy · akwarystyka poradnik
- **CZ:** hotové šablony · pracovní sešit · plánovač k tisku · digitální balíček · sada šablon · příručka pdf · checklist stěhování · výcvik štěněte · rodinný rozpočet · akvaristika průvodce
- **HU:** kész sablonok · feladatlapok · munkafüzet pdf · nyomtatható planner · sabloncsomag · letölthető pdf · költözés checklist · kiskutya nevelés · családi költségvetés · akvárium útmutató
- Ceros activos (repetidos con ALL): RO planner printabil, dresaj cățeluș, buget familial, ghid acvariu; PL checklista przeprowadzka, akwarystyka poradnik; CZ checklist stěhování, výcvik štěněte, akvaristika průvodce (cero también con ALL); HU nyomtatható planner, költözés checklist, kiskutya nevelés, akvárium útmutató. Los 4 lotes Haiku devolvieron la tabla sin falla.
- Ruido: `pachet digital` (RO) = autos usados; `budżet domowy` (PL) = bancos/fotovoltaica; `családi költségvetés` (HU) = constructoras; `ghid acvariu` (RO) = viajes. Ver trampas en la cola.
- Salieron ~330 filas de página; ~45 parecían infoproducto.

### Etapa 2 — 10 páginas nunca vistas (grep por page_id en cazas/ y RAW/: 0 apariciones salvo Edu Digital, solo como señal NL del EU del mismo día), paso rápido
Corte de 7 días: ahora = 1795324354 (2026-11-22 ~06:10 CET) → ad_creation_time ≤ 1794719554 (≈ 2026-11-15). Todos con `ACTIVE`.

| Página (page_id) | País | Sobrev. / activos | Nota |
|---|---|---|---|
| Veronica Rose `1342395585621504` | HU | 2 / 21 | los 2 son anuncios de «Systemische Toolkit» en neerlandés; la oferta húngara «60 kész feladat» 0 (todo del 20-21) |
| Miłosz Sadowski `1340709525788261` | PL | 4 / 22 (6 con las 2 de «Niezbędnik studenta») | multi-SKU (historia, técnica, 120 diagnósticos de splits, 1000 GIF); la oferta de historia 4 / 6 → vigilancia (portafolio), pago en EUR |
| Knihovna dovedností `1451064928086229` | CZ | 0 / 6 | todo del 20-nov |
| Paul Miller `547086365144888` | CZ | **14 / 28** | oferta única → paso completo |
| Muzica pe înțeles `1481694865025481` | RO | 0 / 3 | todo del 22-nov |
| Edu Digital `100629922105479` | RO | **15 / 38** | → paso completo |
| Złoty Tydzień `1497253373462050` | PL | 0 / 8 | todo del 21-nov (planillas de presupuesto en Google Sheets) |
| Trade Pro Kit `1437484146115003` | HU | 0 / 17 | todo del 20-21 nov (misma fábrica que ProKit/Edulabs) |
| Elektronika w schematach `1086864684514383` | PL | 0 / 3 | del 20-nov |
| So Follow `139515539234030` | PL | 0 / 14 | todo del 17-nov, cumple 7 d el 11-24 |

Páginas del barrido no contadas por ser nicho excluido o fuera de formato: Eszter tanító néni (HU, 17 ads) e Ioana Radu (RO, 10 ads) = dislexia infantil, Spokojny Dom (PL) = ADHD infantil → zona neurokids, ignoradas; Lovely Crafts, Emilia Zabala, Biblia przez zabawę = manualidades/religioso, ignoradas; Escuela Saludable (HU 30, CZ, RO), Studio Facile (RO CZ PL HU), Hravá příprava, Ready Resources, Edulabs, ProKit, Fenix Library, Digital Books, Charlotte Miller, Next Skill Studio: ya vistos o cazados, sin recontar. Base Digital «Kit Contabil Practic 2027» RO (3 ads, 20-nov) = molde del Kit Comptable/Contabile ya cazado, sin cambios relevantes.

### Paso completo

**1. Edu Digital — «Mintea celor 6 mari genii» (6 PDF: Platon, Aristotel, Nietzsche, Freud, Lacan, Jung; 388 págs)** · page_id `100629922105479`
| País | Apareció en tablas de subagentes | Sobrev. / activos (ACTIVE) | Notas |
|---|---|---|---|
| 🇭🇺 HU | no (la encontró el recuento por page_id) | **27 / 28** | lotes del 5, 9, 11 y 12 nov; el más viejo 17 d (2026-11-05); todos «A 6 legnagyobb géniusz elméje» |
| 🇨🇿 CZ | no | **15 / 34** | lotes del 9 y 12 nov («Mysl 6 největších géniů») |
| 🇷🇴 RO | sí (descărcare imediată: Edu Digital 5) | **15 / 38** | lotes del 9 y 12 nov («Mintea celor 6 mari genii»); el más viejo 13 d |
| 🇵🇱 PL | no | 0 / 6 | todos del 18-nov («Umysł stratega · 6 książek w PDF») |
- Reloj de entrega: HU, CZ y RO quedan muy por encima de 10 con ambos relojes; solo la tanda del 12-nov de HU (5 ads, entrega ≥ 1794717037) roza el corte y aun sin ella HU = 22.
- Gate: A (marca personal) → pasa: página «Edu Digital», sin rostro ni nombre en landing ni en el link a `facebook.com/edudigitalarg2` (operador de la red Impultienda con ARS en el nombre de página); la landing dice «EduDigital România». B (embudo) verificado con Firecrawl: ad → `edudigital-ro.impultienda.ar` → `/checkout`, precio US$ 22,99 (tachado 45,99), PDF, garantía 7 d, plazo «preț de lansare». C (back-end): no se ve upsell. D (entregable): 6 PDF de ≈ 60+ págs → producible. Marketing extra: la landing de otros idiomas `en.mentisclassics.com` y `strategist.mentisclassics.com` apareció en el creativo de la tienda (mismo producto en inglés: no abierto).
- Originalidad: filosofía y psicoanálisis «explicados simple» sobre autores de dominio público, no marca ni persona. Contenido ajeno a nichos excluidos.
- Antes: el EU del mismo día anotó la página como NL «6 PDF-boeken, chicos y nuevos» (señal); el ESTE confirma tres mercados con 15+ y 27 en HU. Molde en otros países: NL (EU), PL 0/6; no se buscó DE/IT/FR/ES.
- Score: ① 45+ d: no (17 d) · ② 50+ en un país: no (27) · ③ duplicación 10+: sí (lotes de 10 ads iguales) · ④ hueco de arbitraje: no medido → ≤ 2/4 (observar).

**2. Paul Miller — «Příručka ztracených dovedností» (246 habilidades ilustradas + 2 libros de regalo)** · page_id `547086365144888`
| País | Apareció en tablas | Sobrev. / activos | Notas |
|---|---|---|---|
| 🇨🇿 CZ | sí (příručka pdf: Paul Miller 14) | **14 / 28** | lotes del 7 nov (8) y 12 nov (6); 3 fechas (7, 12, 19 nov); el más viejo 15 d |
| 🇷🇴 RO | no | 8 / 14 | «Manualul abilităților pierdute», lote del 10 nov (8); ya cerca |
| 🇭🇺 HU | no | 8 / 14 | «Az elfeledett tudás kézikönyve», lote del 8 nov (8); los 6 del 14-nov quedan fuera con el reloj de entrega |
| 🇵🇱 PL | no | 0 / 0 | sin anuncios activos |
- Gate: A: «Paul Miller» es solo el nombre de la página; la landing no trae foto, bio ni firma (garantía «Dědovo slovo»). B verificado con Firecrawl: snapshot → `dovednosti.digitalnivedeni.com` → checkout `dovednosti.impultienda.ar/o/prirucka-dovednosti-cesko`; paquete 3 en 1 por **449 Kč** (tachado 1 499 Kč), cuenta regresiva «15 min» y «hoy domingo 22 de noviembre» (urgencia de plantilla). C: libros 2 y 3 incluidos de regalo («Spíž, která se nikdy nevyprázdní», 60 técnicas de conservación; «Amišské tajemství», 60 recetas de pan, manteca y quesos): el 2º y el 3º rozan recetario (nicho excluido) pero el producto principal es el manual de habilidades. D: PDF producible. 
- Dice 246 habilidades en el anuncio y «220+» en el titular de la landing.
- Score: ① no (15 d) · ② no (14) · ③ sí (14 anuncios con el mismo título) · ④ no medido → ≤ 2/4.
- Moldes parecidos en otros países: no buscados (el tema «habilidades perdidas / autosuficiencia» tiene versión en inglés por probar en 🇺🇸 🇬🇧).

## Cobertura
- Keywords: 40/40 barridas (4 subagentes × 10, ~6 por idioma de huella y 4 de molde × tema). Países: un país por keyword (RO, PL, CZ, HU).
- Páginas verificadas: 10 (paso rápido) y 2 con paso completo (4 países cada una). Firecrawl: 2 snapshots y 2 landings (Paul Miller, Edu Digital) sin falla.
- No se llegó a: contar Alma Artesana RO (planner de presupuesto 79 lei, 9 ads con `ALL`, cero activo), Estelle Crawford PL (guía de enfermería, 3 ads), Aula Mater 2 PL (lecciones de historia, 1-5 ads), DomoweStory PL (7 ads, actividades para niños), Poradnik Kierownika Budowy PL (5 ads), Klub moderního psa CZ (curso 197 Kč, 20 ads), Materiály od Dominči CZ (RVP, 2 ads), BJJ příručka CZ (3 ads), Profe Pack / Edulabs HU, Kasten feladatok HU, Note Női Energia HU (3 ads). Quedan para el próximo barrido de ESTE.
- Altas a la cola: `filosofia-psicoanalisis-pdf` (Edu Digital) y `supervivencia-autosuficiencia` (Paul Miller), ambos `virgen`.
