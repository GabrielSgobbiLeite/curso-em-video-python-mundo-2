primeiro_termo = int(input('diga o primeiro termo da sequencia:'))
razao = int(input('agora a razão:'))
decimo = primeiro_termo+(10-1)*razao
for c in range(primeiro_termo, decimo+razao, razao):
    print(c)
