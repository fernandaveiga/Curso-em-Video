# 045 - Crie um programa que jogue joquenpô com você:

import random

lista = ['pedra', 'papel', 'tesoura']

comp = random.choice(lista)
voce = str(input('Digite pedra, papel ou tesoura para jogar: ')).lower().strip()

if comp==voce:
  print(f'Você jogou {voce}, o computador jogou {comp}. Vocês empataram.')
elif comp=='papel' and voce=='pedra':  
  print(f'Você jogou {voce}, o computador jogou {comp}. O computador ganhou.')
elif comp =='pedra'  and voce == 'papel':
  print(f'Você jogou {voce}, o computador jogou {comp}. Você ganhou!')
elif comp== 'papel' and voce=='tesoura':
  print(f'Você jogou {voce}, o computador jogou {comp}. Você ganhou!')  
elif comp== 'tesoura' and voce=='papel':
  print(f'Você jogou {voce}, o computador jogou {comp}. O computador ganhou!')  
elif comp=='tesoura' and voce=='pedra':
  print(f'Você jogou {voce}, o computador jogou {comp}. Você ganhou!')
elif comp=='pedra' and voce=='tesoura':
  print(f'Você jogou {voce}, o computador jogou {comp}. O computador ganhou!') 
else:
  print('Você não digitou uma opção válida. ')    