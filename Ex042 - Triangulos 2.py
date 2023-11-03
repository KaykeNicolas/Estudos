'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, 
acrescentando o recurso de mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes'''

#Bibliotecas
from sty import fg

#Variáveis
r1 = float(input('Diz aí um seguimento de reta: '))
r2 = float(input('Manda outro: '))
r3 = float(input('O último, só pra finalizar: '))

#Processamento e Saída
if((r1+r2 > r3) and (r2+r3 > r1) and (r1+r3 > r2)):
    print(f'É{fg.li_green} POSSÍVEL {fg.rs}formar um triângulo com essas retas')
    if(r1 == r2 == r3):
        print(f'Inclusive, esse triângulo é {fg.li_green}EQUILÁTERO{fg.rs}')
    elif((r1 != r2) and (r1 != r3) and (r2 != r3)):
        print(f'Falando nisso, esse triângulo seria {fg.li_red}ESCALENO{fg.rs}')
    else:
        print(f'Até {fg.li_blue}ISÓCELES{fg.rs} esse triângulo seria')
else:
    print(f'Pow, é{fg.li_red} IMPORSSÍVEL {fg.rs}formar um triângulo com essas 3 retas')

