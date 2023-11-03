'''Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

#Bibliotecas
from sty import fg
from datetime import date
from emoji import emojize

#Variáveis
nasc = int(input('Me diga aí, por favor, o ano que tu nasceu: '))
idade = (date.today().year) - nasc

#cores
verde = fg.green
vermelho = fg.red
limpa = fg.rs

#emojis
calma = ':hand_with_fingers_splayed:'
zangado = ':angry_face:'
neutro = ':neutral_face:'
aquele = ':face_with_raised_eyebrow:'

#Processamento e saída
if(idade > 0):
    if(idade < 18):
        print(f'Tenha calma, moreno {emojize(calma)}. Ainda faltam {verde}{18-idade}{limpa} anos pra você se alistar')
    elif(idade == 18):
        print(f'Ei parceiro {emojize(zangado)}, {verde}bora se alistar né?{limpa} Já tá na hora')
    elif(idade > 18 and idade < 26):
        print(f'Rapaz, já passou do tempo em? {vermelho}{idade-18}{limpa} anos pra ser mais específico {emojize(neutro)}')
    elif(idade > 26 and idade < 100):
        print(f'É meu consagrado, {vermelho}da mais não{limpa}, visse? {emojize(neutro)}')
    else:
        print(f'Como assim tu ainda é vivo, filho de Cristo? {emojize(aquele)}')
else:
    print(f'Tu {vermelho}ainda vai nascer{limpa}, parceiro? Como assim? {emojize(aquele)}')