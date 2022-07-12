n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunta nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
m = (n1 + n2 + n3 + n4) / 4
if m < 6.0:
    print('Aluno reprovado, pois sua media foi {}!'.format(m))
else:
    print('Aluno aprovado, pois sua media foi {}!!'.format(m))
print('---FIM---')
