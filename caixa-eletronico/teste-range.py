# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:30:00 2015

@author: papacheco
"""
num = input("Digite um numero:")
n = range(10,1001,10)
for p in n:
    if num == p:
        #print "SIM"
        res = "SIM"
        #print res
        break
    else:
        #print "Não"
        res = "NAO"
        #print res
       
print res