import random
computador = random.randint(0, 10)
jogador = 99
tentativas = 0
while jogador != computador:
    jogador = int(input('Digite seu palpite até acertar: '))
    if jogador != computador:
        tentativas = tentativas + 1
print('PARABÉNS! APÓS {} JOGADA(S), VOCÊ ACERTOU O NÚMERO {}'.format(tentativas, computador))