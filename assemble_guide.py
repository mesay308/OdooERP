# -*- coding: utf-8 -*-
import re
from head_block import HEAD
from sec1_4 import COVER, STICKY_HEADER, SEC1, SEC2, SEC3, SEC4
from sec5_7 import SEC5, SEC6, SEC7
from sec8_11 import SEC8, SEC9, SEC10, SEC11, BOTTOM_DOCK, SCRIPT

# Accordion: state is controlled by the .open class (not inline styles)
SEC6 = SEC6.replace(' style="display:none;"', '')
HEAD = HEAD.replace('grid-template-columns:1fr 1fr 1.4fr auto', 'grid-template-columns:1.7fr 1fr auto')
HEAD = HEAD.replace(
    '#sticky-header.hidden-up{transform:translateY(-110%);opacity:0;pointer-events:none;}',
    '#brand-bar{max-height:50px;overflow:hidden;transition:max-height .25s ease,padding .25s ease,opacity .2s ease;}\n#sticky-header.hidden-up #brand-bar{max-height:0;padding-top:0!important;padding-bottom:0!important;opacity:0;pointer-events:none;}'
)
SEC6 = SEC6.replace('<div class="acc-item" id="acc-6-1">', '<div class="acc-item open" id="acc-6-1">')

html = (HEAD + '\n<body>\n' + BOTTOM_DOCK + STICKY_HEADER + COVER +
        SEC1 + SEC2 + SEC3 + SEC4 + SEC5 + SEC6 + SEC7 + SEC8 + SEC9 + SEC10 + SEC11 +
        '\n<div style="height:12px;"></div>\n' + SCRIPT + '\n</body>\n</html>\n')

with open('addis_tech_odoo_guide.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('written', len(html), 'chars')
print('sections:', sorted(set(re.findall(r'id="(sec\d+)"', html)), key=lambda s: int(s[3:])))
print('accordions:', len(re.findall(r'class="acc-item', html)), '| open:', len(re.findall(r'class="acc-item open', html)))
print('industry panels:', len(re.findall(r'class="ind-panel', html)))
