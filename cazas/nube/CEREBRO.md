# CEREBRO.md — lo que el cerebro de Carlos ya sabe de cazar

> **Puente cerebro → nube.** Este archivo es una copia destilada del cerebro local de Carlos
> (Obsidian, en su PC), hecha a pedido suyo. Las rutinas no pueden leer su PC: **lo que sabe el
> cerebro llega acá**. Última sincronización: **2026-11-20**. Se rehace cuando Carlos pide
> «sincronizá el cerebro con las cazas».
>
> **Jerarquía:** en **evidencia y criterio** (vara, gate, score, cómo se cuenta, cómo se
> escribe) **este archivo manda sobre `skills/cazar/` y `modos-y-bandeja.md`**. En lo
> **técnico** (git, sin navegador, horarios) manda `NUBE.md`. Una rutina **no edita este
> archivo**.

---

## 1. La vara — 10+, por oferta y por país, igual en todos los mercados

> **Decidido por Carlos el 2026-11-20.** Reemplaza la vara por región (20 / 30) de la mañana
> del mismo día. Vale en las cinco sesiones (EN · BR · ES · EU · ESTE).

**Sobrevivientes** = anuncios creados hace **7 días o más** y **todavía activos**, contados
**en el país cazado** y **sobre la misma oferta**. El total de activos es contexto, nunca
evidencia.

| Veredicto | Sobrevivientes (oferta × país) | Qué hace la rutina |
|---|---|---|
| **Pasa** | **10+** | gate de 5 filtros → si pasa, **tarjeta** |
| **Cerca** | 7-9 | señal en «Señales del día» con **fecha de re-conteo** (+7 d). Ni tarjeta ni descarte |
| **Vigilancia** | 4-6 | señal en «Señales del día» con **fecha de re-conteo** (+7 d). Ni tarjeta ni descarte |
| Señal | < 4 | a lo sumo una línea de señal, sin re-conteo |

- **Un solo número en todos los países**, sin vara por región.
- **Whale = 100+ sobrevivientes**, una oferta, un país. Un whale **no se salta el gate**.
- **Reporte:** el veredicto — «pasa», «cerca», «vigilancia». El conteo crudo
  (`sobrevivientes / activos`, con qué reloj, ver §2) va en el informe de `RAW/cazas-auto/`.
  Con `limit: 50` lleno, el número es **piso (`≥`)**.
- **Las tandas no se piden.** Son contexto: no aprueban ni tumban un candidato.
- **Ratio** `sobrevivientes / activos` = salud; se lee contra la longevidad.
- **Se cuenta por OFERTA, no por anunciante.** Un anunciante con 20 verticales de 5-8
  anuncios no es un winner: es un portafolio (caso *The Ascent Club*).

## 2. Cómo se cuenta sin engañarse (correcciones de método ya pagadas)

1. **El barrido tiene dos pasos.** Paso 1: `search_terms` → solo sacás `page_id` y nombres
   de oferta, **ninguna edad**. Paso 2: una consulta por `page_id` + `countries` → ahí se
   cuentan sobrevivientes. El techo de 50 devuelve lo **más nuevo**: contar sobre el paso 1
   da ceros falsos.
2. **Si el paso 2 devuelve 50, cortá hasta bajar de 50:** por país, por oferta
   (`search_terms: "<título de la oferta>"`). Con +50 activos, cortá por **los dos países de
   la vara y uní las listas**: cada corte trae un subconjunto distinto (caso *Energy
   Profitable*: la tanda más vieja solo apareció en el corte 🇬🇧).
3. **Dos relojes.** `ad_creation_time` (creación) y `ad_delivery_start_time` (entrega)
   difieren 1-2 días. Si el veredicto depende de **una tanda de 7-9 días**, decide el de
   **entrega**, y si discrepan **gana el que deja al candidato afuera**.
4. **`ALL` sobre todo candidato que llega al gate** (`page_ids` + `countries` +
   `ad_active_status: ALL`) y comparar con `ACTIVE`: las ofertas apagadas son **sus tests
   fallidos** — anotarlas en el informe («dónde ya se probó y falló»).
