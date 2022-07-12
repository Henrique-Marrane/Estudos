# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('Qual a velocidade do carro? '))
m = (vel - 80) * 7
if vel <= 80:
    print('Vc esta dentro dos limites permitidos. Boa viagem!!')
else:
    print('VC ultrapassou os limite permitidos e tera que pagar uma multa de R${}'.format(m))
print('Dirija com cuidado!!')