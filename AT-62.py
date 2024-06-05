print("="*20)
print("10 TERMOS DE UMA PA")
print("="*20)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = a1
c = 1
total = 0
termosamais = 10
quant = 0
while termosamais != 0:
    total = total + termosamais
    while c <= total:
        print(f'{termo} ', end='')
        termo = termo + r
        c += 1
        quant += 1
    print('PAUSA')
    termosamais = int(input('''Quantos termos a mais você quer mostrar ? '''))
print(f'Progressão finalizada com {quant} termos mostrados. ')
