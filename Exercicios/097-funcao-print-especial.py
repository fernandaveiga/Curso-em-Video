# 097 - Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mopstre uma mensagem com tamanho adaptável

def escreva(frase):
  print('-'*(len(frase)+4))
  print(f'  {frase.upper()}  ')
  print('-'*(len(frase)+4))

frase = input('Digite a frase: ')
escreva(frase)