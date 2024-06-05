from random import randint

itens = ('pedra', 'papel', 'tesoura:')
computador = randint(0, 2)
print('vamos jogar jokenpô?')
opcao = int(input('escolha, (0)pedra, (1)papel ou (2)tesoura'))
print(f'Você jogou {(itens[opcao])}!')
print(f'o computador jogou {(itens[computador])}!')
if computador == 0:  # jogou pedra
    if opcao == 0:
        print('Empate!!')
    elif opcao == 1:
        print('Você Venceu!!')
    elif opcao == 2:
        print('Você perdeu!!')
    else:
        print('jogada ivalida')
if computador == 1:  # jogou papel
    if opcao == 0:
        print('Você perdeu!!')
    elif opcao == 1:
        print('Empate!!')
    elif opcao == 2:
        print('Você Venceu!!')
    else:
        print('jogada ivalida')
if computador == 2:  # jogou tesoura
    if opcao == 0:
        print('Você perdeu!!')
    elif opcao == 1:
        print('Você Venceu!!')
    elif opcao == 2:
        print('Empate!!')
    else:
        print('jogada ivalida')
