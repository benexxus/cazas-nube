# ES · 2026-11-28 (sáb) · Modo B perforar — nodos `virgen` ES + 20 semillas

Resultado: **0 tarjetas.** Ninguna página pasó la vara (10+ sobrevivientes por oferta y país, gate). Conteos por API; snapshots con Firecrawl (`maxAge: 0`).
Reloj: «hoy» ≈ 2026-11-28; sobreviviente = creado hace 7+ días (corte ≈ 2026-11-21).

## Embudo
- **Etapa 0 (operadores, 5 filas ES):** Estudia Sencillo CO (50 visibles, tope; títulos conocidos: GLP-1, Farmacología Ilustrada, IECA/ARA II), Pautas Listas ES (50 visibles / 111, título conocido), Digi Aprende PE (31 activos, «+300 Mapas Ilustrados», conocido), Mente Académica MX (50 visibles / 390; títulos conocidos + «+300 Mapas Mentales de TI» = Informática 300), Fichas Foto Pro CO (26, conocido). **Sin SKU nuevo.** Sin conteo de ofertas conocidas (re-conteo de la PC).
- **Etapa 1:** 40 keywords × CO MX ES CL PE (ACTIVE, limit 50) en 4 subagentes Haiku. Las 200 búsquedas corrieron, pero **ningún lote devolvió la tabla completa** (lote 1: parcial con ruido; lote 2: 6 filas verificadas + lista de candidatos; lote 3: lista de candidatos sin conteos; lote 4: solo «costeo menú» completa). Se trabajó con lo verificable y se verificó cada candidato por `page_ids` (ver `log-nube.md`).
  - Propias (20, nodos virgen ES): acuario principiantes · peces acuario · ciclado acuario · acuario plantado · adiestramiento canino · educación cachorros · cuidado gatos · contabilidad básica · cuaderno contable · contabilidad emprendedores · seguridad higiene · manual BPM · carpeta cocina · fichas fotografía · fotografía celular · costeo menú · plantilla costos · plantilla inventario · finanzas constructoras · atlas peces.
  - Semillas (20, nunca usadas): garantía de 7 días · bonos incluidos · producto digital · formato digital · imprime en casa · recibes al instante · llega a tu email · pack de ebooks · 100 plantillas · plantillas listas · formatos editables · formatos en word · pensión IMSS · declaración anual SAT · facturación CFDI · crédito Infonavit · piscicultura tilapia · cuyes crianza · gallinas ponedoras · apicultura principiantes.
  - Ceros con ACTIVE (repetidos con ALL cuando el lote lo hizo): ciclado acuario CO/ES/CL, acuario plantado CL, atlas peces CO/MX/CL/PE (ALL: solo ruido), declaración anual SAT CO/ES/CL/PE (ALL: 5-8 ads, ninguno infoproducto), pensión IMSS CL (ALL: préstamos a pensionados), crédito Infonavit CL (ALL: 32 guías inactivas), piscicultura tilapia ES/CL (ALL: nada propio). Un cero en el paso 1 no dice nada del mercado.
- **Etapa 2 (paso rápido, `page_ids` + país):** 15 páginas.

