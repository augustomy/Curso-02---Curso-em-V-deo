sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo da pessoa: [M/F]\n')).strip().upper()[0] #[0] SIGNIFICA QUE O PROGRAMA IRÁ LER APENAS A PRIMEIRA LETRA DIGITADA
print('O sexo digitado foi: {}'.format(sexo))
