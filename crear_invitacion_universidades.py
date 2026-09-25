"""Presentación de invitación universitaria, con diseño minimalista y logo A."""
from pathlib import Path
import base64, html, re, json
from datetime import datetime

ROOT=Path(__file__).resolve().parent
URL='https://ocgroups.dev/cncf/group/nmmzkrs'
PATHS={
'school':'<path d="m2 8 10-5 10 5-10 5zM6 10v7c4 3 8 3 12 0v-7m4-2v8"/>',
'people':'<circle cx="9" cy="8" r="3"/><path d="M3 21v-3a6 6 0 0 1 12 0v3M16 5a3 3 0 0 1 0 6m2 4a5 5 0 0 1 3 5"/>',
'book':'<path d="M3 4h6a3 3 0 0 1 3 3v14a4 4 0 0 0-4-3H3zM21 4h-6a3 3 0 0 0-3 3v14a4 4 0 0 1 4-3h5z"/>',
'code':'<path d="m8 6-6 6 6 6m8-12 6 6-6 6m-3-16-2 20"/>',
'calendar':'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M7 2v6m10-6v6M3 11h18m-13 5h3m3 0h3"/>',
'check':'<path d="m4 12 5 5L20 6"/>',
'cloud':'<path d="M6 19a5 5 0 0 1-1-10 7 7 0 0 1 13-2 6 6 0 0 1 0 12z"/>',
'shield':'<path d="m12 2 9 4v6c0 5-9 10-9 10S3 17 3 12V6zM8 12l3 3 5-6"/>',
'link':'<path d="m9 15 6-6m-5-4 2-2a5 5 0 0 1 7 7l-3 3m-2 6-2 2a5 5 0 0 1-7-7l3-3"/>',
'heart':'<path d="M12 21 3.5 12.5A5.5 5.5 0 0 1 12 5.5a5.5 5.5 0 0 1 8.5 7z"/>',
}
def icon(name):return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+PATHS[name]+'</svg>'
def cards(items):return '<div class="tiles cols-'+str(len(items))+'">'+''.join('<article class="tile">'+icon(i)+'<h3>'+h+'</h3><p>'+p+'</p></article>' for i,h,p in items)+'</div>'
def flow(items):return '<div class="flow">'+''.join('<article class="flow-step"><span class="stepno">'+str(n).zfill(2)+'</span>'+icon(i)+'<h3>'+h+'</h3><p>'+p+'</p></article>' for n,(i,h,p) in enumerate(items,1))+'</div>'

