from random import randint
l = ['sim', 'nao']

while True:
    ask = str(input(('\nVoce gostaria de jogar o Dado? '))).lower()
    if ask not in l:
        print('\nInforme uma resposta valida: sim ou nao.')
    if ask == 'nao':
        break
    elif ask == 'sim':
        value = randint(1,6)
        print(value)