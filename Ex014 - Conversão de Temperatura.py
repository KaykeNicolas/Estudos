#Converter diferentes temperaturas
temp = int(input('Informe a temperatura da sua cidade em Celcius: '))
print('Na sua cidade está {}°C, {}°F e {}°K'.format(temp, ((temp * 9/5) + 32), (temp + 273)))