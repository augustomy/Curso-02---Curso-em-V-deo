import datetime
ano = int(input('Digite o ano de nascimento do atleta: '))
anoatual = datetime.date.today().year
idade = anoatual - ano
if 0 <= idade <= 9:
    print('Em {}, o atleta tem/terá {} ano(s).\nCategoria: MIRIM'.format(anoatual, idade))
elif 9 < idade <= 14:
    print('Em {}, o atleta tem/terá {} ano(s).\nCategoria: INFANTIL'.format(anoatual, idade))
elif 14 < idade <= 19:
    print('Em {}, o atleta tem/terá {} ano(s).\nCategoria: JUNIOR'.format(anoatual, idade))
elif 19 < idade <= 25:
    print('Em {}, o atleta tem/terá {} ano(s).\nCategoria: SÊNIOR'.format(anoatual, idade))
elif idade > 25:
    print('Em {}, o atleta tem/terá {} ano(s).\nCategoria: MASTER'.format(anoatual, idade))
