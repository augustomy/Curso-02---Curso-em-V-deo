'''numero = int(input('Digite um número inteiro: '))
for c in range(numero, 0, -1):
    if c != 1:
        fatorial = c * numero
        numero = numero - 1
    print('{} | {}'.format(numero, fatorial))'''

numero = int(input('Digite um número inteiro: '))
while numero != 0:
    fatorial = numero * (numero - (numero - 1))
    numero = numero - 1
    print ('{} = {} x {}'.format(fatorial, numero, (numero - (numero - 1))))