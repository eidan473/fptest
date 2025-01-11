from os import system
system("cls")

# edad=int(input("ingrese edad"))
# if edad>10 and edad<19:
#     print("su tiket vale 1000")
# if edad >18 and edad<66:
#     print("su tiket vale 2000")
# if edad>66:
#     print("su tiket vale 1500 ")
# if edad<=10:
#     print("su gratis")


# num1=int(input("inmgrese numero"))
# num2=int(input("ingrese numer"))
# if num1>num2:
#     print("el numero mayor es",num1)
# elif num1<num2:
#     print("el numero mayor es ",num2)

# x=int(input("tabla"))
# for  b in range (10):
#     print (x,"x",b+1,"=",(b+1)*(x))



total=0
while True:
    print("ingrse nombre 1")
    print("mostrar menu de platos 2")
    print("mostrar saludo al cliente 3")
    print("salir 4")
    opc=int(input())
    if opc==1:
        nombre=input("ingrese nombre\n")
        print("su nombre ahora es",nombre)
    if opc ==2:
        while True:
            print("arroz a la marinera 4500=1")
            print("arroz marinero 5200=2")
            print("sopá marinera 9700=3")
            print("salir=4")
            op=int(input())
            if op==1:
                total=total+4500
                print("usted quiere arroz a la marinera",total)
            if op ==2:
                total=total+5200
                print("usted quiere arroz marinero",total)
            if op==3:
                total=total+9700
                print("usted quiere sopa marinera")
            if op==4:
                print("salir")
                break
            if op>4:
                print("numero invalido")
    if opc==3:
        print("gracias",nombre,"por venir al restaurant")
    if opc== 4:
        print ("salir")
        break
    if opc>4:
        print ("numero invalido")
    