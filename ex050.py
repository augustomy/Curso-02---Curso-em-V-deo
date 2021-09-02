s = 0
for c in range(0, 6, 1):
    a = int(input('Digite um número inteiro: '))
    if a % 2 == 0:
        s = s + a
print('A soma apenas dos números pares digitados vale: {}'.format(s))