5. **Un cero en el paso 1 no dice nada del mercado.** Un cero en el paso 2 sobre un
   `page_id` sí es un hecho. En húngaro (lengua aglutinante) un cero vale todavía menos.
6. **Un número grande de resultados NO es un nicho ocupado**: mirá cuántos anunciantes
   distintos hay y si venden lo nuestro (una app puede llenar un barrido entero).
7. **No se puede cazar por plataforma de cobro.** `hotmart`, `kiwify`, `digistore24`,
   `whop.com`, `myshopify.com`, `pay.hotmart.com`, `pay.kiwify.com.br` son **keywords
   contaminadas**. La excepción es **`impultienda`**: aloja cada tienda en
   `<tienda>.impultienda.ar` y el nombre aparece en el anuncio.
8. **El dominio raíz vacío no prueba que no haya landing** (Shopify esconde `/pages/`). La
   landing se saca **siguiendo el link del anuncio**. El handle de la tienda no es marca
   personal: decide quién cobra.

## 3. El gate — cinco filtros eliminatorios

| | Filtro | Pregunta |
|---|---|---|
| **A** | Marca personal | ¿Hay una persona con audiencia detrás? (anuncios + dominio raíz + About + pie de página + redes) |
| **A-bis** | Marketplace de expertos | ¿Cada producto necesita un experto con credenciales a cámara? |
| **B** | Embudo | ¿La página está diseñada para vender un infoproducto? (o WhatsApp con la oferta en el copy) |
| **C** | Back-end | ¿El front-end se sostiene solo o es carnada? |
| **D** | **Entregable** | **¿Qué tendríamos que producir?** PDF / guía / plantilla ✅ · video con instructor, libro impreso, área de miembros, suscripción, app, software ⛔ |

Patrones que ya cayeron: marca personal · marketplace de expertos · entregable que no
producimos · lead-gen a llamada · catálogo de terceros · producto físico · PLR/reventa.
**Modelamos productos, no marcas.** Desde la nube, lo que no se pudo verificar se dice
(«embudo no verificado desde la nube»), nunca se inventa.

## 4. Score de 4 señales (solo si pasa el gate)

① longevidad: sobrevivientes a **45+ días** · ② volumen: **50+** sobrevivientes, un
jugador, una oferta, un país · ③ duplicación: mismo creativo **10+ veces entre los
sobrevivientes** · ④ hueco de arbitraje en un destino. 4/4 = A · 3 = B · ≤2 = observar.

## 5. Cómo se escribe (reglas de Carlos)

- **Ningún país se descarta.** Prohibido «DESCARTAR», «vacío», «quemado», «no volver» sobre
  un país. Se escribe el hecho con su alcance: *«🇭🇺: 5 anunciantes en 4 días, 0
  sobrevivientes, nicho X, fecha»*.
- **Nunca «quemado» sobre un nicho.** Semáforo: 🟢 2-6 anunciantes, ninguno domina · 🟡
  7+ con ofertas parecidas = **evaluable** (el diferencial es ángulo, avatar o mercado) ·
  🔴 solo si falla el gate o no hay demanda.
- **Un tester no es un hallazgo.** Algo con 0 sobrevivientes y horas de vida se escribe
  «OFERTA NO VALIDADA» con la tabla de umbrales al lado. **Hueco ≠ validado.**
- En 🇧🇷 🇨🇴 🇲🇽 (y el Este): **mucho volumen con 0 sobrevivientes es timing, no demanda**.
  Ahí pesan más el Filtro A (marca personal) y el B (lead-gen por WhatsApp).

## 6. Footprints de formato (sesgan el barrido hacia PDF)

