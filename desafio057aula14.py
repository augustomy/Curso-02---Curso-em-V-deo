sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo da pessoa: [M/F]\n')).strip().upper()
print('O sexo digitado foi: {}'.format(sexo))