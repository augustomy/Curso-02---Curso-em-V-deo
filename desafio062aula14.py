n = 0
primeirotermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
total = 0
resp = 10
while resp != 0:
    total = total + resp
    while n < total:
        termos = primeirotermo + n * razao
        n = n + 1
        print(termos, end= ' → ')
    print('PAUSA')
    resp = int(input('\nGostaria de mostrar quantos termos a partir do décimo? '))
print('FIM')
