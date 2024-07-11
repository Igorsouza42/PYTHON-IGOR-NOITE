#faça um sistema de conversão de °celsius - °Kelvin
#Temperatura-kelvin = Temperatura-celsius + 273,15
print('Conversor de temperatura')
celsius = 1
kelvin = 2
fahrenheit = 3
fahrenheit = 4
Opçao = int(input("informe a opção 1 para converter para celsius;  opção 2 para kelvin; opção 3 para fahrenheit; opção 4 para fahrenheit: "))
print (f'Você escolheu a opção {Opçao}°.')
temperatura = float(input("Digite a temperatura: ")) 

#condição
if Opçao == 1 :
    temperatura = kelvin - 273.15
    print (f'{temperatura} ° Celsius')
elif Opçao == 2 :
    temperatura = Celsius + 273.15
    print (f'{temperatura} ° kelvin')

elif Opçao== 3:
    temperatura = fahrenheit - 273.15
    print (f'{temperatura} ° Celsius')

elif Opçao == 4:
    temperatura = fahrenheit + 273.15
    print(f'{temperatura} ° kelvin')
else:
    print ('Opção Inválida!')

