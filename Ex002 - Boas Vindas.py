#O objetivo do código é o usuário digitar seu nome e eu imprimir

#Aqui eu crio um dicionário e dou o nome das cores e o código
cores = {
    'limpa' : '\033[m',
    'cor31' : '\033[31m'
}

#Depois eu pergunto ao usuário o nome dele
nome = input('Digite seu {}nome{} '.format(cores['cor31'], cores['limpa']))

#E no final imprimo
print('Seja bem vindo! {}{}!{}'.format(cores['cor31'], nome, cores['limpa']))