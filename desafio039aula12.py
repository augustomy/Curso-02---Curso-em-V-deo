import datetime
ano = int(input('Digite o ano de nascimento (\033[1;34mAAAA\033[m): '))
anoatual = datetime.date.today().year
idade = anoatual - ano
if idade > 18:
    passou = idade - 18
    print('Já se passaram \033[1;31m{}\033[m ano(s) do seu alistamento.'.format(passou))
elif idade < 18:
    alistamento = 18 - idade
    print('Falta(m) \033[1;33m{}\033[m ano(s) para você se alistar!'.format(alistamento))
else:
    print('Esse é o ano para você se alistar!'.format(idade))
