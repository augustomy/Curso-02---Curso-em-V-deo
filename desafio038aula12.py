n1 = int(input('Digite o primeiro número \033[1;32minteiro\033[m: '))
n2 = int(input('Digite o segundo número \033[1;33minteiro\033[m: '))
if n1  > n2:
    print('O primeiro número (\033[1;32m{}\033[m) é maior.'.format(n1))
elif n2 > n1:
    print('O segundo número (\033[1;33m{}\033[m) é maior.'.format(n2))
else:
    print('Não existe valor maior, os dois são iguais')
