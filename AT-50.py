soma = 0
conta = 0
for c in range(0, 6):
    numero = int(input('digite um número interio?'))
    if numero % 2 == 0:
        soma += numero
        conta += 1
print(f'a soma de todos os valores é {soma} é os valores solicitado são {conta}')
