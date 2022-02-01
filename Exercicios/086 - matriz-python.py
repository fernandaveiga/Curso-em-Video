# 086 - Crie um progreama que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, 
#com a formatação correta:

lista = [[], [], []]

for c in range(0,3):
  n = int(input(f'Digite o número [0][{c}] para a matriz: '))
  lista[0].append(n)
for c in range(0,3):
  n = int(input(f'Digite o número [1][{c}] para a matriz: '))
  lista[1].append(n)
for c in range(0,3):
  n = int(input(f'Digite o número [2][{c}] para a matriz: '))
  lista[2].append(n)
print(' ')

print(f'[{lista[0][0]}] [{lista[0][1]}] [{lista[0][2]}]')
print(f'[{lista[1][0]}] [{lista[1][1]}] [{lista[1][2]}]')
print(f'[{lista[2][0]}] [{lista[2][1]}] [{lista[2][2]}]')