# BR · lun 2026-11-23 · B perforar + 20 semillas · `profesiones/examenes-y-oposiciones` (slice BR: ENEM, CNH, bancas, PM/bombeiro)

Hora de la corrida: 03:33-04:xx Europe/Madrid. Decisión de nodo: los dos nodos `virgen` de BR (`ar-condicionado-whatsapp`, `reforma-tributaria-visual`) los tocó BR ayer (11-22) → se saltan (< 7 d). Se perfora el `superficial` más viejo con mercado BR: `profesiones/examenes-y-oposiciones` (BR: faltaban ENEM, bancas, CNH).

## Embudo
- **Etapa 1:** 40 keywords en 4 subagentes Haiku (`countries: ["BR"]`, `ACTIVE`, `limit 50`), todas devolvieron resultados (ninguna en cero → no hizo falta `ALL`). El lote 3 asignó las filas a la keyword «por contenido» (la API no repite la keyword).
  - 20 propias (B examenes BR): resumo ENEM · mapas mentais ENEM · redação ENEM · simulado ENEM · prova teórica CNH · legislação trânsito · autoescola apostila · questões CESPE · questões FGV · apostila PM · concurso polícia · apostila bombeiro · concurso INSS · magistério concurso · apostila TJ · concurso prefeitura · resumo Direito Constitucional · OAB segunda fase · técnico enfermagem concurso · apostila SEFAZ.
  - 20 semillas, tal cual: huellas R$ 27 · R$ 47 · imprimível · kit digital · R$ 17 · R$ 29 · R$ 9,90 · modelos editáveis · caderno de exercícios · material pronto · entrega imediata · baixe agora; molde × tema orçamento familiar · sair das dívidas · currículo modelo · barbeiro apostila · manicure apostila · tatuagem iniciante · inventário herança · gestante checklist.
- **Etapa 0 (ronda de operadores, 2 filas BR):** Packs & Moldes Pro `1227856100409706` → 29 / 29 (3 tandas 27-ago, 06-sep, 14-sep), solo «Manual do Eletricista Residencial», sin SKU nuevo. Guedes Serviços `1315091175012794` → 8 / 24 (misma cifra que 11-22), solo «Apenas 10 reais»; la tanda del 11-18/19 cumple 7 d el 11-25/26 → re-conteo 2026-11-25 sigue vigente.
- **Etapa 2:** 18 páginas con 1+ pasada (todas `grep` limpio salvo Tutoria EAD, ya vista el 11-20). Paso rápido a 11 páginas; paso completo a 1.

## Cobertura (por página verificada, solo apareció en 🇧🇷)
| Página (`page_id`) | Oferta | cohorte / activos (🇧🇷) | Veredicto |
|---|---|---|---|
| **Mapas da Guarda** `1281225235079752` | «416 mapas do concurso GCM Santana» / «Edital da Guarda de Santana em mapas» | **34 / 48 por creación · 29 / 48 por entrega** (`< 50`, manda la API) | **pasa** → tarjeta |
| Mapas da Guarda (misma página) | Guarda de Campinas «290 mapas» (11 ads, lote 11-22) · Guarulhos (3 ads, 11-14) | 0 / 11 · 0 / 3 | portafolio por municipio; re-conteo 11-29 |
| ENEM PROVA MAPAS Mentais `1316379811568954` | «Revisão Final ENEM 2026 R$ 17,90» + «Kit 22 Mapas Mentais da Prova» | 21 / 21, **una sola fecha de creación (04-nov, 2,5 h)** | «posible zombi» (< 3 fechas); además atado al ENEM 2026 ya rendido. Sin tarjeta; embudo no abierto |
| Fabiana Tavares `815686988302921` | «220/240+ Páginas Ilustradas» | tope 50 (82 est.) → corte «220 Páginas Ilustradas» 0 / 16 (más viejo 11-20, 3,3 d) | 0 sobrev.; tanda 11-20/22. Re-conteo 11-30 |
| Mapas e Guias `1398408656682325` | OAB 2ª fase «Treine a peça…» / «Pare de errar…» | tope 50 (81 est.) → corte «Pare de errar» 0 / 17 (más viejo 11-20) | 0 sobrev.; re-conteo 11-30 |
| Mapa com Prova OAB `1018524351351298` | «Os 25 temas que a FGV repete» | 0 / 8 (más viejo 6,1 d) | señal; re-conteo 11-30 |
| Brabo Editora `396005163592042` | «Apostila Mestre em Questões TJ-SP» (R$ ?) | tope 50 (137 est.), los 50 son de 11-20 en adelante; corte «Mestre Questões» devuelve los mismos 50 | **«Para re-contar en la PC»** (piso 0 < 10) |
| Felipe Resumão `759042973953984` | apostilas R$ 19,90 por concurso (Banestes, TJ-SP, PRF, PM-SP, PC-AC, IBGE, Polícia Penal PE, DPE-AM) | tope 50 (652 est.), todo de 11-20/21 | portafolio multi-SKU, sin oferta con cohorte; señal |
| Psi.se `101207292972176` | Kits Freud/Lacan/Jung/TDAH (docs de psicología R$ 47) | 0 / 8 (más viejo 11-20) | señal |

