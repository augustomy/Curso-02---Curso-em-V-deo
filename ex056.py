maior = 0
menor = 0
s = 0
for c in range(1, 4+1, 1):
    nome = str(input('Digite o nome ({}): '.format(c))).strip().upper()
    idade = int(input('Digite a idade ({}): '.format(c)))
    sexo = str(input('Digite o sexo ({}) - Homem(H) / Mulher(M): '.format(c))).strip().upper()
    if c == 1:
        nome1 = nome
        idade1 = idade
        sexo1 = sexo
        if sexo1 == 'H':
            maior = idade1
        else:
            menor = idade1
        if idade1 <= 20 and sexo == 'M':
            s = s + 1
    elif c == 2:
        nome2 = nome
        idade2 = idade
        sexo2 = sexo
        if idade2 > maior and sexo2 == 'H':
            maior = idade2
        if (idade2 < menor and sexo2 =='M') or (menor == 0 and sexo2 == 'M'):
            menor = idade2
        if idade1 <= 20 and sexo == 'M':
            s = s + 1
    elif c == 3:
        nome3 = nome
        idade3 = idade
        sexo3 = sexo
        if idade3 > maior and sexo3 == 'H':
            maior = idade3
        if idade3 < menor and sexo3 == 'M':
            menor = idade3
        if idade1 <= 20 and sexo == 'M':
            s = s + 1
    elif c == 4:
        nome4 = nome
        idade4 = idade
        sexo4 = sexo
        if idade4 > maior and sexo4 == 'H':
            maior = idade4
        if idade4 < menor and sexo4 == 'M':
            menor = idade4
        if idade1 <= 20 and sexo == 'M':
            s = s + 1

media = (idade1 + idade2 + idade3 + idade4) / 4

#CONDIÇÃO PARA VERIFICAR QUAL É O NOME DO HOMEM MAIS VELHO
if maior == idade1:
    nomemaior = nome1
elif maior == idade2:
    nomemaior = nome2
elif maior == idade3:
    nomemaior = nome3
elif maior == idade4:
    nomemaior = nome4

#CONDIÇÃO PARA VERIFICAR QUAL É O NOME DA MULHER MAIS NOVA
if menor == idade1:
    nomemenor = nome1
elif menor == idade2:
    nomemenor = nome2
elif menor == idade3:
    nomemenor = nome3
elif menor == idade4:
    nomemenor = nome4

print('\033[1;32mA média das idades informadas é: {}\033[m'.format(media))
print('\033[1;33mHomem mais velho: {}\033[m'.format(nomemaior))
print('\033[1;34mMulher mais nova: {}\033[m'.format(nomemenor))
print('\033[1;35mQuantidade de mulheres com menos de 20 anos: {}\033[m'.format(s))
