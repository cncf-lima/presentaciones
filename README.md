# Cloud Native Lima · Presentaciones

Materiales de Cloud Native Lima para dar la bienvenida a organizadores e invitar a universidades a participar en Cloud Native University.

## Presentaciones actuales

| Presentación | HTML autónomo | PDF | Contenido |
|---|---|---|---|
| Cloud Native University | [Descargar HTML](https://github.com/cncf-lima/presentaciones/raw/refs/heads/main/cloud-native-university.html) | [Ver PDF](cloud-native-university.pdf) | 12 diapositivas principales y 3 de historial; invitación a universidades. |
| Onboarding de organizadores | [Descargar HTML](https://github.com/cncf-lima/presentaciones/raw/refs/heads/main/onboarding-organizadores.html) | [Ver PDF](onboarding-organizadores.pdf) | 15 diapositivas; funciones, operación y políticas CNCF. |

Descarga el HTML y ábrelo en tu navegador. Cada presentación incluye sus imágenes y funciona sin servidor. Usa las flechas, el selector, «Ver todas» o «Notas y fuentes». Para exportar, selecciona «PDF / Imprimir»: se imprimen todas las diapositivas.

## Editar y regenerar

Requiere Python 3; los generadores usan únicamente la biblioteca estándar.

```sh
python3 crear_onboarding_organizadores.py
python3 crear_invitacion_universidades.py
```

Para University, editar `crear_invitacion_universidades.py` y `universidades.css`. Para organizadores, editar `crear_onboarding_organizadores.py`. Los scripts regeneran los HTML y sus plantillas. El onboarding se genera primero porque University reutiliza su navegación y controles. `onboarding-integrantes-anterior.template.html` es una dependencia de plantilla, no una presentación vigente.

Después de modificar el contenido, volver a exportar los PDF desde el navegador y versionarlos junto con los HTML. Los alias `presentacion-universidades.html` y `onboarding-cloud-native-lima.html` se generan localmente; las versiones canónicas son las enlazadas en la tabla.

## Identidad y fuentes

Usamos el logo de la opción A de Cloud Native Lima, con la referencia a Lima y al río Rímac. Los PNG necesarios para regenerar las presentaciones están en `identidad/`. Es una identidad local propuesta; no representa aprobación oficial de una marca CNCF.

- [Comunidad y eventos](https://ocgroups.dev/cncf/group/nmmzkrs)
- [Revisión del historial de eventos](revision-eventos.md) · [CSV](revision-eventos.csv)
- [Programa de comunidades CNCF](https://github.com/cncf/communitygroups)
- [Código de conducta CNCF](https://github.com/cncf/foundation/blob/main/code-of-conduct.md)

Fuentes revisadas el 25/09/2026. El historial distingue las ediciones University, las colaboraciones de apoyo y el archivo heredado; excluye registros de prueba. Fechas, cupos y recursos del próximo piloto son propuestas por acordar. Las notas enlazadas en cada presentación aportan contexto y fuentes.

## Actualizaciones

Propón cambios mediante un issue o pull request. Revisa enlaces, navegación, vista móvil y PDF antes de publicar una actualización. Conserva la distinción entre requisitos CNCF, recomendaciones y prácticas locales propuestas.
