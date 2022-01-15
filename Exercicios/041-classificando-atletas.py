# 041 - A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
#Até 9 anos: mirim
#Até 14 anos: infantil
#Até 19 anos: júnior
#Até 25 anos: senior
#Acima:master

from datetime import date

nasc = int(input('Qual o ano de nascimento do atleta? '))

ano_atual = date.today().year

idade = ano_atual - nasc

if idade <=9:
  print('Categoria: Mirim')
elif (idade>9) and (idade<=14):
  print('Categoria: Infantil')
elif (idade>14) and (idade<=19):
  print('Categoria: Junior')
elif (idade>19) and (idade<=25):
  print('Categoria: Senior')
else:
  print('Categoria: Master')