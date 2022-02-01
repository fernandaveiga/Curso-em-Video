# 098 - Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo. 
#Seu programa tem que realizar três contagens através da função criada: 

from time import sleep

def contagem(ini, fim, pas):
  if ini<=fim:
    for c in range(ini, fim+1, pas):
      print(f'{c}', end = ' ')
      sleep(0.5)
    print()
  else:
    for c in range(ini, fim-1, -pas):
      print(f'{c}', end = ' ')
      sleep(0.5)
    print()
  print('-='*17)        

print('Contagem de 1 até 10 de 1 em 1')
contagem(1,11,1)

print('Contagem de 10 até 0 de 2 em 2')
contagem(10,0,2) 

ini = int(input('Digite o início da sequencia: '))
fim = (int(input('Digite o fim da sequencia: ')))
pas = int(input('Digite de quanto em quanto a sequencia deve ir: '))
contagem(ini, fim, pas)
