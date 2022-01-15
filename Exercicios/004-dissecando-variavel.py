# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela:

algo = input('Digite algo: ')
print(f'O tipo primitivo é {type(algo)}')
print(f'É um número? ', algo.isnumeric())
print(f'É composto apenas por espaços? ', algo.isspace())
print(f'É composto somente por letras? ', algo.isalpha())
print(f'É composto por números e letras? ', algo.isalnum())
print(f'É composto somente por letras minusculas? ', algo.islower())
print(f'É composto somente por letras maiúsculas? ', algo.isupper())
print(f'Está capitalizada? ', algo.istitle())