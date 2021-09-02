pa = 0
primeirotermo = int(input('Digite o primeiro termo da Progressão Aritmética: '))
razao = int(input('Digite a razão da Progressão Aritmética: '))
termo10 = primeirotermo + (10-1) * razao
print('Segue a PA com os 10 primeiros termos, com primeiro termo {} e razão {}:'.format(primeirotermo, razao))
for c in range(primeirotermo, termo10 + 1, razao):
    print(c, end= ' ')
