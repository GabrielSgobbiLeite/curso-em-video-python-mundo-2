# fazer um jogo de par ou ímpar(para o jogo acabar o computador tem que vence)

from random import randint

soma = 0
vitorias = 0

print('=' * 30)
print('VAMO JOGAR PAR OU ÍMPAR')
print('=' * 30)
while True:
    jogador = int(input('Diga um número:'))
    computador = randint(1, 11)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador} a soma é {soma}', end=' ')
    print('Deu Par' if soma % 2 == 0 else 'Deu Ímpar')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você Venceu')
            vitorias += 1
        else:
            print('Você Perdeu')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você Venceu')
            vitorias += 1
        else:
            print('Você Perdeu')
            break
    print('Vamos jogar denovo')
print(f'Game Over! Você venceu {vitorias} vezes')
