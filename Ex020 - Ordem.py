#O professor quer uma ordem aleatória de gente pra apresentar um trabalho
import random
import emoji

#Primeiro lê quais os alunos
a1 = input('Diga o nome de um aluno: ')
a2 = input('Diz outro aí: ')
a3 = input('Manda bala: ')
a4 = input('O último vai: ')

#Põe essa galera numa lista e sorteia ela
lista = [a1, a2, a3, a4]
random.shuffle(lista)

print('A ordem para se lascar nos trabalhos é: {} {}'.format(lista, emoji.emojize(':face_with_tears_of_joy:')))