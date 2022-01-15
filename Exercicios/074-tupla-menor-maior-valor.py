# 074 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados 
#e também indique o menor e o maior número que estão nessa tupla:

from random import randint

n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'Os valores sortados foram: {n}, o maior valor é {max(n)} e o menor é {min(n)}')