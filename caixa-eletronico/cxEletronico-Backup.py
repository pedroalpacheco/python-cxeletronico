# -*- coding: utf-8 -*-
"""
Created on Wed May 13 09:53:03 2015

@author: papacheco
"""
#O programa deverá perguntar ao usuário a valor do saque:
valor = input("Digite o valor do saque:")
#O valor mínimo é de 10 reais e o máximo de 600 reais
if valor < 10:
    print "Não é permitido valores menor que R$ 10,00"
elif valor > 1000:
    print "Para sua segurança o valor maximo para saque é R$1.000,00"


else:
    for p in 100,50,20,10:
        if valor >= p:
            n = valor / p
            r = valor - p * n
            print ">> Extraido %s nota(s) de R$ %s." % (n, p)
            valor = r

#depois informar quantas notas de cada valor serão fornecidas.
#disponíveis serão as de 10, 20, 50 e 100 .
#Verificar de valor é com ultimo digito de zero.