## Cobertura: verificadas
| Página | page_id | País contado | Resultado (`sobrev. / activos`) | Veredicto |
|---|---|---|---|---|
| Fer Rendon (Costeo de Menú · Finanzas Constructoras · plantillas Excel) | `1977647735819349` | MX | 0 / ≥ 50 visibles (todos del 25-26 nov; 122 activos, tope 50) | **[gate: A marca personal]**: landing `ferrendonx.com/p/costeo-de-menu-2026`, código «FREDDY10», página = persona. Sin corte por oferta (el gate cierra antes). Solo apareció en MX |
| Aprende Profesional | `1446593095195719` | PE | 50 visibles / 62; 26 de 50 con 7+ días, repartidos en ~25 títulos distintos («54 fichas…», SKU por tema) | **[gate: WhatsApp]**: snapshot abierto, `wa.me/12137860982`, «Escribe por WhatsApp» (+ `aprendia.shop`). Red AprendIA (ver nodo `fichas-visuales-aprendia`) |
| Aprende con Guías Profesionales | `1380966491766673` | MX · PE | MX 50 visibles / 350; PE 50 visibles / 388; todos del 21-28 nov (los 50 más nuevos) | **[gate: WhatsApp]** (mismo `wa.me`, snapshot de «Reparación de packs de litio · Edición Perú»). Portafolio de SKUs; no hay una oferta que pase |
| Mente Académica (Informática 300) | `1239880759219492` | MX | 50 visibles / 390; títulos ya conocidos; sin corte (oferta conocida → re-conteo en PC) | sin cambio |
| Psico Recursos | `1376516648885799` | CO | 2 / 2 (Hotmart, «Kit de 10 Formatos Editables para Psicólogos»; 14-nov) | < 4 |
| Tu Abogado Virtual | `617985411409450` | MX | 0 / 4 (30 formatos jurídicos $149 MXN + «Divorcio en línea» servicio; 27-nov) | < 4 |
| Seguridad y Salud Ocupacional y Medio Ambiente | `108273737689362` | PE | 3 / 3 (SG-SST pack documental, «archivos 100 % editables») | < 4 |
| Contabilidad Fácil Colombia | `1485870234602161` | CO | 0 / 7 (21-26 nov, «Descárgalo aquí») | < 4 |
| Ana Laura «10 guías visuales» (acuario) | `114860084961404` | CO | 0 / 3 (BRL, 27-nov); apareció en CO MX ES CL PE con 2-3 ads | < 4 |
| Diagnóstico Express | `1372065712666261` | PE | 0 / 9 (25-26 nov; «Una falla por página» y «+120 diagnósticos de aire split»; USD) | < 4 (nueva, tester) |
| Lanna Ribeiro | `1466459413209583` | CL | 0 / 1 («+300 mapas mentales para aprender inglés») | < 4 |
| Novika | `1394511833743138` | CO | 1 / 9 (moldes de costura PDF, $10.000-20.000 COP) | < 4 |
| Derecho Claro Digital | `1496957090161174` | ES | 0 / 5 (todos del 27-nov; «Todo el Código Civil, ordenado») | < 4 (nueva) |
| Reliant Offers | `1359074290630093` | MX | 3 / 3 (curso grabado «Velas y jabones» US$ 35: manualidades, nicho excluido; no se sigue) | ignorada |
| Valentina Herrera | `1250106704860994` | CL | 0 / 2 (BRL, «+1.500 recursos listos para imprimir») | < 4 |

Candidatos listados por los subagentes y **no verificados** (solo señal de existencia): Pack de Plantillas `108486535276295`, Silvia Menéndez `111642171338135`, Sublipaquete `1329911963546171`, Tu SuperPack Digital `539309959256552`, Calvyne store `791031190770866`, RayosPedia `101412365114027`, Mini Genios `739087692611672`, Higiene y Seguridad Latinoamérica `564187653627376` (6 ebooks), Gestión Profesional con Excel `961233043748737`, ExcelentesPlantillas `506094592589095`, Nexo Digital `1395478350324653`, Universo Visual `364045540126936` («60 diseños para tu acuario», CL, solo ALL), Cuidando en Casa `1344750005393443` («100 proyectos de acuarios», CL, solo ALL), Packs Pro `1191268424076265`, Guía digital 2026 `1477822395412407`, Aprende Ya: Guías Aprendia `1288181344388955` (AprendIA, WhatsApp). Los de recetario (Mundoebook, Deli Postres, Mi Pan Sin Gluten, Recetas de Oro) se ignoran por el nicho excluido.

## Embudo (resumen)
40 keywords barridas · ~60 páginas de infoproducto aparecieron en las tablas · 15 verificadas (paso rápido) · 0 completas (nadie llegó a 4+ sobrevivientes fuera de las del gate) · 3 `firecrawl_scrape` de snapshots (Aprende Profesional, Aprende con Guías, Fer Rendon).

## Molde en otros mercados
«Plantilla de costeo de menú» = Fer Rendon MX (solo MX); «molde de costura PDF» = Novika CO (1 / 9). Sin señal de molde con 10+.

## Dónde ya se probó y falló / patrones
- Acuario: el molde «100 proyectos de acuarios» tuvo operadores en CL (Cuidando en Casa, Universo Visual, Packs Pro) hoy sin activos; Ana Laura (0 / 3) es el único activo con guías visuales.
- Seguridad e higiene: Negocio en Regla y Cocina en Regla (nodo `seguridad-higiene-carpetas`) siguen activos en MX en las tablas; no se re-contaron hoy (re-conteo agendado 2026-11-29).
