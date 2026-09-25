"""Construye una presentación autónoma: HTML con imágenes integradas."""
from pathlib import Path
import base64

ROOT=Path(__file__).resolve().parent
def asset(path):
    return 'data:image/png;base64,'+base64.b64encode((ROOT/path).read_bytes()).decode()

template=ROOT/'onboarding.template.html'
content=template.read_text(encoding='utf-8')
for name,path in {
    '{{LOGO}}':'identidad/kit-opcion-a/tamanos/azul/logo/logo-azul-800px.png',
    '{{ICON}}':'identidad/kit-opcion-a/tamanos/azul/icono/icono-azul-512px.png',
    '{{QR}}':'identidad/qr-comunidad.png',
}.items():
    content=content.replace(name,asset(path))
(ROOT/'onboarding-cloud-native-lima.html').write_text(content,encoding='utf-8')
print('Creado onboarding-cloud-native-lima.html · autónomo, sin dependencias externas.')