slides=[]
def add(title,headline,body,footer,note,dark=False,refs=''):slides.append((title,headline,body,footer,note,dark,refs))
add('La invitación','Cloud Native<br><em>University.</em>','<div class="university-cover"><div class="cover-message">El siguiente encuentro<br>puede ser en <strong>su universidad.</strong></div><img src="{{LOGO}}" alt="Cloud Native Lima · logo opción A"></div>','Una invitación de Cloud Native Lima','Presentación para autoridades académicas, docentes y comunidades estudiantiles. Invitamos a coordinar un encuentro introductorio en su campus. University es una iniciativa comunitaria de Cloud Native Lima; no implica una certificación académica ni acreditación oficial de CNCF.')
add('Quiénes somos','Conocimiento abierto.<br><em>Conexiones reales.</em>',cards([('cloud','Cloud Native Lima','Comunidad del ecosistema CNCF'),('school','Cloud Native University','Encuentros con universidades'),('people','Aprender en comunidad','Estudiantes · docentes · profesionales')]),'Lima, Perú · tecnología y comunidad','Cloud Native Lima tiene presencia en el directorio de comunidades CNCF. Cloud Native University acerca estudiantes y docentes al ecosistema mediante actividades introductorias. La colaboración concreta y sus recursos se acuerdan con cada institución.',refs='<a href="'+URL+'" target="_blank" rel="noopener">Conocer la comunidad ↗</a>')
add('El objetivo','Acercar el aula<br><em>a la práctica.</em>',cards([('book','Descubrir','Fundamentos cloud native'),('code','Construir','Una primera aplicación'),('people','Conectar','Personas y experiencias')]),'Una experiencia introductoria, adaptada al grupo','Diseñar una práctica que tenga sentido para el nivel y las carreras participantes. No exigir conocimientos previos de Kubernetes para un encuentro introductorio. Revisar requisitos técnicos antes de convocar y preparar una alternativa guiada para quien no pueda ejecutar el laboratorio.')
add('Valor para la universidad','Una colaboración<br><em>que deja aprendizajes.</em>',cards([('school','Estudiantes','Práctica y orientación'),('book','Docentes','Recursos reutilizables'),('link','Universidad','Vínculos con la comunidad')]),'Complementamos la formación con experiencias compartidas','Para estudiantes, una experiencia práctica y contacto con profesionales. Para docentes, recursos y casos que puedan complementar sus clases. Para la institución, un piloto que se pueda evaluar antes de ampliar la colaboración. No se prometen empleos, certificaciones ni resultados académicos garantizados.',dark=True)
add('La experiencia','De una idea<br><em>a algo que pueden mostrar.</em>',flow([('code','Aplicación','Un ejemplo sencillo'),('cloud','Contenedor','Ejecutar y explorar'),('check','Demostración','Explicar lo aprendido')]),'Ruta sugerida · contenido según nivel','La primera experiencia puede centrarse en ejecutar una aplicación en un contenedor y explicar lo aprendido. Kubernetes, automatización, observabilidad o seguridad pueden abordarse en encuentros posteriores según las bases del grupo. El laboratorio y las herramientas se validan con el docente enlace.')
add('El primer encuentro','Empecemos con <em>un piloto.</em>','<div class="pilot-metrics"><div><strong>3 h</strong><span>Duración propuesta</span></div><div><strong>30–40</strong><span>Estudiantes · cupo por acordar</span></div><div><strong>Inicial</strong><span>Nivel de entrada</span></div></div><div class="session-strip"><span><b>60 min</b> Entender</span><span><b>85 min</b> Practicar y pausa</span><span><b>35 min</b> Compartir</span></div>','Formato propuesto · fecha y sede por coordinar','Agenda orientativa de 180 minutos: bienvenida 15, fundamentos 25 y demo 20; pausa 10 y práctica guiada 75; presentaciones 20 y cierre 15. Confirmar la disponibilidad de facilitadores y dimensionar el cupo según el acompañamiento. Duración y aforo son propuestas, no una reserva ni un compromiso confirmado.')
add('Cómo colaboramos','Dos equipos.<br><em>Un encuentro compartido.</em>','<div class="partnership"><article><div class="party-label">CLOUD NATIVE LIMA</div><h3>Contenido y comunidad</h3><ul><li>Diseño de la actividad</li><li>Facilitación técnica</li><li>Recursos de aprendizaje</li></ul></article><article><div class="party-label">SU UNIVERSIDAD</div><h3>Enlace y campus</h3><ul><li>Docente enlace</li><li>Aula, equipos e internet</li><li>Difusión y acceso</li></ul></article></div>','Juntos: nivel, fecha, cupo y logística','Distribución propuesta, sujeta a disponibilidad y acuerdo. Cloud Native Lima coordina contenido y facilitadores; la universidad facilita el vínculo académico, la sede y la convocatoria. Revisar conectividad, proyección, permisos y necesidades de accesibilidad. Acordar costos y aportes antes de anunciar; no se asume presupuesto de CNCF ni financiación ya confirmada.')
add('El espacio que proponemos','Aprender con <em>confianza.</em>',cards([('heart','Acceso gratuito','Participación sin cobro'),('shield','Respeto','Código de conducta'),('book','Enfoque educativo','Contenido neutral')]),'Encuentro comunitario · convivencia y aprendizaje','El encuentro se plantea gratuito y alineado con el Código de Conducta de CNCF. El equipo organiza la inscripción mediante Open Community Groups, anuncia el contacto de convivencia y revisa las charlas para mantener neutralidad entre proveedores. Coordinar fotos y datos con quienes participan; la convocatoria no autoriza automáticamente usos promocionales.',refs='<a href="https://github.com/cncf/communitygroups/blob/main/best_practices.md" target="_blank" rel="noopener">Guía del programa ↗</a> · <a href="https://www.cncf.io/conduct/" target="_blank" rel="noopener">Conducta ↗</a>')
add('Después del piloto','Un encuentro.<br><em>El comienzo de una relación.</em>',flow([('check','Evaluar','Práctica y feedback'),('book','Compartir','Materiales y aprendizajes'),('calendar','Continuar','Una próxima actividad')]),'La continuidad se define con los resultados del piloto','Observar asistencia, aprendizaje y comentarios. Acordar una meta de realización del ejercicio según el nivel del grupo, compartir los materiales disponibles y decidir juntos si conviene un segundo encuentro. La participación en el piloto no crea una alianza permanente ni exige futuras fechas.',dark=True)
add('Próximo paso','Llevemos la comunidad<br><em>a su universidad.</em>','<div class="university-next"><div><div class="meeting">20 min <span>para conocernos</span></div><div class="meeting-points"><span>Docente enlace</span><span>Público y objetivo</span><span>Fecha tentativa</span></div><a class="cta" href="'+URL+'" target="_blank" rel="noopener">Conocer Cloud Native Lima ↗</a></div><a class="university-qr" href="'+URL+'" target="_blank" rel="noopener" aria-label="Abrir Cloud Native Lima"><img src="{{QR}}" alt="QR de Cloud Native Lima"><span>Conozca la comunidad</span></a></div>','Propuesta de colaboración · Cloud Native University','Cierre sugerido para quien presenta: proponer una conversación de veinte minutos, identificar docente enlace y acordar un objetivo inicial. El QR abre la comunidad; no agenda una reunión. No se añade un correo institucional porque aún no se ha proporcionado. El equipo presentador coordina directamente con su contraparte; no se han enviado invitaciones ni confirmado alianzas.')


