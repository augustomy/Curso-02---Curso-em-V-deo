peso = float(input('Digite o peso em \033[1;35mkg\033[m: '))
altura = float(input('Digite a altura em \033[1;36mmetros\033[m: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é \033[1;33m{:.1f}\033[m.\n\033[1;33mAbaixo do peso\033[m.'.format(imc))
elif 18.5<= imc < 25:
    print('Seu IMC é \033[1;32m{:.1f}\033[m.\n\033[1;32mPeso ideal\033[m.'.format(imc))
elif 25<= imc < 30:
    print('Seu IMC é \033[1;33m{:.1f}\033[m.\n\033[1;33mSobrepeso\033[m.'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é \033[1;31m{:.1f}\033[m.\n\033[1;31mObesidade\033[m.'.format(imc))
elif imc >= 40:
    print('Seu IMC é \033[1;31m{:.1f}\033[m.\n\033[1;31mObesidade mórbida\033[m.'.format(imc))
else:
    print('Houve alguma inconsistência nos dados informados.\nPor favor tente novamente.')
    