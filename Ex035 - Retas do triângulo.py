a = int(input('Diz o valor da primeira reta: '))
b = int(input('Agora da segunda: '))
c = int(input('Da última vai: '))

if((a+b > c) and (a+c > b) and (b+c >a)):
    print(f'As retas {a},{b} e {c} são capazes de formar um triângulo SIM')
else:
    print('Vai dar NÃO')