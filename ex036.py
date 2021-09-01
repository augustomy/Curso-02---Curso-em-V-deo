casa = float(input('Valor da casa: R$\033[1;32m'))
salario = float(input('\033[mValor mensal do salário: R$\033[1;32m'))
tempo = float(input('\033[mEm quantos anos irá pagar? \033[1;32m'))
meses = tempo * 12
prestacao = casa / meses
print('\033[mValor da casa: R${:.2f}\nSalário: R${:.2f}\nTempo: {} ano(s)'.format(casa, salario, tempo))
if prestacao <= 0.3 * salario:
    print('\033[1;32mEmpréstimo APROVADO\033[m!')

else:
    print('\033[1;31mEmpréstimo NÃO APROVADO\033[m!')
