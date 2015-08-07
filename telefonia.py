minutos = int(input("minutos : "))
if minutos < 200:
    preco = minutos * 0.20
    print ( "valor da conta : %.2f" %preco)
else:
    if minutos >= 200 and minutos <=400:
         preco = minutos * 0.18    
         print( "valor da conta : %.2f" %preco)
        
    else:
         preco = minutos * 0.15
         print("valor da conta : %.2f" %preco)
        
    
