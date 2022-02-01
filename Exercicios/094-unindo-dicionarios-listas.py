# 094 - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários 
#em uma lista. No final, mostre: Quantas pessoas foram cadastradas, a média de idade, uma lista de mulheres e uma lista com idade acima da média. 

lista = []
count = 0
soma = 0
listaf = []
listam = []

while True: 
  dicio = {}
  nome = input('Digite o nome: ')
  dicio['nome'] = nome
  sexo = input('Digite o sexo [M ou F]: ').upper()
  dicio['sexo'] = sexo
  idade = int(input('Digite a idade: '))
  dicio['idade'] = idade
  if sexo in 'fF':
    listaf.append(nome)
  count = count+1
  soma = soma+idade
  lista.append(dicio)
  resp = input('Deseja adicionar mais alguem [S ou N] ? ')
  if resp not in 'Ss':
    break
media = soma/count

print(lista)
print(' ')
print(f'''Temos {count} pessoas cadastradas. 
A média de idade entre elas é igual a {media}
As mulheres cadastradas são {listaf}. ''')
