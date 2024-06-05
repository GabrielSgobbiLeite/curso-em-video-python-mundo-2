primeira_nota = float(input('Dígite a sua primeira nota:'))
segunda_nota = float(input('Dígite sua segunda nota:'))

media = primeira_nota + segunda_nota
media = media / 2

if media <= 5.0:
    print('Reprovado')
elif media > 5.1 <= 6.9:
    print('recuperação')
elif media >= 7.0:
    print('aprovado')
