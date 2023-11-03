#A ideia do código é ver se a cidade começa ou não com Santos
import emoji

#Pego o nome da city e já meto nela o upper e tiro os espaços, pra depois dividir
cidade = str(input('Nome da sua cidade: ')).strip()
nome = cidade.split()

#Depois verifico se o vetor 0 dela pós split é santos
if(nome[0].upper() == 'SANTOS' or 'SANTO'):
    print('Sua cidade começa com o nome Santo(s) {}'.format(emoji.emojize(':thumbs_up:')))
else:
    print('Sua cidade não começa com Santo(s) {}'.format(emoji.emojize(':thumbs_down:')))