# La revisión incluye todas las fichas públicas; los registros de prueba se excluyen.
data=json.loads((ROOT/'revision-eventos-datos.json').read_text())
valid=[d for d in data if not d['title'].lower().startswith('test')]
def event_link(code,label):return '<a href="'+URL+'/event/'+code+'" target="_blank" rel="noopener">'+label+' ↗</a>'
def change(i,**kw):
 names=['title','headline','body','footer','note','dark','refs']
 row=list(slides[i])
 for k,v in kw.items():row[names.index(k)]=v
 slides[i]=tuple(row)
change(0,headline='El talento está en el campus.<br><em>La comunidad también.</em>',body='<div class="cover-grid"><div class="cover-brand"><img src="{{LOGO}}" alt="Cloud Native Lima · logo A"><p>Cloud Native <strong>University</strong></p><span>Aprender. Construir. Conectar.</span></div><div class="cover-invite"><span class="chip">INVITACIÓN A UNIVERSIDADES</span><h3>Su campus, nuestro<br>próximo encuentro.</h3><div class="campus-strip"><span>UNI</span><span>PUCP</span><span>UTEC</span></div><p>Tres ediciones universitarias en el historial.</p></div></div>',footer='Una iniciativa de Cloud Native Lima · Lima, Perú',refs=event_link('b6rhg7e','UNI')+' · '+event_link('kw8a6c8','PUCP')+' · '+event_link('jjmz4m4','UTEC'))
change(1,headline='De la comunidad<br><em>al aula.</em>',body=cards([('cloud','Ecosistema abierto','Cloud Native Lima · CNCF'),('school','University','Charlas y encuentros en campus'),('people','Aprendizaje compartido','Estudiantes + docentes + profesionales')]))
change(4,headline='Una ruta para<br><em>aprender haciendo.</em>')
change(5,headline='El próximo campus.<br><em>Un piloto a su medida.</em>')
change(8,headline='El encuentro termina.<br><em>El aprendizaje continúa.</em>')
# Dos láminas de trayectoria, con fuentes por evento.
old=slides[:]
slides=[]
add('University · trayectoria','Ya nos encontramos<br><em>en tres universidades.</em>','<div class="campus-grid">'+''.join('<a class="campus-card" href="'+URL+'/event/'+code+'" target="_blank" rel="noopener"><span class="edition">UNIVERSITY / '+num+'</span><h3>'+campus+'</h3><time>'+date+'</time><p>'+desc+'</p><span class="event-open">Ver evento ↗</span></a>' for num,campus,date,desc,code in [('01','UNI','11 OCT 2025','Cloud Native 101 · microservicios, Kubernetes y GitOps','b6rhg7e'),('02','PUCP','13 DIC 2025','Segundo encuentro · Facultad de Ciencias e Ingeniería','kw8a6c8'),('03','UTEC','25 ABR 2026','Introducción al ecosistema · contenedores e infraestructura','jjmz4m4')])+'</div>','Tres ediciones presenciales · 2025–2026','Revisión de las tres fichas University publicadas en OCG. UNI contiene una agenda detallada; PUCP no publica desglose de charlas; UTEC describe un enfoque introductorio. No se infieren asistencia, resultados ni convenios permanentes a partir de estas fichas.',refs=event_link('b6rhg7e','UNI')+' · '+event_link('kw8a6c8','PUCP')+' · '+event_link('jjmz4m4','UTEC'))
add('Más allá del campus','Una comunidad<br><em>que sigue aprendiendo.</em>','<div class="history-grid">'+''.join('<article class="history-card"><div class="history-top">'+icon(ic)+'<span>'+date+'</span></div><h3>'+title+'</h3><p>'+desc+'</p>'+event_link(code,label)+'</article>' for ic,date,title,desc,code,label in [('book','03–14 AGO 2026','KCNA Study Group','Cinco sesiones virtuales de preparación.','pdkhaus','Serie KCNA'),('people','09 JUL 2026','Pre-KCD · Interbank','Open Space sobre adopción cloud native.','r5kvxau','Ver encuentro'),('code','15 AGO 2025','Meetup #9','Kubernetes Release Shadow y FinOps.','w6dhfj8','Ver meetup'),('school','13 JUN 2026','KubeFest · URP','Apoyo a un evento de otras comunidades.','tu52ja4','Ver colaboración')])+'</div>','Estudio + industria + colaboración','KubeFest declara expresamente que Cloud Native Lima participa como soporte a otras comunidades. No se presenta como una cuarta edición University. KCNA incluye cinco sesiones el 3, 5, 7, 12 y 14 de agosto de 2026. Son preparación comunitaria, no certificaciones otorgadas por Cloud Native Lima. El Pre-KCD es distinto del KCD principal.',dark=True)
history=slides[:]
slides=old[:2]+history+old[2:]
# Anexo consultable: 30 fichas no marcadas como prueba, sin inflar la presentación principal.
for offset in range(0,len(valid),10):
 rows=[]
 for d in valid[offset:offset+10]:
  date=re.search(r'Event date (.*?) Location',d['text']).group(1)
  short=re.search(r'([A-Z][a-z]+ \d+, \d{4})',date).group(1)
  short=datetime.strptime(short,'%B %d, %Y').strftime('%d/%m/%Y')
  title=d['title']
  label='Colaboración' if 'KUBEFEST' in title else ('Archivo Perú' if int(short[-4:])<2020 else 'Comunidad')
  rows.append('<a class="archive-row" href="'+d['url']+'" target="_blank" rel="noopener"><time>'+short+'</time><span>'+html.escape(title)+'</span><small>'+label+' ↗</small></a>')
 add('Archivo · '+str(offset//10+1),'Nuestro historial.<em> '+str(offset//10+1)+' / 3</em>','<div class="archive-list">'+''.join(rows)+'</div>','Anexo · fichas públicas revisadas el 25/09/2026','Se revisaron las 34 fichas del historial público: cuatro registros test/testte se excluyen y se conservan 30 fichas. Seis pertenecen al archivo heredado Cloud Native Perú de 2018–2019; una corresponde a apoyo a KubeFest. Un registro publicado no demuestra asistencia efectiva ni valida automáticamente todos los datos de su descripción. El informe revision-eventos.md documenta las inconsistencias.',refs='<a href="'+URL+'" target="_blank" rel="noopener">Fuente: Open Community Groups ↗</a>')

sections=[]
for n,(title,headline,body,footer,note,dark,refs) in enumerate(slides,1):
 sections.append(f'<section class="slide organizer {"dark" if dark else ""}" data-title="{html.escape(title)}" aria-labelledby="title-{n}" {"hidden" if n>1 else ""}><p class="eyebrow">{n:02d} / CLOUD NATIVE UNIVERSITY</p><h2 id="title-{n}">{headline}</h2><div class="organizer-content">{body}</div><div class="bottomline"><span>{footer}</span><span class="source-links">{refs}</span></div><template class="speaker-note"><h3>{title}</h3><p>{html.escape(note)}</p><p>{refs}</p></template></section>')

base=(ROOT/'onboarding.template.html').read_text()
base=re.sub(r'<main class="stage".*?</main>','<main class="stage" id="deck" aria-label="Invitación a universidades">'+''.join(sections)+'</main>',base,flags=re.S)
base=base.replace('Organizadores · Cloud Native Lima','Cloud Native University · Invitación a universidades').replace('Onboarding de organizadores','Invitación a universidades').replace('aria-valuemax="15"','aria-valuemax="10"').replace('01 / 15','01 / 10')
base=base.replace('aria-valuemax="10"',f'aria-valuemax="{len(slides)}"').replace('01 / 10',f'01 / {len(slides)}')
base=re.sub(r'<meta name="description"[^>]+>','<meta name="description" content="Invitación a universidades: colaboración con Cloud Native Lima para experiencias prácticas de Cloud Native University.">',base)
base=re.sub(r'<style>.*?</style>', '<style>'+ (ROOT/'universidades.css').read_text()+'</style>',base,flags=re.S)
(ROOT/'universidades.template.html').write_text(base)
for name,path in {'{{LOGO}}':'identidad/kit-opcion-a/tamanos/azul/logo/logo-azul-800px.png','{{ICON}}':'identidad/kit-opcion-a/tamanos/azul/icono/icono-azul-512px.png','{{QR}}':'identidad/qr-comunidad.png'}.items():
 base=base.replace(name,'data:image/png;base64,'+base64.b64encode((ROOT/path).read_bytes()).decode())
for name in ['cloud-native-university.html','presentacion-universidades.html']:(ROOT/name).write_text(base)
print(f'Invitación universitaria: {len(slides)} diapositivas, logo A, HTML autónomo.')
