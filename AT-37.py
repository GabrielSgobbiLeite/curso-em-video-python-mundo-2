numero_inteiro = int(input('Dígite um número:'))
base_de_convercao = int(input('''Dígite [1] para para converter em binário, 
[2] para octal, [3] para hexadecimal:'''))

if base_de_convercao == 1:
    binario = bin(numero_inteiro)
    print(f'O seu número inteiro {numero_inteiro} foi convertido para {binario}.')
elif base_de_convercao == 2:
    octal = oct(numero_inteiro)
    print(f'O seu número inteiro {numero_inteiro} foi convertido para {octal}.')
elif base_de_convercao == 3:
    hexadeciamal = hex(numero_inteiro)
    print(f'O seu número inteiro {numero_inteiro} foi convertido para {hexadeciamal}.')
else:
    print('você colocou uma formatação não disponível')
