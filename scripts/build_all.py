"""Regenera ambas presentaciones y el ejemplo desde el tema compartido."""
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
for script in ['crear_onboarding_organizadores.py','crear_invitacion_universidades.py']:
    subprocess.run([sys.executable,str(ROOT/script)],check=True,cwd=ROOT)
assets=ROOT/'skills/cloud-native-lima-slides/assets/template'
subprocess.run([sys.executable,str(assets/'render.py'),str(assets/'example.json'),'--output',str(ROOT/'plantilla-diapositivas.html')],check=True)
