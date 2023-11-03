#A ideia do código é a pessoa digitar lá um nome e você tem que dizer qual é o primeiro e o útlimo nome

n = str(input('Diz aí teu nome: ')).strip()
nome = n.split()

print('O seu primeiro nome é {}'.format(nome[0]))
print(f'E o teu último é {nome[len(nome)-1]}')