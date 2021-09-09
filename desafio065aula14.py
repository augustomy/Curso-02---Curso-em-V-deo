resposta = ' '
s = 0
somatorio = 0
maior = 0
menor = 0
while resposta != 'N':
    n = int(input('Digite um número inteiro: '))
    somatorio = somatorio + n
    s = s + 1
    if s == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Deseja continuar digitando números inteiros? [S/N] ')).strip().upper()[0]
media = somatorio / s
print('Você digitou {} números.\nMédia dos valores digitados: {}'.format(s, media))
print('O maior valor foi {}'.format(maior))
print('O menor valor foi {}'.format(menor))
