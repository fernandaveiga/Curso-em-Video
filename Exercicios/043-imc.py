# 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IKC e mostre seu status, de acordo com a tabela abaixo:
#<18.5:abaixo do peso, <25: peso ideal, <30:sobrepeso, <40: obesidade, >40: obesidade morbida

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))
imc = peso/(altura*altura)

if imc<18.5:
  print(f'O IMC é {imc} e está abaixo do peso. ')
elif (imc>=18.5) and (imc<25):
  print(f'O IMC é {imc} e você está com um peso normal. ')
elif (imc>=25) and (imc<30):
  print(f'O IMC é {imc} e você está com sobrepeso. ') 
elif (imc>=30) and (imc<40):
  print(f'O IMC é {imc} e você está obeso. ')
else:
  print(f'O IMC é {imc} e você está com uobesidade mórbida. ')    