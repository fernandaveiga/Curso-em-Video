# 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo':

cidade = str(input('Digite o nome da cidade: '))
cidade1 = cidade
cidade = cidade.lower()
cidade = cidade.split()
if cidade[0] == 'santo':
  print(f"A cidade {cidade1} tem o primeiro nome 'Santo'")
else:
  print(f"A cidade {cidade1} não tem o primeiro nome 'Santo'")