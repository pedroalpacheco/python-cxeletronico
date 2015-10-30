# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:25:58 2015

@author: papacheco
"""
import os

valordez = input("Digite quantidade de notas R$ 10,00:")
os.chdir("/home/papacheco/Dropbox/scripts/python/Exercicios/Exercicio2/caixa-eletronico/10")
nota = "dez-reais"
for i in range(valordez):
    vl = "%s-%s" % (i,nota)
    fo = open(vl, "wb")
    
valorvinte = input("Digite a quantidade de notas R$ 20,00:")
os.chdir("/home/papacheco/Dropbox/scripts/python/Exercicios/Exercicio2/caixa-eletronico/20")
nota = "vinte-reais"
for i in range(valorvinte):
    vl = "%s-%s" % (i,nota)
    fo = open(vl, "wb")
    
valorcinquenta = input("Digite a quantidade notas R$ 50,00:")
os.chdir("/home/papacheco/Dropbox/scripts/python/Exercicios/Exercicio2/caixa-eletronico/50")
nota = "cinquenta-reais"
for i in range(valorcinquenta):
    vl = "%s-%s" % (i,nota)
    fo = open(vl, "wb")
    
valorcem = input("Digite a quantidade de notas  R$ 100,00:")
os.chdir("/home/papacheco/Dropbox/scripts/python/Exercicios/Exercicio2/caixa-eletronico/100")
nota = "cem-reais"
for i in range(valorcem):
    vl = "%s-%s" % (i,nota)
    fo = open(vl, "wb")