Pasos rápidos omitidos por tiempo y por no ser infoproducto claro o por ser de 1-5 ads: Tudo Para Polícia (33 ads, «Do Zero a Policial Rodoviário Federal» = curso), Editora Amaral (15, lead por comentario), Mapas de Primeiros Socorros (14), Léo Lima, Rogerio Pereira, Mapeia Estudos, ONE SHOP, Primeira venda, Arlindo Beloni, Julia Oliveira.

## Mapas da Guarda — evidencia
- Página fantasma «Mapas da Guarda» (FB `61594728811538`), landing `gcmsantana.abstratainc.com.br` (dominio `abstratainc`). Footer: «Material de estudo independente… sin vínculo con la Prefeitura / Guarda / IDCAP». Sin persona ni cara; testimonios de WhatsApp de la «mesma coleção» de Guarulhos → **Filtro A pasa** (landing, footer y FAQ leídos con Firecrawl; no hay redes personales).
- **Filtro B/C/D:** landing de venta directa; checkout Kiwify (`pay.kiwify.com.br/jSz7LZe` Plano Básico R$ 17,90 y `/jPktfxv` Plano Completo R$ 27,90, ambos «de R$ 47 / R$ 192»); front-end se sostiene solo (sin back-end ni mentoria); entregable = **416 mapas mentais en PDF** (51 de leis da Guarda, 95 português, 34 mat/lógica, 10 história AP, 11 geografia AP, 57 legislação especial, 50 constitucional, 29 administrativo, 68 penal, 11 DDHH) + 5 bonos (checklist verticalizado, raio-X do edital, roteiro de estudos, cadernos de revisão ativa, mapas em texto para imprimir). Todo producible → ✅.
- Snapshots abiertos: `1101789806058975` (empezó 30-oct) y `1682193059916620` (empezó 15-nov): video + texto de copy completo con prova IDCAP 17/01/2027, inscripciones hasta 09/11.
- Zombis (API): 7 fechas de creación distintas entre los 34 sobrevivientes (27-oct, 29-oct, 03-nov, 05-nov, 08-nov, 13-nov, 17-nov…), y 11 + 3 ads de los últimos 30 días → no es zombi. Longevidad máxima ~28 d (primera tanda 27-oct). Dos relojes: por creación 34, por entrega 29 → ambos ≥ 10.
- **Alerta de relanzamiento:** la tanda de Campinas (11 ads, 22-nov) tiene otro título; tamaño 11 / 34 = 32 % < 70 % → sin alerta.
- `ALL` ≈ `ACTIVE` (48 / 48): la API no trae ofertas apagadas (NUBE §4); apagados solo se confirman en la web.
- Salvedades: (1) producto **atado a un concurso municipal con fecha** (prova 17-ene-2027; inscripciones cerradas 09-nov); modelo replicable por municipio (Guarulhos, Santana, Campinas). (2) la API no ve apagados.

## Señales extra del barrido (sin verificación completa)
- Rogerio Pereira `102294775997398`: «+120 Mapas Visuais de Planejamento Sucessório» (1 ad, inventário/herança, molde cuaderno ilustrado) — vigilar.
- Vanguarda Docs `1344384498755738` (kits de plantillas para inmobiliarias), Ederson Deda `137773240137527` (laudos PGR/LTCAT editáveis, 4), MUST University `275604999546664` (modelos NR-1, 3 + 3), Verônica Fragoso `106119094230511` (200+ documentos editáveis, 2): pocos ads, sin cohorte.
- Ruido: `entrega imediata`, `baixe agora` (apps, short-dramas, supermercados), `R$ 27/47/17/29/9,90` (retail, autos usados, supermercados), `currículo modelo` (vagas), `inventário herança` (abogados), `barbeiro/manicure/tatuagem` (academias), `sair das dívidas` (DramaBox ×40), `gestante checklist` (clínicas). Nichos excluidos ignorados (recetarios: Natal Lucrativo, A Casa Moderna, Ebook Digital, Pet Comilão; religioso: Biblia 360, Pratico & Digital).

## Trampas nuevas
- `entrega imediata` · `baixe agora` (BR): sin infoproducto (apps, short-dramas, retail); usar entregable + tema.
- `R$ 27` / `R$ 47` / `R$ 17` / `R$ 29` / `R$ 9,90` (BR): 50 resultados de retail y autos usados, solo leen nombres de página.
- API con `page_ids` + `search_terms` repetidos en una fábrica con una sola oferta visible (Brabo Editora): el corte no baja de 50; va a «Para re-contar en la PC».

## Molde en otros mercados (Etapa 2.4)
No se corrió búsqueda de molde en otros países (BR es la única sesión de su idioma); el molde «un municipio = un edital en mapas mentais» ya aparece en 🇮🇹 (Concorsi in Mappe, tarjeta del 11-20) → anotado como destino sugerido en la tarjeta.

## Nodos / altas
Sin nodo nuevo (el tema entra en `profesiones/examenes-y-oposiciones`). Ronda de operadores: alta de Mapas da Guarda en la fila BR.
