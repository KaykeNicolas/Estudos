#A ideia do código é pegar um valor em reais e transformar ele em doláres
reais = float(input('Digite quantos reais você tem: R$'))

print('Da para comprar {:.2f} dólares com R${}'.format(reais / 4.93, reais))
print('Em 2017, era possível comprar {:.2f} dólares com os mesmos R${}'.format(reais / 3.27, reais))