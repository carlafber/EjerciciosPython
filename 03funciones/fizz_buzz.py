def funcion(texto1, texto2):
    cont = 100
    for n in range(1, 101):
        if((n%3==0) and (n%5==0)):
            cont = cont - 1
            print(texto1 + texto2)
        elif(n%3==0):
            cont = cont - 1
            print(texto1)
        elif(n%5==0):
            cont = cont - 1
            print(texto2)
        else:
            print(n)
    return cont
    

print("total: " + str(funcion(input(), input())))
