# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.
from random import randint
from time import sleep
com = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei?' ))
print('Processando...')
sleep(4)
if com == jogador:
    print('Parabens vc acertou, pois eu pensei no numero {}!!'.format(com))
else:
    print('Essa eu ganhei, eu pensei no numero {}!!'.format(com))
