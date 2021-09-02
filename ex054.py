import datetime
anoatual = datetime.date.today().year
s = 0
z = 0
for c in range(1, 7+1, 1):
    a = int(input('Digite o ano de nascimento ({}): '.format(c)))
    if anoatual - a  >= 21:
        s = s + 1
    else:
        z = z + 1
print('Maioridade: {} pessoa(s)\nMenoridade: {} pessoa(s)'.format(s, z))
