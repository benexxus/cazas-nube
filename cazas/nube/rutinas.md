# Rutinas de la nube

Entorno: `env_01HHJfWCw4kCngd7cw3uj5Lq` (Default). Creadas el 2026-11-20. Conectores adjuntos: Meta_Ads_Library, Firecrawl, Claude_Docs, Claude_Code_Remote.

**Desde el 2026-11-22: una sola corrida por día**, de madrugada, una sesión cada 30 minutos (cada corrida dura
10-15 minutos, así no se pisan). Antes eran dos (mañana y tarde).

| Sesión | Id de la rutina | Cron UTC | Hora local (Europe/Madrid, invierno) | Modelo |
|---|---|---|---|---|
| EN (US, GB, CA, AU) | `trig_01RkprFnJjhTDUmuPA9NHoJo` | `0 2 * * *` | 03:00 | claude-sonnet-5-5 |
| BR | `trig_01VXzvyaBRKuNk8SXU4et1Vs` | `30 2 * * *` | 03:30 | claude-sonnet-5-5 |
| ES (CO, MX, ES) | `trig_01LiEvqkcztqFh7GXYYUykL9` | `0 3 * * *` | 04:00 | claude-sonnet-5-5 |
| EU (IT, FR, DE, PT) | `trig_019k6LjHpK6CZdz7WPeVaDka` | `30 3 * * *` | 04:30 | claude-sonnet-5-5 |
| ESTE (RO, PL, CZ, HU) | `trig_01BoJZKpXC27ThoBVTDXipJM` | `0 4 * * *` | 05:00 | claude-sonnet-5-5 |

> El cron está en UTC: con el horario de verano (desde fin de marzo) corren una hora más tarde en hora local
> (04:00 a 06:00).
