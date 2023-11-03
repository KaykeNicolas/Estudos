'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
#Importando bibliotecas
import sty
import emoji

#Variáveis
#Uso essa primeira linha para adicionar cores ao
print(sty.fg(250))

valor = float(input('Informe o valor da casa R$'))
sal = float(input('Diga-nos seu salário R$'))
anos = int(input('Com quantos anos você quer pagar essa casa? '))
meses = anos*12
parcela = valor/meses

#Processamento e Saída
#Se as parcelas forem menores que 30% do salário ele pode pagar
if(parcela <= sal*0.30):
    print('{}A prestação será de R${:.2f} \n{}APROVADO{}, meus parabéns! {}'.format(sty.fg.rs, parcela, sty.fg(118), sty.fg.rs, emoji.emojize(':star-struck:')))
else:
    print('{}A prestação será de R${:.2f} \n{}NEGADO!{} {}'.format(sty.fg.rs, parcela, sty.fg.red, sty.fg(250), emoji.emojize(':grimacing_face:')))