# 023 - Faça um programa que leia um número do 0 ao 9999 e mostre na tela cada um dos dígitos separados

num = int(input('Digite um número do 1 ao 9999: '))
milhar = num//1000
resto1 = num%1000
print(f'A unidade de milhar é igual a {milhar}')
centena = resto1//100
resto2 = resto1%100
print(f'A unidade da centena é igual a {centena}')
dezena = resto2//10
resto3 = resto2%10
print(f'A unidade de dezena é igual a {dezena}')
unidade = resto3
print(f'A unidade é igual a {unidade}')