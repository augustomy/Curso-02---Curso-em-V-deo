preconormal = float(input('Digite o preço do produto: R$'))
escolha = int(input("""Selecione a forma de pagamento:
\033[1;37m1 para a vista no dinheiro ou cheque\033[m;
\033[1;36m2 para a vista no cartão\033[m;
\033[1;35m3 para até 2x no cartão\033[m;
\033[1;34m4 para 3x ou mais no cartão\033[m.\n"""))
if escolha == 1:
    valor = preconormal * 0.9
    print('Forma de pagamento escolhida: \033[1;37ma vista no dinheiro ou cheque\033[m.\nValor a ser pago: R${:.2f}'.format(valor))

elif escolha == 2:
    valor = preconormal * 0.95
    print('Forma de pagamento escolhida: \033[1;36ma vista no cartão\033[m.\nValor a ser pago: R${:.2f}'.format(valor))

elif escolha == 3:
    valor = preconormal
    print('Forma de pagamento escolhida: \033[1;35mpara até 2x no cartão\033[m.\nValor a ser pago: R${:.2f}'.format(valor))

elif escolha == 4:
    valor = preconormal * 1.2
    print('Forma de pagamento escolhida: \033[1;34mpara 3x ou mais no cartão\033[m.\nValor a ser pago: R${:.2f}'.format(valor))
else:
    print('\033[1;31mOcorreu um erro.\nPor gentileza tente novamente\033[m.')
