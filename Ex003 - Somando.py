#A ideia do código é somar dois valores dados pelo usuário

#Importo as cores
cores = {
    'limpa' : '\033[m',
    'cor' : '\033[32m'
}

#Pergunto os números
n1 = float(input('{}Digite um valor:{} '.format(cores['cor'], cores['limpa'])))
n2 = float(input('{}Digite outro número:{} '.format(cores['cor'], cores['limpa'])))

#Depois imprimo
print('A soma entre {}{}{} e {}{}{} é {}{}{}!!'.format(cores['cor'], n1, cores['limpa'], cores['cor'], n2, cores['limpa'], cores['cor'], n1+n2, cores['limpa']))