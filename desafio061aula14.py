n = 0
primeirotermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
while n < 10:
    termos = primeirotermo + n * razao
    n = n + 1
    print(termos, end= ' → ')
print('FIM')

