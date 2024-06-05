res = 'S'
cont = 0
soma = 0
media = 0
maior = 0
menor = 0
while res in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma/cont
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
