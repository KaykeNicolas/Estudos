'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais'''

#Bibliotecas
from sty import fg

#Variáveis
n1 = int(input('Informe um valor: '))
n2 = int(input('Digite outro número: '))

#Processamento e saída
if(n1 > n2):
    print(f'O {fg(80)} PRIMEIRO {fg.rs} valor é o maior')
elif(n2 > n1):
    print(f'O {fg(80)} SEGUNDO {fg.rs} valor é o maior')
else:
    print(f'Oxente, os números são {fg(80)}IGUAIS{fg.rs}')