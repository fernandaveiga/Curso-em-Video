# 084 - Faça um programa que leia o nome o peso de várias pessoas, guardando tudo em uma lista. No final mostre: quantas pessoas
#foram cadastradas, uma listagem com as pessoas mais pesadas e uma listagem com as pessoas mais leves.

lista = []
listap = []
count = 0

while True:
  nome = input('Digite o nome da pessoa: ')
  lista.append(nome)
  peso = int(input('Digite o peso da pessoa: '))
  lista.append(peso)
  listap.append(peso)
  count = count+1
  resp = input('Deseja adicionar mais dados? [S ou N] ')
  if resp not in 'Ss':
    break
listap = sorted(listap)
print(listap)

print(f'O maior peso da lista é {listap[-1]}', end = ' ')
for pos, item in enumerate(lista):
  if item==listap[-1]:
    print(f'[{lista[pos-1]}]', end = ' ')

print(' ')

print(f'O menor peso da lista é {listap[0]}', end = ' ')
for pos, item in enumerate(lista):
  if item==listap[0]:
    print(f'[{lista[pos-1]}]', end = ' ')
      