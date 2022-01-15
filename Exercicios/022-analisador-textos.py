# 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas
#quantas letras ao todo (sem considerar espaços)
#quantas letras tem o primeiro nome

nome = str(input(f'Digite o nome completo: '))
print(f'O nome com todas as letras maiúsculas é {nome.upper()} e minúsculas é {nome.lower()}')

nome = nome.split()
tam = len(nome[0])
nome = ' '.join(nome)

nome = nome.replace(' ', '')

print(f'O total de letras do nome é {len(nome)}')
print(f'O total de letras do primeiro nome é {tam}')