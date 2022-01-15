# 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Caso esteja errado, peça a digitação novamente
#até ter um valor correto:

sexo = 'k'
while sexo!='F' and sexo!='M':
  sexo = str(input('Digite o sexo da pessoa: ')).strip()
  if sexo =='F' or sexo=='M':
    print(f'O sexo da pessoa é {sexo}')
  else:
    print('Você não digitou uma opção válida.')
