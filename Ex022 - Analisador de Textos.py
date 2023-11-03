#Pega o nome de um caba, mostra ele em:
#1- Minúsculas e Maiúsculas
#2- Quantas letra ao todo sem espaços
#3- Quantas letra no primeiro nome

#Ele lê o nome do usuário
nome = str(input('Me diz teu nome aí, namoral: ')).strip()

#1) Puxa o nome em minúsculo e maiúsculo
print('Seu nome com letras minúsculas é: {} \nCom maiúsculas é: {}'.format(nome.lower(), nome.upper()))

#2) Substitui os espaços por nada e conta quantas letras tem
nome_esp = nome.replace(' ','')
print(f'O número total de letras no seu nome é: {len(nome_esp)}')

#3) Depois divide o nome original e conta só o zero no vetor
nome_div = nome.split()
print(f'E só o seu primeiro nome tem {len(nome_div[0])} letras')