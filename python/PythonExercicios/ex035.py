# Desenvolva um programa que leia o comprimento de três retas e diga
# ao usuário se elas podem ou não formar um triângulo.
print('\033[0;33;40m-=-\033[m' * 20)
print('Analisador de Triangulo')
print('\033[0;33;40m-=-\033[m' * 20)
r1 = int(input('Primeiro seguimento: '))
r2 = int(input('Segundo sequimento: '))
r3 = int(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima pode forma um triangulo.')
else:
    print('Os seguimentos acima nao pode forma um triangulo.')
