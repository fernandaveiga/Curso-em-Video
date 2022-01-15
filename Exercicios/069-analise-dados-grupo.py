# 069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer 
#ou não continuar. no final, mostre:
#a - Quantas pessoas tem mais de 18 anos
#b - Quantos homens foram cadastrados
#c - Quantas mulheres tem menos de 20 anos

resp = 'S'
count18 = 0
counth = 0
countm = 0

while resp == 'S':
  idade = int(input('Digite a idade da pessoa: '))
  if idade>18:
    count18 = count18+1
  sexo = str(input('Digite o sexo da pessoa. F ou M : ')).upper().strip()
  if sexo=='M':
    counth = counth+1
  elif sexo=='F':
    if idade<20:
      countm = countm+1
    else:
      pass
  else:
    print('Voce não digitou um sexo válido. ')
  resp = input('Deseja adicionar mais alguem a esta lista? [S ou N] ').upper().strip()


print(f'Há {count18} pessoas com mais de 18 anos. ')
print(f'Há {counth} homens nesta lista. ')
print(f'Há {countm} mulheres com menos de 20 anos. ')