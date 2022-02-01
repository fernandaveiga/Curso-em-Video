# 095 - Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do 
#aproveitamento de cada jogador

lista0 = []
dicio = {}

while True: 
  lista = []
  nome = input('Digite o nome: ') 
  dicio['nome'] = nome
  n = int(input(f'Digite o número de partidas que o {nome} jogou: '))
  dicio['partidas'] = n
  for c in range(1, n+1):
    gol = int(input(f'Quantos gols o {nome} fez na partida {c}? '))
    lista.append(gol)
  dicio['gols']=lista
  dicio['tgols'] = sum(lista)
  lista0.append(dicio.copy())
  resp = input('Deseja adicionar alguem? [S/N] ')
  if resp not in 'Ss':
    break

print(lista0)
print(' ')
print('cod ', end = '')
for c in dicio.keys():
  print(f'{c:<15}', end = '')
print(' ')

for pos, item in enumerate(lista0):
  print(f'{pos:>3}', end =' ')
  for f in item.values():
    print(f'{str(f):<15}', end = ' ')
  print(' ')
print(' ')
