# 049 - refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for:

n = int(input('Digite um número inteiro para calcularmos a tabuada: '))

for c in range(1,11):
  print(f'{n} x {c} = {n*c}')