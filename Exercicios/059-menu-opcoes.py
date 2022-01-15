# 059 - Crie um programa que leia dois valores e mostre um menu como a seguir. Seu programa deverá realizar a operação solicitada em casa acesso: 
#[1]somar, [2]multiplicar, [3]maior, [4] novos números, [5] sair do programa

escolha=4

while escolha==4:
  n1 = int(input('Digite o primeiro número: '))
  n2 = int(input('Digite o segundo número: '))
  escolha = int(input('''Digite o número correspondente a operação que você deseja fazer:
  [1] somar
  [2] multiplicar
  [3] maior
  [4] novos números
  [5] sair do programa '''))
  if escolha==1:
    print(f'A soma entre os números {n1} e {n2} é igual a {n1+n2}')
  elif escolha ==2:
    print(f'A multiplicação entre os números {n1} e {n2} é igua a {n1*n2}')
  elif escolha == 3:
    if n1>n2: 
      print(f'O maior número entre {n1} e {n2} é o {n1}')
    else:
      print(f'O maior número entre {n1} e {n2} é o {n2}')      
  elif escolha==5:
    print('Sair do programa. ')
    pass
  else: 
    pass