| Idioma | Footprints |
|---|---|
| 🇺🇸🇬🇧🇨🇦🇦🇺 | `printable` · `print-ready` · `instant PDF` · `worksheets` · `fillable` · `workbook` · `no-prep` · `done-for-you` · `binder` · `checklist` |
| 🇩🇪 | `zum Ausfüllen` · `druckfertig` · `Vorlagen` · `Arbeitsblätter` · `Komplettset` |
| 🇫🇷 | `à imprimer` · `imprimable` · `modèles` · `fiches` · `classeur` |
| 🇮🇹 | `da stampare` · `stampabile` · `modelli` · `schede` |
| 🇧🇷🇵🇹 | `para imprimir` · `imprimível` · `apostila` · `planilhas` |
| 🇵🇱 | `do druku` · `gotowe do wydruku` · `karty pracy` |
| 🇷🇴 | `de printat` · `printabil` · `fișe` |

**Anti-keywords:** si el nicho solo trae `video lessons`, `masterclass`, `membership`,
`subscription`, `paperback`, `free shipping`, es un **hueco de formato** (anotalo como señal).

**El formato que más rinde hoy en el cerebro: el «cuaderno ilustrado»** — PDF de 50-92 páginas,
una idea por página, dibujada («in pictures», «made visual», «in mappe», «în imagini»,
«illustriert»). Hay decenas de operadores; está en 🟡.

## 7. Ya cazados — van como SEÑAL, nunca como tarjeta nueva

Si aparece uno de estos `page_id`, **no es novedad**: si cambió algo (país nuevo, oferta
nueva, cruzó la vara) va **una línea** en «Señales del día» con el antes → ahora; si no
cambió, no se menciona.

| Producto (ficha en el cerebro) | Operador | `page_id` | Estado |
|---|---|---|---|
| 60 Esercizi per Ciclisti | Lorenz Varen | `1351005084760173` | Idea · candidata B |
| Adult Voice & Resonance Clinical System | Adult Voice & Resonance | `1239610002573947` | Idea |
| Begin Early Activities | Rachel Bennett | `280579905138659` | Idea |
| Building Defects Atlas | Fernanda Oller | `1262265860313000` | Idea |
| Contabilitatea / Sudura / Teoria muzicii în imagini · Le Permis Bateau Illustré | Studio Facile (rota fanpages cada 2-3 semanas) | `1232011766670582` · `1272162682644374` | Idea |
| Cuadernos de Oficio | Furgo Libre | `1405313469331346` | Idea |
| The Electrical Controls Guide | Energy Profitable | `720903437767543` | Idea · 🟡 observar |
| Griffbereit | Griffbereit | `1395192210344917` | Idea |
| Kit Comptable Pratique / Kit Contabile Pratico | Amélie Boissieu · Giulia Ferraresi | `1363004406903385` · `1299765756564104` | Idea |
| Klarordner | Plainleaf Publishing | `1391989857327505` | Idea |
| Leave It Sorted | Leave It Sorted | `1273987602462473` | Idea |
| Lo Spagnolo in Mappe | Lingua Chiara | `1034177656443347` | Idea |
| Manual Prático do Eletricista Residencial | Packs & Moldes Pro | `1227856100409706` | Idea · 🟡 vigilancia |
| Planul Hashimoto 21 | Verde Guides | `1413675531823485` | Idea · oferta no validada |
| Relief On Every Plate (recetario: nicho excluido) | Relief On Every Plate | `1191202924084648` | Idea |
| The Resource Lab | The Resource Lab | `1123744187496255` | Idea |
| 200+ Visuelle Lernkarten Pflege | Gracie Williams | `1316868038177272` | Idea |
| Huerta en Casa | **producto propio de Carlos** | — | Testeando |

## 8. Prioridades que ya marcó el cerebro (para elegir nodos)

- **Destinos de mayor ticket primero**: 🇺🇸 🇬🇧 > Europa occidental > Latam (Latam va último
  como destino **por ticket, no por demanda**).
- Nichos con demanda validada: **profesiones** (material listo para docentes, contadores,
  enfermería; preparación de examen/oposición), **herencia y papeles** (ordenador de papeles
  rellenable), **cuadernos ilustrados** (formato), **idiomas en PDF** (🟢, pares de lenguas
  libres), **movilidad deportiva**.
- Los re-conteos con fecha del cerebro **no los hace la nube**: son a pedido de Carlos.
