x = int(input('Digite um número \033[1;34minteiro\033[m: '))
n = int(input('Digite:\n\033[1;31m1 para binário.\033[m\n\033[1;32m2 para octal.\033[m\n\033[1;33m3 para hexadecimal.\033[m\n'))
if n == 1:
    binario = bin(x)
    print('O número inteiro {} em \033[1;31mbinário vale\033[m: \n\033[1;31m{}\033[m'.format(x, binario))
elif n == 2:
    octal = oct(x)
    print('O número inteiro {} em \033[1;32moctal\033[m vale: \n\033[1;32m{}\033[m'.format(x, octal))
elif n == 3:
    hexadecimal = hex(x)
    print('O número inteiro {} em \033[1;33mhexadecimal\033[m vale: \n\033[1;33m{}\033[m'.format(x, hexadecimal))
else:
    print('A opção digitada não é válida.\nPor favor tente novamente.')
