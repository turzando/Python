from random import randint

answers = ['Sim, vai la.', 'Simbora, mofio.', 'Vambora.',
'Maseclaro','Com certeza.','Nao, macho.','Mermao, ce quem sabe.',
'Sei nao em...','ta loko.','Claro que nao, azideia do leke.']

while True:
        print('\nEscreva sua pergunta e obterá uma resposta (escreva sair para parar).\n')
        ask = str(input('Pergunta: ')).lower()
        if ask.isnumeric():
            print('Digite apenas letras.')
            continue
        if ask == 'sair':
            break
        value = randint(0,9)
        print(f'Resposta: {answers[value]}')