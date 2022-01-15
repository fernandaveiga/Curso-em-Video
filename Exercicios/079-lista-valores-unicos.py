# 079 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, 
#ele não será cadastrado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente:

lista = []
resp = 'S'

while resp=='S': 
  n = int(input('Digite um número: '))
  if n not in lista:
    lista.append(n)
  resp = input('Você deseja adicionar mais um número? ').upper()

print(f'Em ordem crescente, os valores únicos digitados foram {sorted(lista)}')
