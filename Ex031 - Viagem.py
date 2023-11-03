d = float(input('Quantos KM tem essa viagem? '))
if(d <= 200):
    preco = d*0.5
else:
    preco = d*0.45
print(f'O preço da passagem foi R${preco}')