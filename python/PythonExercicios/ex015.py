# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos KM foi rodado? '))
d = float(input('Quantos dias ficou como o carro? '))
kmr = km * 0.15
ad = d * 60
print('O carro rodou por {:.0f}Km, por {:.0f} dias, o valor total a pagar é de R${:.2f}'.format(km, d, (kmr + ad)))
