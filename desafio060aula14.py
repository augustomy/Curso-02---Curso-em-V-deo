# OUTRA MANEIRA DE FAZER
numero = int(input('Digite um número inteiro: '))
c = 0
f = 1
for c in range(1, numero):
    f = f * numero
    numero = numero - 1
print('{}'.format(f), end= ' ')

# OUTRA MANEIRA DE FAZER
'''numero = int(input('Digite um número inteiro: '))
c = numero
f = 1
print('Calculando {}! = '.format(numero), end = ' ')
while c > 0:
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    f = f * c
    c = c - 1
print('{}'.format(f))'''

# OUTRA MANEIRA DE FAZER   
'''from math import factorial
numero = int(input('Digite um número inteiro: '))
f = factorial(numero)
print('O fatorial de {} é: {}'.format(numero, f))'''
