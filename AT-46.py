import time


TEMPO = 1  # tempo do contador
for c in range(10, -1, -1):
    print(f'{c}!!!')
    time.sleep(TEMPO)
print('Fogos de arteficios estorados!!')
