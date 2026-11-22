# EN 2026-11-22 (dom) · lint de la cola + embudo con 40 semillas

## Lint de la cola EN
- Ningún nodo EN sin tocar > 30 días (el programa arrancó el 2026-11-20). Ningún 🟡 vencido: `idiomas/mapas-visuales` vence 2026-11-27; re-conteos de Visual Journeyman Style, Central Pack y Spanish Made Visual caen el 11-27/28. Sin cambios de estado.

## Embudo
- Etapa 1: 40 keywords (13 huellas nunca usadas de `semillas.md` §1 + 27 combinaciones molde × tema / momentos de vida), 4 subagentes Haiku, US GB CA AU. Lotes: (1) instant access, emailed instantly, gumroad, etsy digital, video course, 30-day plan, printable journal, only $7, only $9, just $17; (2) $27 today, £9 today, £17 only, plumbing cheat sheet, welding cheat sheet, pharmacy technician study guide, phlebotomy study guide, insurance license exam, part 107 study guide, roofing estimate template; (3) esthetician templates, newborn schedule, pregnancy checklist, breastfeeding checklist, debt payoff planner, freelance invoice template, linkedin profile templates, interview questions answers, guitar chords chart, fishing knots; (4) camping checklist, yoga sequences, aquarium cycling guide, dog grooming guide, funeral planning checklist, layoff severance guide, first apartment checklist, college dorm checklist, car accident checklist, identity theft recovery.
- Anomalías: lotes 3 y 4 usaron un `client_conversation_id` de 19 caracteres (aceptado). `aquarium cycling guide` y algunos bloques ALL devolvieron el mismo resultado en los 4 países (el subagente lo marcó; no verificado). `layoff severance guide` 0 ACTIVE.
- Etapa 2: 9 páginas verificadas con paso rápido (una consulta `page_ids` + US): Ultimate Budget Planner, Quinn Morrissette Studio, The Paycheck Plan, Spreadsheetables, Plum & Pencil, The Family Folder, Visuals Loop, Upleaf Studio, Checkride Study Guide. Paso completo: Ultimate Budget Planner.

## Cobertura (por página)
| Página | page_id | País | ACTIVE | Cohorte 7+ | Nota |
|---|---|---|---|---|---|
| Ultimate Budget Planner (oferta Debt Snowball Avalanche) | 485276957995076 | US | 28 (total página) | **13 / 13** | creados 12-sep (70 d), una tanda; landing debtpayoffplanner.site US$ 9 |
| idem | | GB | 24 | 11 / 11 | |
| idem | | CA | 28 | 13 / 13 | resultado idéntico a US |
| idem | | AU | 28 | 13 / 13 | resultado idéntico a US |
| Ultimate Budget Planner (oferta Ultimate Budget Planner) | 485276957995076 | US | | **11 / 15** | tandas 4 y 7-oct (46-49 d) + 4 ads de 17-21 nov; landing ultimatebudgetplanner.site US$ 9 |
| idem | | GB | | 11 / 13 | |
| idem | | CA / AU | | 11 / 15 | idéntico a US |
| Quinn Morrissette Studio | 101975594666133 | US | 50 (tope; est. 542) | ≥ 5 visibles | curso en video «1 Day Welder» US$ 58 + marca personal; fuera por A y D. Solo apareció en US GB CA AU con el mismo ad |
| The Paycheck Plan | 1381188005083313 | US | 3 | 0 / 3 | |
| Spreadsheetables | 110233751896223 | US | 50 (tope; est. 72) | 0 visible | plantillas para revender; fuera |
| Plum & Pencil | 1357650247441173 | US | 3 | 1 / 3 | |
| The Family Folder | 487465484456721 | US | 10 | 4 / 10 | vigilancia |
| Visuals Loop | 632093113327237 | US | 5 | 2 / 5 | |
| Upleaf Studio | 1349687651563870 | US | 6 | 5 / 6 | vigilancia |
| Checkride Study Guide | 470054809533979 | US | 50 (tope; est. 159) | ≥ 22 | flashcards físicas; ya en RAW 2026-11-20 |

`ALL` en US sobre 485276957995076: 113 ads en total (28 activos) → mucho churn de creativos, ofertas que ya se probaron y apagaron.
Gate: A ✓ (marca «Cosmo Suite Limited, UK», sin persona; pie sin redes), B ✓ (landing directa con botón de compra US$ 9, checkout no recorrido), C: sin upsell visible («No upsells»), D ✓ (planilla Excel + Sheets; el tutorial YouTube es bono). Zombis por API: ≥ 3 fechas de creación y 4 ads de 17-21 nov → vivo.
Molde en otros mercados: no se corrieron búsquedas en otros idiomas (tiempo); sugerido en la tarjeta.
