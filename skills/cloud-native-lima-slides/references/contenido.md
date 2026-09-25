# Contenido JSON y layouts

El generador usa solo Python 3. Ejemplo completo: `../assets/template/example.json`.

## Documento

`title`: título de la pestaña; `subtitle`: descripción en la barra; `label`: rótulo de las diapositivas; `slides`: lista no vacía.

## Campos comunes de diapositiva

- `layout`: uno de los siete layouts siguientes.
- `title`: título principal; `accent`: segunda línea opcional resaltada.
- `dark`: booleano opcional para fondo marino.
- `footer`: pie breve, apropiado para estado de una propuesta o fecha de consulta.
- `notes`: explicación larga para el presentador, oculta durante la presentación.
- `sources`: lista de objetos `{"label": "Fuente", "url": "https://…"}`. Aparecen en el pie y en las notas.

El contenido JSON es texto plano, no HTML: el renderizador escapa caracteres. Las URLs aceptan HTTP, HTTPS o mailto. No insertar bloques de HTML en el JSON.

## Layouts

| Layout | Campos específicos | Uso |
|---|---|---|
| `cover` | `series`, `tagline`, `badge`, `message`, `tags` (hasta 3) | Logo A y propuesta de apertura |
| `cards` | `items` (2–4): `icon`, `title`, `text` | Objetivos, beneficios, reglas |
| `flow` | `items` (2–4): `icon`, `title`, `text` | Pasos numerados |
| `metrics` | `items` (3): `value`, `title`, `text` | Valores con contexto |
| `split` | `items` (2): `label`, `title`, `points` (lista breve) | Roles de dos equipos |
| `links` | `items` (2–6): `icon`, `title`, `url` | Fuentes y recursos |
| `closing` | `callout`, `message`, `tags` (hasta 3) | Siguiente paso y QR a la comunidad |

Iconos disponibles: `people`, `book`, `heart`, `shield`, `calendar`, `mic`, `check`, `key`, `globe`, `balance`, `mail`, `flag`, `link`, `school`, `lock`, `chart`, `code`, `cloud`.

Para pasos de cuatro elementos, usar títulos de una o dos palabras. Las métricas necesitan procedencia o la etiqueta «propuesta». Las tarjetas no son un lugar para párrafos: cada explicación extensa va en `notes`.

## Ejecución

Desde cualquier carpeta, con la ruta real del skill:

```sh
python3 /ruta/al/skill/assets/template/render.py contenido.json --output charla.html
```

El HTML integra todos los recursos; compartirlo no requiere compartir el directorio del skill. El JSON permanece como fuente editable. El PDF se exporta desde el navegador después de verificar el HTML.
