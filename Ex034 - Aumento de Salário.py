sal = float(input('Diz aí quanto tu ganha que eu digo teu aumento: '))

if(sal > 1250):
    sal *= 1.10
else:
    sal *= 1.15

print(f'O teu salário novo é {sal}')