# 100 - Faça um programa que tenha uma lista chamada números e duas funções, chamadas somarpar() e sorteia(). A primeira função vai sortear 5 números
#e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

lista = []
count = 0
def sortear():
  from random import randint
  for c in range(1,6):
    n = randint(1,10)
    lista.append(n)
  print(lista)

def somapar():
  print(f'A soma entre os elementos da lista {lista} é igual a {sum(lista)}')


sortear()
somapar()