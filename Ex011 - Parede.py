#A ideia do código é: Preciso ler a altura e largura de uma parede
#Em seguida descobrir quanto de tinta preciso para pintá-la
#Cada litro pinta dois m²
h = float(input('Digite a altura da parede da sua casa, em metros: '))
b = float(input('Informe a largura da sua parede, em metros: '))
print('Você vai precisar de {:.0f} baldes de tinta de 1 litro para pintar sua parede'.format((b*h)/2))