# Rutinas de la nube

Entorno: `env_01HHJfWCw4kCngd7cw3uj5Lq` (Default). Creadas el 2026-11-20. Conectores adjuntos: Meta_Ads_Library, Firecrawl, Claude_Docs, Claude_Code_Remote.

| Sesión | Id de la rutina | Cron UTC | Hora local (Europe/Madrid, invierno) | Modelo |
|---|---|---|---|---|
| EN (US, GB, CA, AU) | `trig_01RkprFnJjhTDUmuPA9NHoJo` | `30 5,17 * * *` | 06:30 y 18:30 | claude-sonnet-5-5 |
| BR | `trig_01VXzvyaBRKuNk8SXU4et1Vs` | `45 5,17 * * *` | 06:45 y 18:45 | claude-sonnet-5-5 |
| ES | `trig_01LiEvqkcztqFh7GXYYUykL9` | `0 6,18 * * *` | 07:00 y 19:00 | claude-sonnet-5-5 |
| EU | `trig_019k6LjHpK6CZdz7WPeVaDka` | `15 6,18 * * *` | 07:15 y 19:15 | claude-sonnet-5-5 |
| ESTE (RO, PL, CZ, HU) | `trig_01BoJZKpXC27ThoBVTDXipJM` | `30 6,18 * * *` | 07:30 y 19:30 | claude-sonnet-5-5 |

> El cron está en UTC: con el horario de verano (desde fin de marzo) corren una hora más tarde en hora local (07:30 / 19:30…).

> Horarios separados cada 15 minutos el 2026-11-21 (antes, 5 minutos): con el embudo de dos etapas las corridas duran más y se pisaban en `cola.md` y `log.md`.
