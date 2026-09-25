"""Genera calendario HTML, CSV y Markdown desde calendario/eventos.json."""
from pathlib import Path
import base64,csv,html,io,json
from collections import defaultdict
from datetime import date
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'calendario/eventos.json').read_text())
esc=lambda v:html.escape(str(v),quote=True)
months=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
rows=[];groups=defaultdict(list);ids=set()
for e in d['events']:
    if e['id'] in ids:raise ValueError('ID duplicado: '+e['id'])
    ids.add(e['id']);date.fromisoformat(e['month']+'-01')
    if e['kind'] not in ('recurrente','fijo'):raise ValueError('Tipo inválido')
    if e['status'] not in ('Propuesto','Confirmado','Cancelado'):raise ValueError('Estado inválido')
    if e['status']=='Confirmado' and (not e['date'] or not e['time'] or e['venue']=='Por confirmar'):raise ValueError('Un evento confirmado necesita fecha, hora y sede/plataforma')
    if e['date'] and date.fromisoformat(e['date']).strftime('%Y-%m')!=e['month']:raise ValueError('La fecha no coincide con el mes')
    series=d['series'].get(e['series']);name=series['name'] if series else 'Hito de comunidad'
    owner=series['owner'] if series else 'Equipo organizador'
    duration=series['format'] if series else 'Encuentro de comunidad · 90 min propuestos'
    color=series['color'] if series else '#087658'
    kind='↻ Recurrente' if e['kind']=='recurrente' else '◆ Fijo anual'
    details=[('Objetivo',e['outcome']),('Nivel',e['level']),('Formato',duration),('Responsable funcional',owner),('Sede',e['venue']),('Ponentes',e['speakers']),('Cupo',e['capacity'] if e['capacity'] is not None else 'Por definir'),('Presupuesto PEN',e['budget_pen'] if e['budget_pen'] is not None else 'Por cotizar')]
    card=f'<article class="event" style="--color:{color}" data-year="{e["month"][:4]}" data-series="{e["series"] or "community"}" data-kind="{e["kind"]}" data-status="{e["status"]}"><div class="event-top"><span class="series">{esc(name)}</span><span class="badge">{kind}</span></div><h3>{esc(e["title"])}</h3><p class="meta">{esc(e["cadence"])}<br>{esc(e["date"] or "Día por acordar")} · {esc(e["time"] or "Hora por acordar")}</p><span class="status">{esc(e["status"])}</span><details><summary>Objetivo y coordinación</summary><dl>'+''.join('<dt>'+esc(k)+'</dt><dd>'+esc(v)+'</dd>' for k,v in details)+'</dl></details></article>'
    groups[e['month']].append(card)
    rows.append([e['month'],name,e['title'],e['kind'],e['cadence'],e['status'],e['date'] or '',e['time'] or '',d['timezone'],e['venue'],owner,e['outcome'],e['level'],e['speakers'],e['capacity'] if e['capacity'] is not None else '',e['budget_pen'] if e['budget_pen'] is not None else '',e['registration_url'] or ''])
stream=io.StringIO(newline='');w=csv.writer(stream,lineterminator="\n");w.writerow(['Mes','Línea','Actividad','Tipo','Frecuencia','Estado','Fecha','Hora','Zona horaria','Sede','Responsable funcional','Objetivo','Nivel','Ponentes','Cupo','Presupuesto PEN','Registro']);w.writerows(rows)
csv_text='\ufeff'+stream.getvalue();(ROOT/'calendario/eventos.csv').write_text(csv_text)
tracks=''.join('<article class="track" style="--color:'+s['color']+'"><small>RECURRENTE · 4 EDICIONES / AÑO</small><h2>'+esc(s['short'])+'</h2><p>'+esc(s['purpose'])+'</p><p class="audience">'+esc(s['audience'])+'</p></article>' for s in d['series'].values())
body=''.join('<section class="month"><header><h2>'+months[int(m[5:])-1]+'</h2><span>'+m[:4]+'</span></header>'+''.join(events)+'</section>' for m,events in sorted(groups.items()))
assets=ROOT/'skills/cloud-native-lima-slides/assets/template'
values={'TRACKS':tracks,'MONTHS':body,'CSV':'data:text/csv;base64,'+base64.b64encode(csv_text.encode()).decode()}
for key,file in [('LOGO','logo.png'),('ICON','icon.png')]:values[key]='data:image/png;base64,'+base64.b64encode((assets/file).read_bytes()).decode()
s=(ROOT/'calendario/template.html').read_text()
for key,value in values.items():s=s.replace('{{'+key+'}}',value)
(ROOT/'calendario.html').write_text(s)
md='''# Calendario propuesto · Cloud Native Lima

Cierre de 2026 y año completo 2027. Zona horaria: America/Lima. Todas las actividades son propuestas; fechas y sedes por acordar.

## Recurrentes y fijos

- **Recurrentes:** University, Rejects y Specialization; cuatro ediciones anuales de cada línea en 2027. Distribución orientativa, no recurrencia exacta cada tres meses.
- **Fijos anuales:** apertura y cierre de comunidad, sugeridos una vez al año. «Fijo» no significa que el día o la sede estén confirmados.
- **Estado:** Propuesto, Confirmado o Cancelado, independiente del tipo. Confirmado exige fecha, hora y sede/plataforma.

Se proponen 12 eventos temáticos más dos hitos anuales en 2027. Apertura y cierre pueden coordinarse como sesiones breves junto a la actividad mensual si la capacidad del equipo lo requiere. University mantiene marzo, mayo, agosto y noviembre de la agenda anterior, sujeto al calendario académico de cada sede.

## Líneas

'''
for track in d['series'].values():md+='### '+track['name']+'\n\n'+track['purpose']+' '+track['format']+'. Público: '+track['audience']+'.\n\n'
md+='## Agenda\n\n| Mes | Línea | Actividad | Tipo | Estado |\n|---|---|---|---|---|\n'
for r in rows:md+='| '+' | '.join([r[0],r[1],r[2],r[3],r[5]])+' |\n'
md+='''
## Operación

Seis semanas antes: asignar responsable y validar objetivo, sede y facilitación. Cuatro semanas antes: revisar charlas/laboratorio, requisitos, presupuesto y convocatoria. Después: compartir recursos, medir asistencia real y hacer retrospectiva.

Rejects usa provisionalmente el formato de charlas no seleccionadas en otras conferencias; no implica afiliación con una conferencia ni fechas relativas a ella. Selección por calidad y adecuación al público. Specialization es formación comunitaria, no una certificación oficial.

La fuente editable es `calendario/eventos.json`. Ejecutar `python3 scripts/build_calendar.py` para actualizar HTML, CSV y este documento. El HTML filtra por año, línea y tipo; imprimir respeta la vista filtrada. CSV completo incluye todos los registros, no solo la vista. No se generan invitaciones ni archivos ICS sin fechas y horas acordadas. Este plan sustituye la agenda temática anterior; los meses futuros no representan compromisos confirmados.
'''
(ROOT/'calendario/README.md').write_text(md)
print(f'Calendario generado: {len(rows)} actividades propuestas.')
