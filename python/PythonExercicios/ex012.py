# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
pre1 = float(input('Digite aqui o valor do produto'))
pre2 = pre1 - float((pre1 * 5) / 100)
print('O valor do produto com desconto fica {}'.format(pre2))
