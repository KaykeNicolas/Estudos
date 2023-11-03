#O computador tem que pensar em um número e a gente tem que adivinhar
from random import randrange

import emoji

n = randrange(0, 5)
chute = int(input('Entre 0 e 5, tu acha que o pc tá pensando em que número? {} '.format(emoji.emojize(':thinking_face:'))))

if(chute == n):
    print('Ih ala, tu acertou {}'.format(emoji.emojize(':face_with_open_mouth:')))
else:
    print('Errou kkkkk, mó otário {}'.format(emoji.emojize(':rolling_on_the_floor_laughing:')))