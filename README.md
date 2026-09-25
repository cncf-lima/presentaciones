# Cloud Native Lima · Presentaciones

Presentaciones, plantilla y skill para crear diapositivas de Cloud Native Lima con una identidad compartida: logo A, azul, marino y menta, bloques visuales, notas y fuentes.

## Presentaciones

| Presentación | HTML autónomo | PDF |
|---|---|---|
| Cloud Native University · 12 diapositivas + 3 de historial | [Descargar](https://github.com/cncf-lima/presentaciones/raw/refs/heads/main/cloud-native-university.html) | [Ver PDF](cloud-native-university.pdf) |
| Onboarding de organizadores · 15 diapositivas | [Descargar](https://github.com/cncf-lima/presentaciones/raw/refs/heads/main/onboarding-organizadores.html) | [Ver PDF](onboarding-organizadores.pdf) |
| Plantilla visual · 7 componentes | [Descargar](https://github.com/cncf-lima/presentaciones/raw/refs/heads/main/plantilla-diapositivas.html) | [Ver PDF](plantilla-diapositivas.pdf) |

Descarga el HTML y ábrelo en tu navegador. Incluye las imágenes y funciona sin servidor. Navega con flechas o selector; «Ver todas» muestra el conjunto; «Notas y fuentes» abre los detalles. «PDF / Imprimir» exporta todas las diapositivas.

## Calendario de eventos

[Calendario interactivo · descargar HTML](https://github.com/cncf-lima/presentaciones/raw/refs/heads/main/calendario.html) · [PDF 2027](calendario-2027.pdf) · [CSV editable](calendario/eventos.csv) · [Plan y criterios](calendario/README.md)

En 2027: **12 recurrentes** (4 University, 4 Rejects, 4 Specialization) y **2 fijos anuales propuestos** (apertura y cierre). Incluye también tres propuestas para el cierre de 2026. El tipo de evento y su confirmación son campos separados: todas las actividades están propuestas, con día y sede por acordar. Rejects tiene un formato provisional por validar.

Editar `calendario/eventos.json` y ejecutar `python3 scripts/build_calendar.py`. El HTML funciona sin servidor, filtra por año/línea/tipo y exporta el CSV completo. Para actualizar el PDF de 2027, restablecer los filtros y usar «Imprimir vista».

## Generar nuevas diapositivas

Requiere Python 3, sin paquetes adicionales. Copia el [JSON de ejemplo](skills/cloud-native-lima-slides/assets/template/example.json), adapta sus textos y ejecuta:

```sh
python3 skills/cloud-native-lima-slides/assets/template/render.py contenido.json --output mi-presentacion.html
```

[Formato y campos](skills/cloud-native-lima-slides/references/contenido.md). Componentes: portada, tarjetas, pasos, métricas, colaboración en dos columnas, enlaces y cierre con QR. El QR abre la comunidad, no agenda una reunión.

## Skill para Codex y Claude

El mismo [skill cloud-native-lima-slides](skills/cloud-native-lima-slides/SKILL.md) incluye las instrucciones, plantilla, generador e imágenes. Funciona sin clonar el repositorio completo.

Para instalarlo en este equipo:

```sh
python3 scripts/install_skill.py --target both
```

También admite `--target codex` o `--target claude`. Copia el skill a `$CODEX_HOME/skills` (por defecto `~/.codex/skills`) y `~/.claude/skills`. Para actualizar una instalación existente: añadir `--update` después de revisar los cambios.

En una nueva sesión:

- Codex: `Usa $cloud-native-lima-slides para crear una presentación de 8 diapositivas sobre Kubernetes para estudiantes.`
- Claude Code: `/cloud-native-lima-slides Crea una presentación sobre Kubernetes para estudiantes.`

[Descargar el paquete ZIP](cloud-native-lima-slides.zip) para compartir o importar donde se admitan skills. El ZIP contiene SKILL.md y todos sus recursos. La instalación local no habilita automáticamente el skill en una cuenta web de Claude. [Referencia oficial de skills de Claude Code](https://code.claude.com/docs/en/skills).

## Editar el diseño compartido

La fuente única está en `skills/cloud-native-lima-slides/assets/template/`:

- `theme.css`: colores, tipografía, componentes, móvil e impresión.
- `shell.html`: navegación, notas, selector y controles.
- `render.py`: renderizador JSON y componentes compartidos.
- `icons.json`, `logo.png`, `icon.png`, `qr.png`: identidad visual.

Las presentaciones actuales usan ese motor mediante `slidekit.py`. Su contenido está en `crear_onboarding_organizadores.py` y `crear_invitacion_universidades.py`. Para regenerar todas las presentaciones:

```sh
python3 scripts/build_all.py
python3 -m unittest discover -s tests
```

El generador produce HTML, no PDF. Después de cambiar contenido o tema, revisar todas las diapositivas en escritorio y móvil; exportar los PDF desde el navegador y comprobar una página por diapositiva. En automatización, usar `printBackground: true` y `preferCSSPageSize: true`.

Los alias `presentacion-universidades.html` y `onboarding-cloud-native-lima.html` se generan localmente; se versionan las rutas canónicas de la tabla. Para actualizar el ZIP después de editar el skill, ejecutar `python3 scripts/package_skill.py`; actualizar también las instalaciones locales con `--update`.

## Fuentes y comunidad

- [Comunidad y eventos](https://ocgroups.dev/cncf/group/nmmzkrs)
- [Revisión del historial](revision-eventos.md) · [CSV](revision-eventos.csv)
- [Programa de comunidades CNCF](https://github.com/cncf/communitygroups)
- [Código de conducta CNCF](https://github.com/cncf/foundation/blob/main/code-of-conduct.md)

Fuentes de las presentaciones revisadas el 25/09/2026. Distinguir eventos propios, apoyo y archivo heredado; no usar registros de prueba ni aforo como asistencia. El logo es identidad local, no aprobación oficial de marca CNCF. Las fechas y cupos del piloto son propuestas por acordar.

Proponer cambios mediante issue o pull request. Conservar fuentes, notas y distinción entre requisitos CNCF, recomendaciones y prácticas locales.
