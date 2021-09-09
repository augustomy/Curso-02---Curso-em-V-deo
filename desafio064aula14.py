n = 0
s = 0
q = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        s = s + n
        q = q + 1
print('Quantidade de números digitados: {}\nSoma dos números digitados: {}'.format(q, s))
