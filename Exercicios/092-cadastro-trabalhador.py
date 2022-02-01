# 092 - Crie um programa que leia, nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a carteira 
#de trabalho for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, alem da idade, com quantos anos a apessoa vai se aposentar.

from datetime import date
atual = date.today().year
dicio = {}

nome = input('Digite o nome: ')
dicio['nome'] = nome
nasc = int(input('Digite o ano de nascimento: '))
dicio['nasc'] = nasc
cart = int(input('Carteira de trabalho (0 se não tem): '))
ano = date.today().year
idade = ano-nasc
dicio['idade']=idade
if cart !=0:
  dicio['cart'] = cart
  contr = int(input('Digite o ano de contratação: '))
  dicio['contr'] = contr
  sal = float(input('Digite o salário: '))
  dicio['sal'] = sal
  apos = idade+30
  dicio['apos'] = apos

print(f'''Nome = {dicio['nome']}
Data de nascimento: {dicio['nasc']} 
Idade: {dicio['idade']}
Carteira de trabalho: {dicio['cart']}
Salário: {dicio['sal']}
A aposentadoria será com {dicio['apos']} anos.''')
