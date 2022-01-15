# 076 - Crie um programa que tenha uma tupla única com nomes de prosutos e seus respectivos preços, na sequenciA. No final, mostre 
#uma listagem de preços, organizando os dados de forma tabular:

listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

print('LISTAGEM DE PREÇOS')
for pos, item in enumerate(listagem):
  if pos%2==0: 
    n = 30-len(item)
    print(f'{item}', end = '-'*n)
  else:
    print(f'R${item:>7.2f}', end = '')
    print(f' ')
