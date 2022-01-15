# 072 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero a vinte. Seu programa deverá ler um 
#número pelo teclado e mostrá-lo por extenso:

tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número de 0 a vinte: '))
print(f"Você digitou '{tupla[num]}'")