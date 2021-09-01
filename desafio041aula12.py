import datetime
ano = int(input('Digite o ano de nascimento do atleta (\033[1;36mAAAA\033[m): '))
anoatual = datetime.date.today().year
idade = anoatual - ano
if idade <= 9:
    print('Categoria do atleta: MIRIM (até 9 anos).')
elif 9 < idade <= 14:
    print('Categoria do atleta: INFANTIL (até 14 anos).')
elif 14 < idade <= 19:
    print('Categoria do atleta: JUNIOR (até 19 anos).')
elif 19 < idade <= 20:
    print('Categoria do atleta: SÊNIOR (até 20 anos).')
elif idade > 20:
    print('Categoria do atleta: MASTER (acima de 20 anos).')
