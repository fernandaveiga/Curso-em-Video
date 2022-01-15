# 085 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que contenha separados 
#os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente:

lista = [[], []]

for c in range(1,8):
  n = int(input(f'Digite o {c}° valor: '))
  if n%2==0:
    lista[0].append(n)
  else:
    lista[1].append(n)

print(f'A lista de números pares em ordem crescente é {sorted(lista[0])}')
print(f'A lista de números ímpares em ordem crescente é {sorted(lista[1])}')
print(lista)