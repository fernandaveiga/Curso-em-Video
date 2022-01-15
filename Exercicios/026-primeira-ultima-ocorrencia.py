# 026 - Faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a palavra 'A'
#Em que posição ela aparece pela primeira vez
#Em que posição ela aparece pela ultima vez

frase = str(input('Digite uma frase: '))
frase = frase.lower().strip()
lista = []

count = frase.count('a')
find = frase.find('a')
rfind = frase.rfind('a')
print(f'O número de vezes que a letra A aparece é {count}')
print(f'A posição que a letra a aparece pela primeira vez é {find+1}')
print(f'A última posição que a letra A é encontrada é {rfind+1}')