# 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo:

import math

ang = float(input(f'Digite o angulo: '))

seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))

print(f'O seno equivale a {seno}, o cosseno equivale a {cos} e a tangente a {tg}')