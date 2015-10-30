# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 10:20:39 2015

@author: papacheco
"""
import os
nota = "ok.txt"
# Open a file
os.chdir("/home/papacheco/Dropbox/scripts/python/Exercicios/Exercicio2/caixa-eletronico/100")
fo = open(nota, "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace
fo.close();

