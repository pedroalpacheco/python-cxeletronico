# -*- coding: utf-8 -*-
"""
Created on Wed May 13 09:53:03 2015

@author: papacheco
"""
#O programa deverá perguntar ao usuário a valor do saque:
valor = input("Digite o valor do saque:")

#Aqui verifica se valor digitado é multiplo de 10, analisa range de 10 a 1000 de 10 em 10
n = range(10,1001,10)
for p in n:
    if valor == p:
        #print "SIM"
        res = "SIM"
        #print res
        break
    else:
        #print "Não"
        res = "NAO"
        #print res
        
#O valor mínimo é de 10 reais e o máximo de 1000 reais
if valor < 10:
    print "Não é permitido valores menor que R$ 10,00"
elif valor > 1000:
    print "Para sua segurança o valor maximo para saque é R$1.000,00"
elif res == "NAO":
    print "E permitido somente retirada de notas de multiplos de R$ 10,00!"
#Verifica o valor de notas
else:
    for p in 100,50,20,10:
        if valor >= p:
            n = valor / p
            r = valor - p * n
            print ">> Extraido %s nota(s) de R$ %s." % (n, p)
            valor = r

#depois informar quantas notas de cada valor serão fornecidas.
#disponíveis serão as de 10, 20, 50 e 100 .

