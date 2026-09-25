"""Acceso al motor incluido en el skill; una única fuente de diseño."""
from pathlib import Path
import importlib.util
path=Path(__file__).resolve().parent/'skills/cloud-native-lima-slides/assets/template/render.py'
spec=importlib.util.spec_from_file_location('cloud_native_slide_renderer',path)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
render_document=module.render_document
section=module.section
icon=module.icon
cards=module.cards
flow=module.flow
