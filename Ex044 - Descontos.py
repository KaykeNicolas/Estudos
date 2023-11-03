'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal 
3x ou mais no cartão: 20% de juros'''

#Bibliotecas
from sty import fg

#Variáveis
print('-=-'*10)
print('{}{:^5}LOJAS COMPROU PAGOU {}'.format(fg(213), '',fg.rs))
print('-=-'*10)
preco = float(input('Digite o preço do produto que deseja comprar R$'))
print('Como você quer pagar esse produto?')
vp = int(input('[1] - À vista  \n[2] - À prazo: '))

#Processamento e Saída
if(vp == 1):
    forma = int(input(f'{fg.da_blue}[1] - Dinheiro  \n[2] - Cheque  \n[3] - Cartão: {fg.li_green}'))
    if(forma == 1 or forma == 2):
        print(f'O preço a pagar que era de R${preco}, se tornou R${preco*0.9:.2f}')
    elif(forma == 3):
        print(f'O preço que era de R${preco}, virou R${preco*0.95}')
    else:
        print('Mano, essa forma de pagar aí não existe não em')

elif(vp == 2):
    parcelas = int(input(f'{fg.da_blue}Em quantas parcelas você gostaria de pagar? {fg.li_green}'))
    if(parcelas == 1):
        print(f'Então é à vista parceiro. De R${preco}, ficou R${preco*0.95:.2f}')
    elif(parcelas == 2):
        print(f'Você naõ ganhou desconto, o preço continua R${preco}')
    elif(parcelas > 2):
        print(f'O preço que era R${preco} vai receber 20% de juros, ficando R${preco*1.20:.2f}. Serão parcelas de R${(preco*1.20)/parcelas:.2f}')

else:
    print(f'{fg.red}Tu nem escolheu direito se queria à vista ou à prazo!')