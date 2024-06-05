num = int(input('''Digite um número para
calcular o seu fatorial: '''))
cont = num
fat = 1
print('Calculando {}! = '.format(num), end='')
while cont > 0:
    print('{} '.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont = cont - 1
print(f'{fat}')
