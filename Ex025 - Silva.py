#A ideia é ler o nome de alguém e ver se ela tem silva no nome

#Primeiro eu leio o nome da pessoa
nome = str(input('Diz aí o teu nome: ')).strip().upper()

#Verifico se tem Silva
if('SILVA' in nome):
    print('Seu nome tem Silva aí no meio')
else:
    print('Seu nome não tem Silva :(')