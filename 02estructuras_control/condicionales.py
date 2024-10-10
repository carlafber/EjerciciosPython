if(1<9):
    print("si")

dia = int(input("Introduzca día: "))
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6 | 7:
        print("Fin de semana")
    case _:
        print("Día inválido")
