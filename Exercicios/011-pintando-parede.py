# 011 - Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta 
#necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

l = float(input(f'Digite a largura da parede em metros: '))
a = float(input(f'Digite a altura da parece em metros: '))

area = l*a
q_tinta = area/2
print(f'A área de parede a ser pintada é igual a {area}m')
print(f'A quantiodade de tinta a ser usada para pintar {area} é igual a {q_tinta}')
