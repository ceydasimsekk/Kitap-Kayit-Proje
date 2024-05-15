# -*- coding: utf-8 -*-
"""
Created on Wed May 17 13:28:48 2023

@author: MONSTER
"""

from PyQt5 import uic

with open('AnaSayfaUI.py', 'w', encoding="utf-8") as fout:
   uic.compileUi('AnaSayfa.ui', fout)