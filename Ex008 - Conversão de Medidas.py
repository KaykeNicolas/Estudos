#A ideia aqui é criar um programa que leia um valor em metros e mostre os cm e ml
n = float(input('Informe um número em metros: '))

print('Km: {:.3f} \nHm: {} \nDam: {} \nm: {} \nDm: {} \nCm: {} \nMm: {}'.format(n / 1000, n / 100, n / 10, n, n*10, n*100, n*1000))
#print('{} metro(s), se torna {:.2f} em centímetros e {:.2f} em milímetros'.format(n, (n * 100), (n * 1000)))