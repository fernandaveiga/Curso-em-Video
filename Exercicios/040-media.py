# 040 - Crie um programa que receba duas notas de um aluno e calcule a média entre elas, mostrando uma mensagem no final, de acordo com a media atingida
#<5 reprovado, 5<=media<6.9 recuperação e media>=7 aprovado:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

if media<5:
  print(f'Média = {media}, REPROVADO')
elif (media>=5) and (media <6.9):
  print(f'Média = {media}, RECUPERAÇÃO')
else:
  print(f'Média = {media}, APROVADO')