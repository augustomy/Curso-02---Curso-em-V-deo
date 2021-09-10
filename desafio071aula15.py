
while True:
    nota50 = nota20 = nota10 = nota1 = 0
    sobra1 = sobra2 = 0
    valor = int(input('Digite o valor a ser sacado: R$'))
    if valor >= 50:
        nota50 = valor // 50
        sobra1 = valor % 50
        if sobra1 >= 20:
            nota20 = sobra1 // 20
            sobra2 = sobra1 % 20
            if sobra2 >= 10:
                nota10 = sobra2 // 10
                nota1 = sobra2 % 10

        if sobra1 < 20:
            nota10 = sobra1 // 10
            nota1 = sobra1 % 10

    elif 20 <= valor < 50:
        nota50 = 0
        nota20 = valor // 20
        sobra1 = valor % 20
        if sobra1 >= 10:
            nota10 = sobra1 // 10
            nota1 = sobra1 % 10
        if sobra1 < 10:
            nota1 = sobra1

    elif 10 <= valor < 20:
        nota50 = nota20 = 0
        nota10 = valor // 10
        nota1 = valor % 10
    
    elif 1 <= valor < 10:
        nota50 = nota20 = nota10 = 0
        nota1 = valor
    print(f'Notas de R$50: {nota50}\nNotas de R$20: {nota20}\nNotas de R$10: {nota10}\nNotas de R$1: {nota1}')
    resp = str(input('Deseja realizar outro saque? [S/N] ')).strip().upper()[0]
    '''while resp != 'S' or resp != 'N':
        print('Opção inválida.')
        resp = str('Deseja realizar outro saque? [S/N] ').strip().upper()[0]'''
    if resp == 'N':
        break
print('FIM')
