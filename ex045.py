import random
a = input('Pedra, papel ou tesoura? ')
aux = a.strip()
jogada = aux.upper()
maquina = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
print('Sua jogada: {}\nJogada da máquina: {}'.format(jogada, maquina))
if jogada == maquina:
    print('EMPATE!')
elif (jogada == 'PEDRA' and maquina == 'TESOURA') or (jogada == 'PAPEL' and maquina == 'PEDRA') or (jogada == 'TESOURA' and maquina == 'PAPEL'):
    print('\033[1;32mPARABÉNS! VOCÊ VENCEU\033[m!')
elif (maquina == 'PEDRA' and jogada == 'TESOURA') or (maquina == 'PAPEL' and jogada == 'PEDRA') or (maquina == 'TESOURA' and jogada == 'PAPEL'):
    print('\033[1;31mQUE PENA! VOCÊ PERDEU\033[m!')
else:
    print('Ocorreu um erro. Tente novamente.')
