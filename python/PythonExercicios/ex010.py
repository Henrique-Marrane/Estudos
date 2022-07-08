#Crie um programa que leia quantos dinheiro uma pessoa tem na carteira e mostre quanbtos dolares ela pode comprar
real = float(input('Quantos reais vc tem na sua carteira '))
cot = float(3.27)
dol = float(real / cot)
print('Vc tem', real, 'na sua carteira, com isso vc pode comprar {:.2f}'.format(dol), 'dolar')
