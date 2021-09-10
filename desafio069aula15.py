maior18 = 0
homens = 0
mulheres = 0
while True:
    idade = int(input('Digite a idade: '))
    while idade == ' ' or idade < 0:
        print('Idade inválida. Digite novamente.')
        idade = int(input('Digite a idade: '))
    if idade >= 18:
        maior18 = maior18 + 1

    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        print('Sexo inválido. Digite novamente.')
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens = homens + 1
    if idade < 20 and sexo == 'F':
        mulheres = mulheres + 1

    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print('Opção inválida. Digite novamente.')
    if resp == 'N':
        break
    
print(f'Pessoas maiores de 18 anos: {maior18}\nQuantidade de homens: {homens}\nQuantidade de mulheres com menos de 20 anos: {mulheres}')
