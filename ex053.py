frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #ELIMINA OS ESPAÇOS DA ESQUERDA (INÍCIO) E DA DIREITA (FINAL). NÃO ELIMINA OS ESPAÇOS ENTRE AS PALAVRAS.
junto = ''.join(palavras) #JUNTA AS PALAVRAS DA FRASE DIGITADA (ELIMINA OS ESPAÇOS ENTRE AS PALAVRAS)
inverso = '' #DECLARA A VARIÁVEL inverso COMO STRING E VAZIA NESSE PRIMEIRO MOMENTO
for letra in range(len(junto) - 1, -1, -1): #VARRE A PALAVRA/FRASE NO SENTIDO OPOSTO (DA ÚLTIMA LETRA ATÉ A PRIMEIRA)
        inverso += junto[letra] #INCREMENTA A VARIÁVEL inverso
print('A frase {} escrita ao contrário é: {}'.format(frase, inverso), end='')
if junto == inverso:
    print('\n\033[1;32mA frase é um PALÍNDROMO!\033[m')
else:
    print('\n\033[1;31mA frase NÃO é um PALÍNDROMO!\033[m')
