from random import randint
from time import sleep

h = 0
dado = randint(1, 100)
print('___'*20)
print('VOU SORTEAR UM NÚMERO...'.center(43))
print('___'*20)
sleep(2)
while True:
    h += 1
    s = int(input('Tente adivinhar em que número eu pensei: '))
    print('___'*20)
    if s == dado:
        print(f'Parabéns, você acertou com {h} tentativas !')
        break
    else:
        print('Você errou !')
        print('___'*20)
        if dado < s:
            print('Tente um número menor !')
            print('___' * 20)
        if dado > s:
            print('Tente um número maior !')
            print('___'*20)
