print('='*20)
print('Insira o seu peso e altura para calcular o seu IMC.')
print('='*20)
altura = float(input('Dígite sua altura:'))
peso = float(input('Dígite seu peso:'))

IMC = peso / altura**2

if IMC < 18.5:
    print(f'abaixo do peso, seu IMC{IMC:.2f}')
elif IMC < 25:
    print(f'Peso ideal, seu IMC{IMC:.2f}')
elif IMC < 30:
    print(f'Sobrepeso, seu IMC{IMC:.2f}')
elif IMC < 40:
    print(f'Obesidade, seu IMC{IMC:.2f}')
else:
    print(f'Obesidade mórbida, seu IMC{IMC:.2f}')
