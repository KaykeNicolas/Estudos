import emoji
from math import trunc
n = float(input('Digite um número todo quebrado aí: '))
print('Isso tá muito esculhambado, é melhor: {} {}'.format(trunc(n), emoji.emojize(':OK_hand:')))