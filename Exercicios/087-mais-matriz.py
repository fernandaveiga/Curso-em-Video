# 087 - Refaça o exercício anterior e mostre: a) a soma de todos os valores pares digitados. b) A soma dos valores da terceira coluna. 
#c) O maior valor da segunda linha.

lista = [[],[],[]]
soma = 0
soma3 = 0

for l in range(0,3):
  for c in range(0,3):
    n = int(input(f'Digite o [{l}][{c}] número para a matriz: '))
    lista[l].append(n)
print(f'''{lista[0]} 
{lista[1]}
{lista[2]}''')
print(' ')

for c in lista:
  for d in c:
    if d%2==0:
      soma = soma +d
print(f'A soma dos números pares é igual a {soma}')

for c in range(0,3):
  soma3 = soma3+ lista[c][2]
print(f'A soma dos números da terceira coluna é igual a {soma3}')
print(f'O número máximo da segunda linha é igual a {max(lista[1])}')