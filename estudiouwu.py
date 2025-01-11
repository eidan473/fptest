from os import system
system("cls")



# con="uwu?"
# while True:
#     contraseña=(input("ingresa contraseña"))
#     if contraseña==con:
#         print("ta bien")
#         break
#     else:
#         print("ta mal")




# edad=int(input("ingrese edad"))
# ingreso=int(input("ingrese su sueldo"))
# if edad>16 and ingreso>1000:
#     print("puede tributar")
# else:
#     print ("no puede tributar")

saldo=100


while True:
    print("ver saldo=1")
    print("sacar saldo=2")
    print("depositar=3")
    print("salir")                 
    opc=int(input())
    if opc==1:
        print("su saldo es",saldo)
    elif opc==2:
        sacar=int(input("cuanto va a sacar"))
        if saldo<sacar:
            print("error no tiene ese dinero")
        elif saldo>=sacar:  
            saldo=saldo-sacar
            print ("usted tiene ",saldo)
    elif opc==3:
        depositar=int(input("cuanto deposita"))
        saldo=saldo+depositar
        print("saldo es",saldo)
    elif opc==4:
        print("salir")
        break
    else:
        print("nonono malo")
    
    


       

    

