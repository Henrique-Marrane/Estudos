# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
al1 = str(input('Digite o primeiro aluno: '))
al2 = str(input('Digite o segundo aluno: '))
al3 = str(input('Digite o terceiro aluno: '))
al4 = str(input('Digite o quarto aluno: '))
list = [al1, al2, al3, al4]
escolhido = choice(list)
print('O aluno escolhido foi {}'.format(escolhido))
