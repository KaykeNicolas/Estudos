#Escreva um programa que pergunte a quantidade de Km e dias percorridos por um carro alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Informe por quantos dias você o usou o carro: '))
km = float(input('Diga quantos Km foram percorridos com o carro: '))

print('O preço a pagar é R${:.2f}'.format((dias * 60) + (km * 0.15)))