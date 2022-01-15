# 016 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira:

from math import trunc

num = float(input(f'Digite um número qualquer: '))
print(f'A parte inteira do número é igual a {trunc(num)}')