# 027 - Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente:

nome = str(input('Digite o nome completo: '))

nome = nome.split()

print(f'O primeiro nome é: {nome[0]}')
print(f'O segundo nome é: {nome[-1]}')