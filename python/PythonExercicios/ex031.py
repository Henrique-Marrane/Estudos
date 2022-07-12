# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input('Me diga quantos KM e sua viagem: '))
dist1 = distancia * 0.50
dist2 = distancia * 0.45
if distancia > 200:
    print('Para a distancia de {}KM o valor da passagem e de R${}'.format(distancia, dist2))
else:
    print('Para a distancia de {}KM  o valor da passagem e de R${}'.format(distancia, dist1))
