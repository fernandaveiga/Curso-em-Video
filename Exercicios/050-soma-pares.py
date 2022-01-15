# 050 = Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquelas que forem pares. Se o valor digitado for ímpar, desconsidere:

lista = []
soma = 0

for c in range(1,7):
  num = int(input(f'Digite o {c}° número inteiro: '))
  lista.append(num)
print(lista)

for c in lista:
  if c%2==0:
    soma = soma+c
print(soma)