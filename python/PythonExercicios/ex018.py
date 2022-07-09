# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, radians, tan
ag = float(input('Digite o angulo que vc deseja: '))
seno = sin(radians(ag))
cosseno = cos(radians(ag))
tang = tan(radians(ag))
print('O angulo de {} tem o Seno de {:.2f}'.format(ag, seno))
print('O andulo de {} tem o Cosseno de {:.2f}'.format(ag, cosseno))
print('O angulo de {} tem a tangente de {:.2f}'.format(ag, tang))
