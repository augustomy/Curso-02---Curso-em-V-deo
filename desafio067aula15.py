c = 0
while True:
    numero = int(input('Digite um número inteiro (negativo para parar): '))
    if numero < 0:
        break
    for c in range(0, 11, 1):
        tabuada = c * numero
        print(f'{numero} x {c} = {tabuada}')
print('FIM')
