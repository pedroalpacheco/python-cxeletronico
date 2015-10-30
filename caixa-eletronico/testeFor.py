# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:34:16 2015

@author: papacheco
"""
import os

os.chdir("/home/papacheco/Dropbox/scripts/python/Exercicios/Exercicio2/caixa-eletronico/10")
nota = "dez-reais"
for i in range(6):
    vl = "%s-%s" % (i,nota)
    fo = open(vl, "wb")