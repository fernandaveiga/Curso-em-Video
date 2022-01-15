# 036 - Escreva um programa para aprovar emprestimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos 
#anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado:

vcasa = float(input('Qual o valor da casa? '))
scomp = float(input('Qual o salário do comprador? '))
anos = int(input('Em quantos anos o empréstimo será pago? '))

pmensal = vcasa/(anos*12)

if pmensal < 0.3*scomp:
  print('O empréstimo poderá ser feito. ')
else:
  print('O empréstimo não será feito. ')