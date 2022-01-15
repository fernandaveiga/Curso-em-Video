# 073 - Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação, depois mostre:
# a) os 5 primeiros, b) os últimos 4 colocados, c) times em ordem alfabética, d) Em que posição está o chapecoense

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético PR', 'Bahia', 
         'São Paulo', 'Fluminense', 'Sport Recife', 'Ec Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético GO')

print('Os cinco primeiros colocados são: ')
for pos, item in enumerate(times):
  if pos<=5:
    print(f'{pos}°: {item}')
print(' ')
print('Os quatro últimos são: ')
for c in range(1,5):
  print(f'{times[-c]}')

print(' ')
print(f'Os times em ordem alfabética são {sorted(times)}')

print(' ')
print(f'A chapecoense está em ', end = '')
for pos, item in enumerate(times):
  if item=='Chapecoense':
    print(f'{pos+1}° lugar')