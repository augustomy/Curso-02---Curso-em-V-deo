n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digie a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Sua média final é \033[1;31m{}\033[m.\n\033[1;31mREPROVADO\033[m.'.format(media))
elif 5.0 <= media <= 6.9:
    print('Sua média final é \033[1;33m{}\033[m.\n\033[1;33mRECUPERAÇÃO\033[m.'.format(media))
elif 7 <= media <= 10:
    print('Sua média final é \033[1;32m{}\033[m.\n\033[1;32mAPROVADO\033[m.'.format(media))
else:
    print('Ocorreu algum erro na digitação das notas.\nPor favor, tente novamente.')