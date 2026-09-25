"""Invariantes del generador: salida autónoma y contenido tratado como texto."""
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from slidekit import module as renderer

class RendererTests(unittest.TestCase):
    def test_all_layouts_are_standalone(self):
        data=json.loads((renderer.ROOT/'example.json').read_text())
        result=renderer.build(data)
        self.assertEqual(result.count('<section class="slide'),len(data['slides']))
        self.assertIn('data:image/png;base64,',result)
        self.assertNotIn('{{',result)
        self.assertNotIn('<script src=',result)
        self.assertNotIn('<link rel="stylesheet"',result)

    def test_untrusted_text_cannot_become_markup(self):
        data={'title':'<script>alert(1)</script>','slides':[{'layout':'cards','title':'A & B','items':[{'title':'<img src=x onerror=alert(1)>','text':'<b>literal</b>'},{'title':'Dos'}]}]}
        result=renderer.build(data)
        self.assertNotIn('<img src=x',result)
        self.assertIn('&lt;img',result)
        self.assertIn('A &amp; B',result)

    def test_rejects_unsafe_links(self):
        with self.assertRaises(ValueError):
            renderer.build({'title':'T','slides':[{'layout':'links','title':'T','items':[{'title':'A','url':'javascript:alert(1)'},{'title':'B','url':'https://example.com'}]}]})

    def test_rejects_empty_deck_and_unknown_layout(self):
        for slides in [[],[{'title':'T','layout':'unknown'}]]:
            with self.assertRaises(ValueError):renderer.build({'title':'T','slides':slides})

if __name__=='__main__':unittest.main()
