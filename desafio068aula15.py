import random
s = 0
while True:
    computador = random.randint(0, 10)
    escolha = str(input('Par (P) ou Ímpar (I)? ')).strip().upper()[0]
    while escolha != 'P' and escolha != 'I':
        escolha = str(input('Par (P) ou Ímpar (I)? ')).strip().upper()[0]
    if escolha == 'P':
        jogada = 'PAR'
        maquina = 'IMPAR'
        print(f'Sua escolha foi {jogada}')
    elif escolha == 'I':
        jogada = 'IMPAR'
        maquina = 'PAR'
        print(f'Sua escolha foi {jogada}')
    else:
        print('Escolha inválida. Tente novamente')
    numero = int(input('Digite seu número de escolha: '))
    print(f'Sua escolha foi {numero}')
    if (computador + numero) % 2 == 0 and jogada == 'PAR':
        print(f'{computador} + {numero} = {computador + numero} é PAR!\nPARABÉNS! Você ganhou!')
        s = s + 1
    if (computador + numero) % 2 != 0 and jogada == 'IMPAR':
        print(f'{computador} + {numero} = {computador + numero} é ÍMPAR!\nPARABÉNS! Você ganhou!')
        s = s + 1
    else:
        print(f'{computador} + {numero} = {computador + numero}\nQUE PENA! Você perdeu!\nVocê teve {s} vitórias consecutivas.')
        break
