# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um numero: '))
resul = num % 2
if resul == 0:
    print('Esse numero {} e PAR'.format(num))
else:
    print('Esse numero {} e IMPAR'.format(num))
