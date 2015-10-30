# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:49:30 2015

@author: papacheco
"""
#contador de troco

preco = int(raw_input("Digite o valor da compra:"))
dinheiro = int(raw_input("Digite a quantia de dinheiro entregue: "))
print

troco = dinheiro - preco


if troco > 0:
    print "Valor do troco: R$ %s." % troco
    print
    
#for p in 100, 50, 20, 10, 5, 2, 1:
    for p in 100,50,20,10,5,2,1:
        if troco >= p:
            n = troco / p
            r = troco - p * n
            print ": %s nota(s) de R$ %s." % (n, p)
            troco = r
else:
    print "O dinheiro entregue é menor do que o valor da compra."