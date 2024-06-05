print('-=' * 20)
print('analizador de triângulos')
print('-=' * 20)

primeiro_segmento = float(input('primeiro segmento:'))
segundo_segmento = float(input('segundo segmento:'))
terceiro_segmento = float(input('terceiro segmento'))

if primeiro_segmento < segundo_segmento + terceiro_segmento and segundo_segmento < primeiro_segmento + terceiro_segmento and terceiro_segmento < primeiro_segmento + segundo_segmento:
    print('os segmentos podem formar um triângulo.')
else:
    print('os segmentos não podem formar um triângulo.')

if primeiro_segmento == segundo_segmento == terceiro_segmento:
    print('Formar um Triâgulo Equilátero')
elif primeiro_segmento == segundo_segmento != terceiro_segmento and primeiro_segmento == terceiro_segmento != segundo_segmento and segundo_segmento == primeiro_segmento != terceiro_segmento and segundo_segmento == terceiro_segmento != primeiro_segmento and terceiro_segmento == primeiro_segmento != segundo_segmento and terceiro_segmento == segundo_segmento != primeiro_segmento:
    print('formar um triâgulo Isósceles')
else:
    print('formar um triâgulo Escaleno')
