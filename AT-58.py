from random import randrange
tentaivas = 1
computador = randrange(0, 10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi ?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais ... Tente mais uma vez.')
        if jogador > computador:
            print('Menos ... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')