SOMA = 0
CONTE = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        CONTE += 1
        SOMA += c
print(f'a soma de todos os valores é {SOMA} é os valores solicitado são {CONTE}')
