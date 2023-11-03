'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER'''

#Bibliotecas
from datetime import date
from sty import fg

#Variáveis
nasc = int(input('Por favor, informe seu ano de nascimento: '))
idade = (date.today().year) - nasc

#Processamento e Saída
print(f'Sua idade: {idade}')
if(idade <= 9):
    print(f'Categoria:{fg.da_blue} MIRIM {fg.rs}')
elif(idade <= 14):
    print(f'Categoria:{fg.cyan} INFANTIL {fg.rs}')
elif(idade <= 19):
    print(f'Categoria: {fg.da_green} JÚNIOR {fg.rs}')
elif(idade <= 25):
    print(f'Categoria:{fg.da_magenta} SÊNIOR {fg.rs}')
else:
    print(f'Categoria {fg.da_yellow} MASTER {fg.rs}')