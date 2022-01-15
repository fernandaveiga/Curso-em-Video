# 082 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão 
#conter apenas os valores pares e os valores ímpares digitados. Ao final, mostre o conteúdo das três listas geradas:

lista = []
listapar = []
listaimpar = []

while True:
  n = int(input('Digite um número: '))
  lista.append(n)
  if n%2==0:
    listapar.append(n)
  else:
    listaimpar.append(n)
  resp = input('Deseja adicionar mais um número? [S ou N] ').upper()
  if resp not in 'Sn':
    break

print(f'A lista gerada é: {lista}')
print(f'A lista de números ímpares gerada é: {listaimpar}')
print(f'A lista de números pares gerada é: {listapar}')
