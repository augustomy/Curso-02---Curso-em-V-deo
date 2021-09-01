#a = float(input('Digite a primeira reta: '))
#b = float(input('Digite a segunda reta: '))
#c = float(input('Digite a terceira reta: '))
#if (abs(b-c) < a < (b+c) and abs(a-c) < b < (a+c) and abs(a-b) < c < (a+b)) and (a == b == c):
#    print('\033[1;32mSIM! É possível formar um triângulo com as dimensões informadas.\033[m')
#    print('Será um triângulo \033[1;34mEQUILÁTERO\033[m com lados medindo {}'.format(a))
#elif (abs(b-c) < a < (b+c) and abs(a-c) < b < (a+c) and abs(a-b) < c < (a+b)) and (a != b != c):
#    print('\033[1;32mSIM! É possível formar um triângulo com as dimensões informadas.\033[m')
#    print('Será um triângulo \033[1;35mESCALENO\033[m com lados medindo {} | {} | {} |'.format(a, b, c))
#elif (abs(b-c) < a < (b+c) and abs(a-c) < b < (a+c) and abs(a-b) < c < (a+b)) and (a == b != c) or (c == b != a) or (a == c != b):
#    print('\033[1;32mSIM! É possível formar um triângulo com as dimensões informadas.\033[m')
#    print('Será um triângulo \033[1;36mISÓSCELES\033[m com lados medindo {} | {} | {} |'.format(a, b, c))
#else:
#    print('\033[1;31mNão é possível formar um triângulo com as dimensões informadas.\033[m')

#OUTRA FORMA DE FAZER ESSE EXERCÍCIO:
a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))
if (abs(b-c) < a < (b+c) and abs(a-c) < b < (a+c) and abs(a-b) < c < (a+b)):
    print('\033[1;32mSIM! É possível formar um triângulo com as dimensões informadas.\033[m')
    if a == b == c:
        print('Será um triângulo \033[1;34mEQUILÁTERO\033[m com lados medindo {}'.format(a))
    elif a != b != c:
        print('Será um triângulo \033[1;35mESCALENO\033[m com lados medindo {} | {} | {} |'.format(a, b, c))
    else:
        print('Será um triângulo \033[1;36mISÓSCELES\033[m com lados medindo {} | {} | {} |'.format(a, b, c))
else:
    print('\033[1;31mNão é possível formar um triângulo com as dimensões informadas.\033[m')

