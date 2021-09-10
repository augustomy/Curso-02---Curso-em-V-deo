maiorquemil = total = s = 0
maisbarato = ''
menorpreco = 0
while True:
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o preço do produto: R$'))
    while preco == ' ' or preco < 0:
        print('Preço inválido.')
        preco = float(input('Digite o preço do produto: R$'))
    if preco > 1000:
        maiorquemil = maiorquemil + 1
    
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        print('Opção inválida.')
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    s = s + 1
    if s == 1:
        menorpreco = preco
        maisbarato = produto
    else:
        if preco < menorpreco:
            menorpreco = preco
            maisbarato = produto
    total = total + preco
    if resp == 'N':
        break

print(f'Total gasto na compra: R${total:.2f}\nQuantidade de produtos que custam mais do que R$ 1000,00: {maiorquemil}\nProduto mais barato: {maisbarato}')
