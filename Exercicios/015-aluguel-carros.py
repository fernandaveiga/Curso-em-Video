# 015 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias 
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

km = float(input(f'Quantos quilometros o carro percorreu? '))
dias = int(input(f'Quantos dias o carro ficou alugado? '))

pagar = (km*0.15)+(dias*60)
print(f'O total a pagar será: R${pagar}')