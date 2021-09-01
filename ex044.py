preco = float(input('Digite o valor do produto: R$'))
escolha = int(input('''Escolha a forma de pagamento:
1 - A vista dinheiro/cheque (10% de desconto);
2 - A vista no cartão (5% de desconto);
3 - Em até 2x no cartão (Preço normal);
4 - 3x ou mais no cartão (20% de juros).\n'''))
if escolha == 1:
    total = 0.9 * preco
    print('Valor a ser pago: R${:.2f}'.format(total))
elif escolha == 2:
    total = 0.95 * preco
    print('Valor a ser pago: R${:.2f}'.format(total))
elif escolha == 3:
    total = preco
    print('Valor a ser pago: R${:.2f}'.format(total))
elif escolha == 4:
    total = 1.2 * preco
    print('Valor a ser pago: R${:.2f}'.format(total))
else:
    print('Ocorreu um erro. Tente novamente.')
