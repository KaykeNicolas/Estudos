n1 = int(input('Informe um número: '))
n2 = int(input('Agora tu diz outro: '))
n3 = int(input('O último vai: '))

if(n1>n2 and n1>n3):
    maior = n1
elif(n2>n3):
    maior = n2
else:
    maior = n3

if(n1<n2 and n1<n3):
    menor = n1
elif(n2<n3):
    menor = n2
else:
    menor = n3

print(f'O maior número desses aí é o {maior} e o menor é o {menor}')