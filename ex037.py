num = int(input('Digite um número inteiro: '))
escolha = int(input("""Escolha a conversão:
\033[1;32m1 - Binário\033[m;
\033[1;33m2 - Octal\033[m;
\033[1;34m3 - Hexadecimal\033[m.\n"""))

if escolha == 1:
    binario = bin(num)
    print('Escolha: \033[1;32m1 - Binário\033[m\nO número {} em Binário é \033[1;32m{}\033[m'.format(num, binario[2:]))

elif escolha == 2:
    octa = oct(num)
    print('Escolha: \033[1;33m2 - Octal\033[m\nO número {} em Octal é \033[1;33m{}\033[m'.format(num, octa[2:]))

elif escolha == 3:
    hexadecimal = hex(num)
    print('Escolha: \033[1;34m3 - Hexadecimal\033[m\nO número {} em Hexadecimal é \033[1;34m{}\033[m'.format(num, hexadecimal[2:]))

else:
    print('\033[1;31mOcorreu um erro.\nTente novamente.\033[m')
