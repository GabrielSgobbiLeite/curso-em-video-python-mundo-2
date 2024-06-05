# analise de dados de grupo
print('=' * 30)
print('INICIADO PROGRAMA')
print('=' * 30)

soma_masculino = 0
soma_feminino = 0
soma_total = 0

while True:
    tipo = ' '
    tipo_1 = ' '
    print('=' * 30)
    print('CADASTRE UMA PESSOAL')
    idade = int(input('Idade:'))
    while tipo not in 'MF':
        tipo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if tipo == 'M':
        if idade > 18:
            soma_total += 1
        if idade > 0:
            soma_masculino += 1
        else:
            break
    elif tipo == 'F':
        if idade > 18:
            soma_total += 1
        if idade >= 20:
            soma_feminino += 1
    tipo_1 = str(input('Que continuar? [S/N]')).strip().upper()[0]
    if tipo_1 == 'S':
        print('='*30)
    else:
        print('FIM DO PROGRAMA')
        break
print(f'''Total de pessoas maiores de 18 anos foi {soma_total}
Número de homens cadastrados foi {soma_masculino}
Número de mulhres com ou mais de 20 foi {soma_feminino}''')
