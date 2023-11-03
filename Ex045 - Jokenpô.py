'''Crie um programa que faça o computador jogar Jokenpô com você.'''

#Bibliotecas
from sty import fg
from random import randint
from time import sleep
from tqdm import tqdm

#emojis
pedra = '✊'
papel = '🖐'
tesoura =  '✌️'

#cores
cor_empate = fg(240)
cor_vitoria = fg(82)
cor_derrota = fg(196)

#Funções
#Comparar a vitória do jogador
def comparando ():
    #Pedra
    if (player == 1):
        if(maquina == 1):
            resultado = f'{cor_empate}EMPATE{fg.rs}'
        elif(maquina == 2):
            resultado = f'{cor_derrota}DERROTA{fg.rs}'
        else:
            resultado = f'{cor_vitoria}VITÓRIA{fg.rs}'

    #Papel
    elif(player == 2):
        if(maquina == 1):
            resultado = f'{cor_vitoria}VITÓRIA{fg.rs}'
        elif(maquina == 2):
            resultado = f'{cor_empate}EMPATE{fg.rs}'
        else:
            resultado = f'{cor_derrota}DERROTA{fg.rs}'

    #Tesoura
    elif(player == 3):
        if(maquina == 1):
            resultado = f'{cor_derrota}DERROTA{fg.rs}'
        elif(maquina == 2):
            resultado = f'{cor_vitoria}VITÓRIA{fg.rs}'
        else:
            resultado = f'{cor_empate}EMPATE{fg.rs}'
    
    #Nenhuma opção válida
    else:
        print(f'{fg.red}VALOR INVÁLIDO{fg.rs}')
    return resultado

#Pega o emoji da máquina
def emoji_maquina ():
    if(maquina == 1): #Pedra
        return pedra
    elif(maquina == 2): #Papel
        return papel
    else:
        return tesoura #Tesoura
    
#Pega o emoji do próprio player
def emoji_player ():
    if(player == 1): #Pedra
        return pedra
    elif(player == 2): #Papel
        return papel
    elif(player == 3): #Tesoura
        return tesoura  
    else:
        return None
    
#Aqui é só o cabeçalho para o programa ficar bonitinho
print(f'{fg(250)}-=-{fg.rs}' * 10)
print(f'{fg(225)}{"VAMOS JOGAR JOKENPÔ":^30}{fg.rs}')
print(f'{fg(250)}-=-{fg.rs}' * 10)

continuar = 's'
while(continuar == 's'):
    #Aqui eu apresento as opções
    print(f'{fg(250)}OPÇÕES:')
    print(f'[1] - Pedra {pedra}  \n[2] - Papel {papel} \n[3] - Tesoura {tesoura}')

    #Aqui eu pego o que o usuário vai utilizar e a máquina também
    player = int(input('O que você vai querer? '))
    maquina = randint(1, 3)

    #Processamento
    print(f'COMPARANDO')
    for i in tqdm(range(20)):
        #print(i)
        sleep(0.04)
    print(f'{fg(250)}-=-{fg.rs}' * 5)

    print(f'Máquina: {emoji_maquina()}')
    print(f'Você: {emoji_player()}')

    print(f'{fg(250)}-=-{fg.rs}' * 5)
    print(f'{comparando():^32}')
    print(f'{fg(250)}-=-{fg.rs}' * 5)

    continuar = str(input('Você deseja continuar? (s/n) ')).strip().lower()
