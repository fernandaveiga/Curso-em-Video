# 033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor: 

lista = []

for c in range(1,4):
  num = int(input(f'Digite um número: '))
  lista.append(num)

print(f'O maior valor é {max(lista)}')
print(f'O menor valor é {min(lista)}')