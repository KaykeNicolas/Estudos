#A ideia do código é ler dois catetos e calcular uma hipotenusa
#Primeiro eu importo os módulos, que é o intuito desse exercício
import math
import emoji

#Depois eu leio os catetos que são necessários
cat1 = float(input('Diz o valor do cateto oposto a uma hipotenusa aí: '))
cat2 = float(input('Diz outro, só adjacente: '))

#Primeiro calculo a potencia dos dois lá, depois passo o quadrado como raíz
calculo = (math.pow(cat1, 2)) + (math.pow(cat2, (2)))
hipo = math.sqrt(calculo)

print('A hipotenúsa desse triângulo vale {:.2f} {}'.format(hipo, emoji.emojize(':red_triangle_pointed_up:')))

print(math.hypot(cat1, cat2))
