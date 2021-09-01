import random
print('\033[7;32;43m*==*\033[m' * 20)
print('\033[1;35m                                   JOKENPÔ\033[m')
print('\033[7;33;42m*==*\033[m' * 20)
escolha = input('Digite sua escolha (Pedra✊, Papel✋, Tesoura✌️): ')
escolhasemespacos = escolha.strip()
escolhac = escolhasemespacos.upper()
maquina = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
if (escolhac == 'PEDRA' and maquina == 'PEDRA') or (escolhac == 'PAPEL' and maquina == 'PAPEL') or (escolhac == 'TESOURA' and maquina == 'TESOURA'):
    print('EMPATE!')

elif (escolhac == 'PEDRA' and maquina == 'TESOURA') or (escolhac == 'TESOURA' and maquina == 'PAPEL') or (escolhac == 'PAPEL' and maquina == 'PEDRA'):
    print('\033[1;32mPARABÉNS! VOCÊ GANHOU!\033[m')

elif (escolhac == 'PEDRA' and maquina == 'PAPEL') or (escolhac == 'TESOURA' and maquina == 'PEDRA') or (escolhac == 'PAPEL' and maquina == 'TESOURA'):
    print('\033[1;31mQUE PENA VOCÊ PERDEU!\033[m')

else:
    print('Ocorreu um erro.\nTente novamente.')

if escolhac == 'PEDRA':
    print('Você: {}✊'.format(escolhac))

elif escolhac == 'PAPEL':
    print('Você: {}✋'.format(escolhac))

elif escolhac == 'TESOURA':
    print('Você: {}✌️'.format(escolhac))

if maquina == 'PEDRA':
    print('Máquina: {}✊'.format(maquina))

elif maquina == 'PAPEL':
    print('Máquina: {}✋'.format(maquina))

elif maquina == 'TESOURA':
    print('Máquina: {}✌️'.format(maquina))
