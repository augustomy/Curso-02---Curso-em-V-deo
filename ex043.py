peso = float(input('Digite o peso em kg: '))
altura = float(input('Digite a altura em metros: '))
imc = peso / (altura ** 2)
print('Seu IMC é: {} kg/m²'.format(imc))
if imc < 18.5:
    print('Sua classificação é: Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Sua classificação é: Peso ideal')
elif 25 <= imc < 30:
    print('Sua classificação é: Sobrepeso')
elif 30 <= imc < 40:
    print('Sua classificação é: Obesidade')
elif imc >= 40:
    print('Sua classificação é: Obesidade Mórbida')
else:
    print('Ocorreu um erro. Tente novamente.')
    