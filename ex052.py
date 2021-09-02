s = 0
n = int(input('Digite um número inteiro: '))
for c in range(1, n+1, 1):
    if n % c == 0:
        s = s + 1
if s == 2:
    print('\033[1;32mO número {} é primo!\033[m'.format(n))
else:
    print('\033[1;31mO número {} não é primo\033[m!'.format(n))
