height = float(input('Altura em metros (ex:1.6): '))
weight = int(input('Peso: '))
imc = float(weight / (height**2))
print('imc: ', imc)

if imc < 18.5:
    print('Magreza')
elif 18.5 > imc > 24.9:
    print('Normal')
elif 25.0 > imc > 29.9:
    print('Acima do peso')
elif 30.0 > imc > 39.9:
    print('Obesidade')
else:
    print('Obesidade grave')
