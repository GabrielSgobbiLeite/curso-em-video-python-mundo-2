print('='*20)
print('\033[1mCalculo de Empréstimo\033[m')
print('='*20)

valor_da_casa = float(input('Dígite o valor da casa:'))
salario = float(input('Dígite o valor do seu salário:'))
tempo_de_pagamento = int(input('Em quanto tempo você que financiar a casa:'))

pagamento_mensal = valor_da_casa / tempo_de_pagamento

if salario * 30 / 100 >= pagamento_mensal:
    print(f'Você pode fazer o financiamento da casa que vai fica {pagamento_mensal}>')
else:
    print('Você não pode fazer o financiamento da casa, passa do limite do seu sálario.')
