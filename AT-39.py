from datetime import date


ano_de_nacimento = int(input('Dígite o ano que você nasceu para saber quando você vai se alistar:'))

idade = date.today().year - ano_de_nacimento

if idade < 18:
    tempo_que_falta = 18 - idade
    print(f'Você tem {idade} está a {tempo_que_falta} ano para se alistar.')
elif idade == 18:
    print('estar na hora de se alistar.')
else:
    print('Já passou o tempo de você se alistar.')
