"""Instala una copia del skill para Codex, Claude Code o ambos."""
from pathlib import Path
import argparse
import os
import shutil

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--target',choices=['codex','claude','both'],default='both')
parser.add_argument('--update',action='store_true',help='Actualizar una instalación existente de este skill')
args=parser.parse_args()
source=ROOT/'skills/cloud-native-lima-slides'
bases={'codex':Path(os.environ.get('CODEX_HOME',str(Path.home()/'.codex')))/'skills','claude':Path.home()/'.claude/skills'}
targets=[base/source.name for name,base in bases.items() if args.target in (name,'both')]
for target in targets:
    if target.exists():
        marker=target/'SKILL.md'
        if not args.update or not marker.is_file() or 'name: cloud-native-lima-slides' not in marker.read_text():
            parser.error(f'Ya existe {target}. Revisar antes de usar --update.')
for target in targets:
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copytree(source,target,dirs_exist_ok=args.update,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    print(target)
