# 048 - faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de tres e que se encomtram no intervalo de 1 até 50:

soma = 0
for c in range(1,500, 2):
  if c%3==0: 
    soma = soma+c
print(soma)