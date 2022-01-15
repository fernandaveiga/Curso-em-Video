# 053 - crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderando espaços:

frase = input('Digite uma frase: ')
lista = []

frase = frase.replace(' ', '')

for pos, item in enumerate(frase):
  lista.insert(-pos, item)
if frase == (''.join(lista)):
  print('É palíndromo" ')
else:
  print('Não é palíndromo! ')
  