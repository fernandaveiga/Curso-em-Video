# 044 - elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento: 
#a vista (dinheiro): 10% off, a vista (cartão): 5% off, em até 2x no cartão: preço normal, 3x ou mais no cartão: 20% juros

valor = float(input('Digite o valor do produto: '))
op = int(input('''Digite o número da opção de pagamento:
1: à vista no dinheiro
2: à vista no cartão
3: 2x no cartão
4: 3x ou mais no cartão '''))

if op==1:
  print(f'O valor a ser pago será R${valor*0.9}')
elif op==2:
  print(f'O valor a ser pago será R${valor*0.95}')
elif op==3:
  print(f'O valor a ser pago será R${valor}')  
elif op==4:
  print(f'O valor a ser pago será R${valor*1.2}')
else:
  print('Você não digitou uma opção válida. ')  