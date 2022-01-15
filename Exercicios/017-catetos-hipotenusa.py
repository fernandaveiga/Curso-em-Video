# 017 - Faça um programa que leia o comprimento do cateto oposto e adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa:

ca = int(input(f'Digite o cateto adjacente: '))
co = int(input(f'Digite o cateto oposto: '))

hi = ((ca**2)+(co**2))**(1/2)
print(f'A medida da hipotenusa é igual a {hi}')