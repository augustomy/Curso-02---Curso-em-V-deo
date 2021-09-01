casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário: R$'))
anos = float(input('Em quanto(s) ano(s) irá pagar o empréstimo? '))

meses = anos * 12
parcelamensal = casa / meses

print('Valor da casa: R${:.2f}\nSalário informado: R${:.2f}\nTempo: {} ano(s)'.format(casa, salario, anos))

if parcelamensal >= 0.3*salario:
    print('\033[1;31mInfelizmente seu empréstimo foi negado\033[m.\n\033[1;33mMotivo: Prestação mensal excedeu 30% do salário informado.\033[m')
else:
    print('\033[1;32mParabéns! Seu empréstimo foi aprovado!\033[m')
