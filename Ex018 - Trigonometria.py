#A ideia do programa é ler um ângulo e dar seu seno, cosseno e tangente
#Vou tentar importar só o necessário dessa vez
import math
from emoji import emojize

#Vou ler um ângulo qualquer aqui
x = math.radians(float(input('Diz um ângulo aí vai: ')))

#E vou imprimir tudo que precisa logo
print('Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f} {}'.format(math.sin(x), math.cos(x), math.tan(x), emojize(':thumbs_up:')))