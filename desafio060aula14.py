'''numero = int(input('Digite um número inteiro: '))
for c in range(numero, 0, -1):
    print('{}'.format(c))'''

numero = int(input('Digite um número inteiro: '))
n = 1
while n <= numero:
    fatorial = numero * (numero - n)
    print ('{} = {} x {}'.format(fatorial, numero, (numero - 1)))
    numero = numero - 1
    