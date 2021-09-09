# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584
print('Sequencia de Fibonacci')
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end= ' → ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('{}'.format(t3), end= ' → ')
    cont = cont + 1
    t1 = t2
    t2 = t3
print('FIM')
