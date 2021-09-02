a = int(input('Digite um número inteiro: '))
print('A tabuada do {} é:'.format(a))
for m in range(0, 11, 1):
    print('{} x {} = {}'.format(m, a, m * a))
