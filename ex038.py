a = int(input('Digite um número inteiro: \033[1;34m'))
b = int(input('\033[mDigite outro número inteiro: \033[1;35m'))
if a > b:
    print('\033[mO primeiro valor (\033[1;34m{}\033[m) é maior.'.format(a))
elif b > a:
    print('\033[mO segundo valor (\033[1;35m{}\033[m) é maior.'.format(b))

else:
    print('\033[mNão existe valor maior, os dois são iguais!')
