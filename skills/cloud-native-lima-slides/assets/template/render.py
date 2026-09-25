"""Renderiza decks JSON como HTML autónomo. Python 3, sin dependencias."""
from pathlib import Path
import argparse
import base64
import html
import json
import re
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parent
ICONS=json.loads((ROOT/'icons.json').read_text())

def esc(value):
    return html.escape(str(value),quote=True)

def url(value):
    if urlparse(value).scheme not in ('https','http','mailto'):
        raise ValueError('Los enlaces requieren https, http o mailto: '+value)
    return esc(value)

def icon(name):
    if name not in ICONS:
        raise ValueError('Icono desconocido: '+name)
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+ICONS[name]+'</svg>'

def cards(items):
    return f'<div class="tiles cols-{len(items)}">'+''.join('<article class="tile">'+icon(i)+'<h3>'+esc(h)+'</h3><p>'+esc(t)+'</p></article>' for i,h,t in items)+'</div>'

def flow(items):
    return f'<div class="flow cols-{len(items)}">'+''.join(f'<article class="flow-step"><span class="stepno">{n:02d}</span>'+icon(i)+'<h3>'+esc(h)+'</h3><p>'+esc(t)+'</p></article>' for n,(i,h,t) in enumerate(items,1))+'</div>'

def section(n,title,headline,body,footer='',note='',dark=False,refs='',label='CLOUD NATIVE LIMA'):
    # headline/body/refs son HTML de componentes internos, nunca texto sin escapar del JSON.
    return f'<section class="slide organizer {"dark" if dark else ""}" data-title="{esc(title)}" aria-labelledby="title-{n}" {"hidden" if n>1 else ""}><p class="eyebrow">{n:02d} / {esc(label)}</p><h2 id="title-{n}">{headline}</h2><div class="organizer-content">{body}</div><div class="bottomline"><span>{esc(footer)}</span><span class="source-links">{refs}</span></div><template class="speaker-note"><h3>{esc(title)}</h3><p>{esc(note)}</p><p>{refs}</p></template></section>'

def render_document(title,subtitle,sections):
    if not sections:
        raise ValueError('La presentación necesita al menos una diapositiva.')
    values={'TITLE':esc(title),'SUBTITLE':esc(subtitle),'COUNT':str(len(sections)),
            'CSS':(ROOT/'theme.css').read_text(),'SLIDES':''.join(sections)}
    for key,filename in [('LOGO','logo.png'),('ICON','icon.png'),('QR','qr.png')]:
        values[key]='data:image/png;base64,'+base64.b64encode((ROOT/filename).read_bytes()).decode()
    # Dos pasadas: los componentes también pueden incluir imágenes del tema.
    text=(ROOT/'shell.html').read_text()
    for _ in range(2):
        text=re.sub(r'\{\{(TITLE|SUBTITLE|COUNT|CSS|SLIDES|LOGO|ICON|QR)\}\}',lambda m:values[m[1]],text)
    return text

def items_for(slide,minimum,maximum):
    items=slide.get('items',[])
    if not minimum<=len(items)<=maximum:
        raise ValueError(f"{slide['layout']}: se requieren entre {minimum} y {maximum} elementos")
    return items

def component(s):
    layout=s['layout']
    if layout=='cover':
        tags=''.join('<span>'+esc(t)+'</span>' for t in s.get('tags',[])[:3])
        return '<div class="cover-grid"><div class="cover-brand"><img src="{{LOGO}}" alt="Cloud Native Lima"><p>'+esc(s.get('series','Cloud Native Lima'))+'</p><span>'+esc(s.get('tagline','Aprender. Construir. Conectar.'))+'</span></div><div class="cover-invite"><span class="chip">'+esc(s.get('badge','COMUNIDAD'))+'</span><h3>'+esc(s['message'])+'</h3><div class="campus-strip">'+tags+'</div></div></div>'
    if layout in ('cards','flow'):
        items=[(i.get('icon','cloud'),i['title'],i.get('text','')) for i in items_for(s,2,4)]
        return cards(items) if layout=='cards' else flow(items)
    if layout=='metrics':
        return '<div class="metrics">'+''.join('<article><strong>'+esc(i['value'])+'</strong><h3>'+esc(i['title'])+'</h3><p>'+esc(i.get('text',''))+'</p></article>' for i in items_for(s,3,3))+'</div>'
    if layout=='split':
        return '<div class="partnership">'+''.join('<article><div class="party-label">'+esc(i.get('label',''))+'</div><h3>'+esc(i['title'])+'</h3><ul>'+''.join('<li>'+esc(t)+'</li>' for t in i['points'])+'</ul></article>' for i in items_for(s,2,2))+'</div>'
    if layout=='links':
        return '<div class="reading-grid">'+''.join('<a href="'+url(i['url'])+'" target="_blank" rel="noopener">'+icon(i.get('icon','link'))+'<span>'+esc(i['title'])+'</span><b>↗</b></a>' for i in items_for(s,2,6))+'</div>'
    if layout=='closing':
        community='https://ocgroups.dev/cncf/group/nmmzkrs'
        return '<div class="university-next"><div><div class="meeting">'+esc(s['callout'])+'<span>'+esc(s['message'])+'</span></div><div class="meeting-points">'+''.join('<span>'+esc(t)+'</span>' for t in s.get('tags',[])[:3])+'</div><a class="cta" href="'+community+'" target="_blank" rel="noopener">Conocer la comunidad ↗</a></div><a class="university-qr" href="'+community+'" target="_blank" rel="noopener"><img src="{{QR}}" alt="QR de Cloud Native Lima"><span>Conozca la comunidad</span></a></div>'
    raise ValueError('Layout desconocido: '+layout)

def build(data):
    slides=data['slides']
    if not isinstance(slides,list) or not slides:
        raise ValueError('slides debe ser una lista no vacía')
    sections=[]
    for n,s in enumerate(slides,1):
        headline=esc(s['title'])
        if s.get('accent'):headline+='<br><em>'+esc(s['accent'])+'</em>'
        refs=' · '.join('<a href="'+url(r['url'])+'" target="_blank" rel="noopener">'+esc(r['label'])+' ↗</a>' for r in s.get('sources',[]))
        sections.append(section(n,s['title'],headline,component(s),s.get('footer',''),s.get('notes',''),s.get('dark',False),refs,data.get('label','CLOUD NATIVE LIMA')))
    return render_document(data['title'],data.get('subtitle','Presentación de la comunidad'),sections)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path,help='Archivo JSON de contenido')
    parser.add_argument('--output',required=True,type=Path,help='HTML de salida')
    args=parser.parse_args()
    try:
        result=build(json.loads(args.input.read_text()))
    except (ValueError,KeyError,TypeError) as error:
        parser.error(str(error))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(result)
    print(args.output)

if __name__=='__main__':main()
