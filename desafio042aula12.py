a = float(input('Digite o valor da \033[1;33mprimeira reta\033[m: '))
b = float(input('Digite o valor da \033[1;34msegunda\033[m reta: '))
c = float(input('Digite o valor da \033[1;35mterceira reta\033[m: '))
if abs(b-c) < a < b+c and abs(a-c) < b < a+c and abs(a-b) < c < a+b and a == b == c:
    print('\033[1;32mSim, é possível formar um triângulo com os valores informados\033[m: \033[1;33m{}\033[m | \033[1;34m{}\033[m | \033[1;35m{}\033[m'.format(a, b, c))
    print('Teremos um triângulo EQUILÁTERO.')

elif abs(b-c) < a < b+c and abs(a-c) < b < a+c and abs(a-b) < c < a+b and a != b != c:
    print('\033[1;32mSim, é possível formar um triângulo com os valores informados\033[m: \033[1;33m{}\033[m | \033[1;34m{}\033[m | \033[1;35m{}\033[m'.format(a, b, c))
    print('Teremos um triângulo ESCALENO.')

elif abs(b-c) < a < b+c and abs(a-c) < b < a+c and abs(a-b) < c < a+b and a == b != c or a == c != b or b == c != a:

    print('\033[1;32mSim, é possível formar um triângulo com os valores informados\033[m: \033[1;33m{}\033[m | \033[1;34m{}\033[m | \033[1;35m{}\033[m'.format(a, b, c))
    print('Teremos um triângulo ISÓSCELES.')

else:
    print('\033[1;31mNão é possível formar um triângulo com os valores informados.\033[m')  
