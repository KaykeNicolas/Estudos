#A ideia é ver a média de um aluno a partir de duas notas
nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Me informe sua segunda nota: '))

print('A sua nota média, usando {:.1f} e {:.1f} como base, foi: {:.1f}'.format(nota1, nota2, ((nota1 + nota2)/ 2)))