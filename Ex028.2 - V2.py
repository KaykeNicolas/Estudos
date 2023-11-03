#O computador tem que pensar em um número e a gente tem que adivinhar (usando While)
from random import randrange
import time
import emoji

n = randrange(0, 5)
chute = 0
print("-=-" * 20)
print('Eu vou pensar num número aqui entre 0 e 5, visse?')
print("-=-" * 20)

while(chute != n):
    chute = int(input('Tu acha que eu tô pensando em que número? {} '.format(emoji.emojize(':thinking_face:'))))
    print('ARGUARDE...')
    time.sleep(1)

    if(chute == n):
        print('Ih ala, tu acertou {}'.format(emoji.emojize(':face_with_open_mouth:')))
    else:
        print('Errou kkkkk, mó otário {}'.format(emoji.emojize(':rolling_on_the_floor_laughing:')))