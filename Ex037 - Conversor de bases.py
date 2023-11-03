'''Escreva um programa em Python que leia um número inteiro qualquer 
e peça para o usuário escolher qual será a base de conversão: 
1 para binário, 2 para octal e 3 para hexadecimal.'''

#Bibliotecas
import sty

#Variáveis
num = int(input('Informe um número inteiro qualquer: '))
print('Essas são as bases disponíveis')
print('[ 1 ] - {}BINÁRIO{}'.format(sty.fg(51), sty.fg.rs))
print('[ 2 ] - {}OCTAL{}'.format(sty.fg(202), sty.fg.rs))
print('[ 3 ] - {}HEXADECIMAL{}'.format(sty.fg(198), sty.fg.rs))
base = int(input('Informe a base que você quer: '))

#Processamento e Saída
if(base == 1):
    print(f'O resultado de {num} em binário é {sty.fg(51)}{bin(num) [2:]}{sty.fg.rs}')
elif(base == 2):
    print(f'O resultado de {num} em octal é {sty.fg(202)}{oct(num) [2:]}{sty.fg.rs}')
elif(base == 3):
    print(f'O resultado de {num} em octal é {sty.fg(198)}{hex(num) [2:]}{sty.fg.rs}')
else:
    print('É parceiro, operação {}INVÁLIDA{}'.format(sty.fg(196),sty.fg.rs))