n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('\033[1;34mPrimeira nota: {:.1f}\033[m\n\033[1;35mSegunda nota: \033[1;35m{:.1f}\033[m'.format(n1, n2))

if 0 <= media < 5 and n1 >= 0 and n2 >= 0:
    print('Média final: {:.1f}\n\033[1;31mREPROVADO\033[m'.format(media))
elif 5 <= media <= 6.9 and n1 >= 0 and n2 >= 0:
    print('Média final: {:.1f}\n\033[1;33mRECUPERAÇÃO\033[m'.format(media))
elif 7 <= media <= 10 and n1 >= 0 and n2 >= 0:
    print('Média final: {:.1f}\n\033[1;32mAPROVADO\033[m'.format(media))
else:
    print('Ocorreu um erro. Tente novamente.')
