#Ler a velocidade de um carro. Se for maior q 80 por hora ele tem multa de 7 pila por km
vel = float(input('Ei bix, diz aí a velocidade que tu tava na moral: '))

if(vel > 80):
    print(f'Tu foi multado em R${(vel - 80) * 7}')
else:
    print('Fosse multado não, pode ficar de boa')