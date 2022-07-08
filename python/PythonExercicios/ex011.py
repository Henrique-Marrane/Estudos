# Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua area e a quantidade
# de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m².
autura = float(input('Qual a altura da parede '))
largura = float(input('Qual a largura da parede '))
tinta = autura * largura / 2
print('Para pinta essa parede sera nescessario {}'.format(tinta), 'litros de tinta.')
