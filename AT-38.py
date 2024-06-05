primeiro_numero = int(input('Dígite um número inteiro:'))
segundo_numero = int(input('Dígite outro número:'))

if primeiro_numero > segundo_numero:
    print('O primeiro número é maior que o segundo.')
elif segundo_numero > primeiro_numero:
    print('O segundo número é maior que o primeiro')
elif primeiro_numero == segundo_numero:
    print('Não existe valor maior, os dois número são iguais')
