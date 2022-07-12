# Crie um programa que leia o nome completo de uma pessoa e mostre:
#
# – O nome com todas as letras maiúsculas e minúsculas.
#
# – Quantas letras ao todo sem considerar espaços.
#
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculo e {}'.format(nome.upper()))
print('Seu nome em minusculo e {}'.format(nome.lower()))
print('Seu nome tem ao toto {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
