#A ideia é pegar um número até 9999 e mostrar quais os dígitos separadamente

#primeiro eu leio o número da pessoa
n = int(input('Vou ler um número até no máximo seu quarto dígito \nManda bala, digite um número até 9999: '))

#Divido pelas unidades respectivas
uni = n //1 % 10
dez = n //10 % 10
cen = n //100 % 10
mil = n //1000 % 10

#E imprimo
print(f'Unidade: {uni} \nDezena: {dez} \nCentena: {cen} \nMilhar: {mil}')