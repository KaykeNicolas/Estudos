'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO'''

#Bibliotecas
from sty import fg

#Variáveis
n1 = float(input('Qual foi a tua primeira nota? '))
n2 = float(input('E a segunda? '))
media = (n1+n2)/2

#Processamento e saída
if(media < 5):
    print(f'É fellas, sua nota foi {media}, tu tá {fg.red}REPROVADO!{fg.rs}')
elif(7 > media >= 5):
    print(f'Beleza, tua média foi {media}, tu tá em {fg.blue}RECUPERAÇÃO!{fg.rs}')
else:
    print(f'Parabéns! Sua média foi {media}. Você foi {fg.green}APROVADO!{fg.rs}')