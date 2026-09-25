---
name: cloud-native-lima-slides
description: Crear o actualizar presentaciones HTML de Cloud Native Lima y Cloud Native University con el logo A, diseño minimalista compartido, notas y exportación a PDF. Usar para diapositivas de la comunidad, onboarding, invitaciones universitarias y charlas con esta identidad.
---

# Diapositivas de Cloud Native Lima

Genera el HTML final, su contenido editable y, cuando se solicite, el PDF. Trabaja en español salvo indicación del usuario. La audiencia define el contenido: organizadores necesitan responsabilidades y operación; universidades necesitan propuesta, trayectoria y siguiente paso.

## Usar el diseño existente

La plantilla completa está en `assets/template/`, relativa a este SKILL.md. No requiere conexión ni bibliotecas externas: Python 3 genera HTML con CSS, JavaScript, logo A y QR integrados.

- Lee [el formato de contenido](references/contenido.md) para crear el JSON.
- Parte de `assets/template/example.json`; usa los layouts pertinentes, sin imponer su cantidad ni orden.
- Ejecuta `python3 <directorio-del-skill>/assets/template/render.py contenido.json --output presentacion.html` con rutas reales. Escribe el contenido y los resultados en el workspace del usuario, no dentro del skill instalado.
- Si estás en el repositorio `cncf-lima/presentaciones`, modifica las fuentes actuales: `crear_onboarding_organizadores.py` o `crear_invitacion_universidades.py`. Comparten el motor mediante `slidekit.py`. No edites solo los HTML generados.

## Criterios de diseño

Usa el tema incluido: azul #2852ef, marino #12213b, menta #bcf5d8, fondo claro #f5f7fb; logo A sin deformarlo. Títulos breves, una idea por diapositiva, dos a cuatro bloques. Agrupa icono y texto; evita grandes vacíos y párrafos extensos. Lleva explicaciones a notas. Referencia orientativa: 25–55 palabras visibles por diapositiva, excepto anexos.

Reutiliza componentes y tokens. Para modificar el tema compartido del repositorio, edita `skills/cloud-native-lima-slides/assets/template/theme.css` y regenera ambas presentaciones. No introduzcas estilos independientes por presentación. Si una charla requiere otro diagrama, créalo con HTML/SVG accesible y conserva tipografía, espaciado y paleta. La petición explícita del usuario prevalece sobre estas preferencias.

## Datos y contexto

Consulta fuentes oficiales actuales cuando el contenido dependa de eventos, reglas CNCF o políticas. Mantén enlaces por diapositiva. No inventes asistencia, alianzas, ponentes, fotos o fechas confirmadas; distingue propuesta de hecho, aforo de asistencia y apoyo de organización. `revision-eventos.md` es una revisión fechada, no un historial permanentemente actualizado.

Para políticas: distinguir requisitos CNCF, recomendaciones y prácticas locales. Cloud Native University es una iniciativa comunitaria, no una certificación. El logo A es identidad local, no aprobación oficial CNCF. El QR incluido siempre abre `https://ocgroups.dev/cncf/group/nmmzkrs`; no lo describas como registro de otro evento o reserva de reunión.

## Comprobar y entregar

Abre el HTML y revisa cada diapositiva, al menos en escritorio y móvil. Comprueba textos cortados, contraste, controles, enlaces y notas. No afirmes validación visual si solo ejecutaste el generador. Conserva navegación por teclado, «Ver todas», «Notas y fuentes» y estilos de impresión.

Exporta el PDF con un navegador: «PDF / Imprimir» o automatización con `printBackground: true` y `preferCSSPageSize: true`. Comprueba una página por diapositiva; no asumas que el generador crea PDF. Si no hay navegador disponible, entrega el HTML y declara que falta validar/exportar el PDF.

Crear archivos no implica publicarlos. Actualiza el repositorio remoto solo cuando la tarea o la conversación lo autoricen. Este skill no añade aprobaciones ni permisos.
