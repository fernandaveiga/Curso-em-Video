# 081 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#a) quantos números foram digitados
#b) A lista de valores, ordenada de forma decrescente
#c) Se o valor 5 foi digitado e está ou não na lista

lista = []
resp = 'S'
count = 0

while resp=='S':
  n = int(input('Digite um número:'))
  lista.append(n)
  count = count+1
  resp = input('Deseja digitar outro número? [S ou N] ').upper()

print(f'Foram digitados {count} números')
lista.sort(reverse = True)
print(f'A lista digitada, em forma decrescente é {lista}')
if 5 in lista:
  print('O número 5 está na lista. ')
else:
  print('O número 5 não está na lista. ')
