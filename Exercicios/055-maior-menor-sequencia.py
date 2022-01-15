# 055 - Faça um programa que leia o peso de 5 pessoas e no final diga qual foi o maior e o menor peso:

lista = []

for c in range(1, 6):
  peso = float(input(f'Informe o {c} peso: '))
  lista.append(peso)

print(f'O maior peso da lista é {max(lista)} e o menor é {min(lista)}')
