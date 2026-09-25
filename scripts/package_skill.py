"""Empaqueta el skill portable sin cachés ni archivos del entorno local."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
ROOT=Path(__file__).resolve().parents[1]
source=ROOT/'skills/cloud-native-lima-slides'
output=ROOT/'cloud-native-lima-slides.zip'
with ZipFile(output,'w',ZIP_DEFLATED) as z:
    for path in sorted(source.rglob('*')):
        if path.is_file() and '__pycache__' not in path.parts and path.suffix!='.pyc' and path.name!='.DS_Store':
            z.write(path,path.relative_to(source.parent))
print(output)
