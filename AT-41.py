from datetime import date


data_de_nacimento = int(input('Qual o ano que você nasceu:'))

idade = date.today().year - data_de_nacimento

if idade <= 9:
    print(f'Você pode tem {idade}, você pode ser um atleta mirim.')
elif idade <= 14:
    print(f'Você tem {idade}, você pode ser um atleta infantil.')
elif idade <= 19:
    print(f'Você tem {idade}, você pode ser um atleta junior.')
elif idade <= 20:
    print(f'Você tem {idade}, você pode ser um atleta sênior.')
else:
    print(f'Você tem {idade}, você pode ser um atleta master.')
