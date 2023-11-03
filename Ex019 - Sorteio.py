#A ideia do código é sortear um cabinha pra apagar o quadro
import emoji
import random
a1 = input('Informe o nome de um aluno: ')
a2 = input('Diz o nome de outro abestalhado aí: ')
a3 = input('Mande oto: ')
a4 = input('Só mais um pra finalizar essa budega: ')

#Criei uma lista com os alunos digitados
lista = [a1, a2, a3, a4]

#Randomizei com o "choice"
print('Quem vai apagar o quadro é mesmo esse(a) tal de {} {}'.format(random.choice(lista), emoji.emojize(':nerd_face:')))