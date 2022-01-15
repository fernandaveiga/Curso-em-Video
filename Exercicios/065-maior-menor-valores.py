# 065 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o 
#maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores:

resp = 'S'
soma = 0 
count = 0
lista = []

while resp == 'S':
  n = int(input('Digite um número: '))
  soma = soma+n
  count = count+1
  lista.append(n)
  resp = input('Deseja adicionar mais um número? [S ou N] ').upper().strip()

print(f'A média dos números é igual a {soma/count}')
print(f'O maior valor é {max(lista)}')