a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = int(input('''Digite a opção desejada:
    \033[1;32m[1] SOMAR\033[m;
    \033[1;33m[2] MULTIPLICAR\033[m;
    \033[1;34m[3] MOSTRAR MAIOR NÚMERO\033[m;
    \033[1;35m[4] DIGITAR NÚMEROS NOVAMENTE\033[m;
    \033[1;36m[5] SAIR DO PROGRAMA\033[m.
'''))
while c == 4:
    a = float(input('Digite o primeiro valor: '))
    b = float(input('Digite o segundo valor: '))
    c = int(input('''Digite a opção desejada:
    \033[1;32m[1] SOMAR\033[m;
    \033[1;33m[2] MULTIPLICAR\033[m;
    \033[1;34m[3] MOSTRAR MAIOR NÚMERO\033[m;
    \033[1;35m[4] DIGITAR NÚMEROS NOVAMENTE\033[m;
    \033[1;36m[5] SAIR DO PROGRAMA\033[m.
    '''))

if c == 1:
    print('{} + {} = {}'.format(a, b, a + b))
elif c == 2:
    print('{} x {} = {}'.format(a, b, a * b))
elif c == 3:
    if a > b:
        print('{} é maior'.format(a))
    if b > a:
        print('{} é maior'.format(b))
    else:
        print('Os números são iguais!')
elif c == 5:
    print('\033[1;31mFIM DO PROGRAMA\033[m')
else:
    print('Opção inválida. Tente novamente.')
