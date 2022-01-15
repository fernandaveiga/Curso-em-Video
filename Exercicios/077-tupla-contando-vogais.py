# 077 - Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você dve mostrar, para cada palavra, 
#quais são as suas vogais:

tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for c in tupla:
  print(f'Na palavra {c} temos', end = ' ')
  for d in c:
    if d in 'aeiou':
      print(d, end = ' ')
  print(' ')