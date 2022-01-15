#062 - Melhore o exercicio anterior, perguntando ao usuário se ele gostaria de ver mais números da PA.
 
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão dessa PA: '))

n=primeiro
print(primeiro, end = ' ')
while n<(primeiro+(razao*9)):
  n = n+razao
  print(n, end = ' ')

primeiro = primeiro+(razao*9)
resp = 'S'
resp = input('Deseja obter mais números dessa PA? [S ou N] ').upper()
if resp == 'S':
  num = int(input('Quantos números a mais você deseja obter? '))
  for c in range(primeiro+razao, primeiro+(num*razao)+razao, razao):
    print(c, end = ' ')
elif rest =='N':
  pass
else:
  print('Você não digitou uma opção válida. ')