n = int(input('Digita um ano aí: '))
if(((n % 4 == 0) and (n % 100 != 0)) or (n % 400 == 0)):
    print('O ano é bissexto SIM')
else:
    print('O ano não é bissexto NÃO em')