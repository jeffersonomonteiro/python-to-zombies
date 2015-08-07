minutos = int(input("minutos : "))
if minutos < 200:
    preco = 0.21
else:
    if minutos <= 400:
        preco = 0.18


print (minutos*preco)
