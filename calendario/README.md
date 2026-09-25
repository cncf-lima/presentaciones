# Calendario propuesto · Cloud Native Lima

Cierre de 2026 y año completo 2027. Zona horaria: America/Lima. Todas las actividades son propuestas; fechas y sedes por acordar.

## Recurrentes y fijos

- **Recurrentes:** University, Rejects y Specialization; cuatro ediciones anuales de cada línea en 2027. Distribución orientativa, no recurrencia exacta cada tres meses.
- **Fijos anuales:** apertura y cierre de comunidad, sugeridos una vez al año. «Fijo» no significa que el día o la sede estén confirmados.
- **Estado:** Propuesto, Confirmado o Cancelado, independiente del tipo. Confirmado exige fecha, hora y sede/plataforma.

Se proponen 12 eventos temáticos más dos hitos anuales en 2027. Apertura y cierre pueden coordinarse como sesiones breves junto a la actividad mensual si la capacidad del equipo lo requiere. University mantiene marzo, mayo, agosto y noviembre de la agenda anterior, sujeto al calendario académico de cada sede.

## Líneas

### Cloud Native University

Acercar el aula a la práctica y conectar con la comunidad. Encuentro en campus · 3 h propuestas. Público: Estudiantes y docentes.

### Cloud Native Rejects

Dar espacio a propuestas no seleccionadas en otras conferencias. Formato por validar con el equipo. Charlas y conversación · 2 h propuestas. Público: Ponentes y comunidad técnica.

### Cloud Native Specialization

Profundizar una especialidad mediante un laboratorio reproducible. Taller técnico · 3 h propuestas. Público: Personas con bases de contenedores y Kubernetes.

## Agenda

| Mes | Línea | Actividad | Tipo | Estado |
|---|---|---|---|---|
| 2026-10 | Cloud Native Specialization | Laboratorio de contenedores | recurrente | Propuesto |
| 2026-11 | Cloud Native University | La próxima edición en campus | recurrente | Propuesto |
| 2026-12 | Cloud Native Rejects | Primera edición y conversaciones | recurrente | Propuesto |
| 2027-01 | Cloud Native Specialization | Kubernetes: bases para operar | recurrente | Propuesto |
| 2027-01 | Hito de comunidad | Apertura del año y bienvenida al equipo | fijo | Propuesto |
| 2027-02 | Cloud Native Rejects | Ideas que merecen escenario | recurrente | Propuesto |
| 2027-03 | Cloud Native University | Del aula al contenedor | recurrente | Propuesto |
| 2027-04 | Cloud Native Specialization | GitOps en la práctica | recurrente | Propuesto |
| 2027-05 | Cloud Native University | Tu primera aplicación en Kubernetes | recurrente | Propuesto |
| 2027-06 | Cloud Native Specialization | Observabilidad para diagnosticar | recurrente | Propuesto |
| 2027-07 | Cloud Native Rejects | Experiencias de infraestructura | recurrente | Propuesto |
| 2027-08 | Cloud Native University | Aprender a observar una aplicación | recurrente | Propuesto |
| 2027-09 | Cloud Native Specialization | Seguridad en Kubernetes | recurrente | Propuesto |
| 2027-10 | Cloud Native Rejects | Open source: ideas y contribuciones | recurrente | Propuesto |
| 2027-11 | Cloud Native University | Proyectos para compartir | recurrente | Propuesto |
| 2027-12 | Cloud Native Rejects | Aprendizajes del año | recurrente | Propuesto |
| 2027-12 | Hito de comunidad | Cierre anual de Cloud Native Lima | fijo | Propuesto |

## Operación

Seis semanas antes: asignar responsable y validar objetivo, sede y facilitación. Cuatro semanas antes: revisar charlas/laboratorio, requisitos, presupuesto y convocatoria. Después: compartir recursos, medir asistencia real y hacer retrospectiva.

Rejects usa provisionalmente el formato de charlas no seleccionadas en otras conferencias; no implica afiliación con una conferencia ni fechas relativas a ella. Selección por calidad y adecuación al público. Specialization es formación comunitaria, no una certificación oficial.

La fuente editable es `calendario/eventos.json`. Ejecutar `python3 scripts/build_calendar.py` para actualizar HTML, CSV y este documento. El HTML filtra por año, línea y tipo; imprimir respeta la vista filtrada. CSV completo incluye todos los registros, no solo la vista. No se generan invitaciones ni archivos ICS sin fechas y horas acordadas. Este plan sustituye la agenda temática anterior; los meses futuros no representan compromisos confirmados.
