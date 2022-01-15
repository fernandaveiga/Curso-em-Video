# 071 - Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado 
#(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues (cédulas podem ser R$50, R$20, R$10, R$1):

n = int(input('Digite o valor a ser sacado: '))
n50 = n//50
n2 = n%50
n20 = n2//20
n3 = n2%20
n10 = n3//10
n1 = n3%10
print(f'{n50} de R$50, {n20} de R$20, {n10} de R$10 e {n1} de R$1')
