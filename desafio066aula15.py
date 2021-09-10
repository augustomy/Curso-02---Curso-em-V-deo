q = s = 0
while True:
    numero = int(input('Digite um número inteiro (999 para parar): '))
    if numero == 999:
        break
    q = q + 1
    s = s + numero
print(f'Você digitou {q} números e a soma deles é {s}')
