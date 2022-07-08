# Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salário, com 15% de aumento.
sal = int(input('Digite aqui o salario '))
val = sal + int((sal * 15) / 100)
print('O valor do salario com aumento é {}'.format(val))
