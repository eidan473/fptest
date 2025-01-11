from os import system
system("cls")



# edad=int(input("ingrese edad "))
# if edad>10 and edad <19:
#     print("su entrada vale 1000")
# if edad>18 and edad<66:
#     print("la entrada vale 2000")
# if edad>65:
#     print("la entrada vale 1500")
# if edad <=10:
#     print("el ticket es gratis")




# num1=int(input("ingrse numero"))
# num2=int(input("ingrse numero"))
# if num1>num2:
#     print(num1,"es mayor")
# if num1<num2:
#     print (num2,"es mayor")



# x=int(input("tabla"))
# for  b in range (10):
#     print (x,"x",b+1,"=",(b+1)*(x))




total=0
while True:
    print("ingrse su nombre=1")
    print("ingresa al menu=2")
    print("saludo=3")
    print("salir=4")
    opc=int(input())
    if opc==1:
        nom=input("ingreser nombre\n")
        print(f"su nombre ahora es {nom}")
    if opc==2:
        while True:
            print("elija una opcion de comida para elejir debe seleccionar el numero que esta en el = \n arroz_ala_francesa 4.500 =1\n arroz_mariner5.200 =2 \n sopa_marinera 9.700 =3  \n salir=4")
            op =int(input())
            if op==1:
                total=total+4500
                print("quiere arroz a la francesa\n",total)
            if op==2:
                total=total+5200
                print("quiere arroz marinero\n",total)
            if op==3:
                total=total+9700
                print ("sopa marinera\n",total)
            if op ==4:
                print("salir")
                break
            elif op >4:
                print("Opción no válida por favor intente nuevamente.")
     
    if opc==3:
        print("gracias",nom,"por venir restaurant panuchis")
    if opc==4:
         print("salir")
         break
    elif opc >4:
        print("Opción no válida por favor intente nuevamente.")
     
                
        
                

    