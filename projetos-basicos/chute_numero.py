from random import randint

value = randint(1,10)
print('\bUm numero aleatorio entre 1 e 10 foi gerado.')

while True:
    try:
        ask = int(input('\nChute um numero (0 para desistir): '))
        if ask > value:
            print('Voce chutou um numero maior.')
        elif ask < value and ask != 0:
            print('Voce chutou um numero baixo.')
        elif ask == value:
            print('Parabens, você acertou.')
            break
        elif ask == 0:
            print('Uma pena, voce estava quase conseguindo. A resposta era {}'.format(value))

    except ValueError:
        print('Digite apenas numeros.')
