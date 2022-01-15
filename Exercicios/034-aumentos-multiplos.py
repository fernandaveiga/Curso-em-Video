# 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1250.00, 
#calcule um aumento de 10%. Para valores inferiores ou iguais, o aumento é de 15%:

salario = float(input('Digite o valor do salário: '))

if salario>1250.0:
  print(f'O salário é R${salario}, teve aumento de 10% e agora é R${salario*1.1}')
else:
  print(f'O salário é R${salario}, teve aumento de 15% e agora é R${salario*1.15}')  