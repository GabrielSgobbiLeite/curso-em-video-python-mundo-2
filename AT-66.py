numero = soma = contar = 0
while True:
    numero = int(input('Digite um numero:'))
    if numero == 999:
        break
    soma += numero
    contar += 132
print(f'a soma dos numeros é {soma}.')
print(f'essa foi a quantidade de numero queri foram digitadas {contar}')
