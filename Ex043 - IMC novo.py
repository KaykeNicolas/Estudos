'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
MC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida'''

#Bibliotecas
from sty import fg

#Variáveis
alt = float(input('Qual é a sua altura? '))
peso = float(input('Qual é o seu peso? '))
imc = peso/(alt**2)

#Processamento e Saída
print(f'Com o peso de {peso}Kg e a altura de {alt} metros, você tem o imc {imc:.2f}. ', end='')
if(18.5<=imc<25):
    print(f'Oh coisa boa, está no peso {fg.li_green}IDEAL!!{fg.rs}')
elif(25<=imc<30):
    print(f'Cuidado, você já está no {fg.li_magenta}SOBREPESO{fg.rs}')
elif(30<=imc<40):
    print(f'Mais cuidado ainda, você é {fg.magenta}OBESO{fg.rs}')
elif(imc>=40):
    print(f'TU VAI MORRER IMRÃO!! {fg.red}OBESIDADE MÓRBIDA{fg.rs}')
else:
    print('Oxente? Tem como tu ser tão magro assim não')