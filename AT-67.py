while True:
    numero = int(input('Digite um numero:'))
    if numero < 0:
        break
    print('-'*30)
    for c in range(1, 10+1,):
        c *= numero
        print(c)
    print('-'*30)
print('seu progamar foi encerrado')
