import datetime
ano = int(input('Digite o ano de nascimento: \033[1;32m'))
anoatual = datetime.date.today().year
idade = anoatual - ano
print('\033[mQuem nasceu em \033[1;32m{}\033[m, tem \033[1;34m{}\033[m ano(s) em \033[1;35m{}\033[m.'.format(ano, idade, anoatual))
if idade > 18:
    print('Seu ano de alistamento ocorreu em \033[1;31m{}\033[m e foi há \033[1;31m{}\033[m ano(s) atrás.'.format(ano + 18, idade - 18))
elif idade < 18:
    print('Seu ano de alistamento será em \033[1;33m{}\033[m, daqui \033[1;33m{}\033[m ano(s).'.format(ano + 18, 18 - idade))
else:
    print('Seu alistamento ocorre(u) esse ano de \033[1;32m{}\033[m.'.format(anoatual))
    