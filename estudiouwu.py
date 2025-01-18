from os import system
system("cls")


# total=0
# while True:
#     print("ingrese opcion")
#     print("comprar=1")
#     print("salir=2")
#     opc=int(input())
#     if opc==1:
#         while True:
#                 print("bienvenido al menu")
#                 print("pan 1000=1")
#                 print("bebia 2000=2")
#                 print("cereal 1500=3")
#                 print("pagar=4")
#                 print("volver al menu principal=5")
#                 op=int(input("ingrese lo que va a comprar"))
#                 if op==1:
#                      total=total+1000
#                      print("usted quiere pan y su total es",total )
#                 elif op==2:
#                      total=total+2000
#                      print("usted quiere bebia y su total es",total)
#                 elif op==3:
#                      total=total+1500
#                      print("usted quiere cereal y su total es",total)
#                 elif op==4:
#                         while True:
#                              print("con quiere pagar")
#                              print("devito 20%=1")
#                              print("credito=10%=2")
#                              print("efectivo=3")
#                              print("salir=4")
#                              opci=int(input()) 
#                              if opci==1:
#                                 total=total*0.80
#                                 print("usted pagara con devito y su total es ",total,"gracias por comprar")
#                              elif opci==2:
#                                   total=total*0.90
#                                   print("pagara con creditoy su total es ",total,"gracias por comprar")
#                              elif opci==3:
#                                   print ("pagara con efectivo y su total es",total,"gracias por comprar")
#                              elif opci==4:
#                                   print("salir")
#                                   break
#                              else:
#                                 print("nonono malo")
#                 elif op==5:
#                     print("vuelve al menu principal")
#                     break
#                 else:
#                  print("nonono malo")
#     if opc==2:
#          print("salir")
#          break
#     else:
#         print("nonono malo")

# import sys

# while True:
#     print("crear cuenta= 1")
#     print("inciar seccion=2")
#     print("salir")
#     opc=int(input())
#     if opc==1:
#         while True:
#             print("crear nombre usuario")
#             nom=input()
#             print("crear contraseña")
#             contra=input()
#             break
#     if opc==2:
#         while True:
#              print("inciar seccion cual es su nombre de usuario")
#              nom1=input()
#              if nom1==nom:
#                 print ("correcto")
#              elif nom1!=nom:
#                  print("siguiente")
#              con1=input("ingrese contra")
#              if con1==contra:
#                 print("su contraseña es correcta")
#                 print("bienvenido")
#                 sys.exit()
#              elif con1!=contra:
#                 print("contraseña o usuario incorrecta ")



# import random
# def ruleta():
#     return random.randint(1,6)
# bala=ruleta
# for i in range (6):
#     print("bienvenido a la ruleta")

ju1=60
ju2=60

p1=""
p2=""
import random
def atake():
    return random.randint(2,10)
ataki=atake()


def persona():
    while True:
        print("apreta 1 para que el jugador 1 elija personaje")
        print("apreta 2 para que el jugador 2 elija personaje")
        print("jugar=3")
        
        op=int(input())
        if op==1:
            while True:
                print("elija personaje")
                print("ryu=1")
                print("chun-Li=2")
                print("ken=3")
                print("Blanka=4")
                opc=int(input())
                if opc==1:
                    print("usted elije a ryu")
                    p1="ryu"
                    break
                elif opc==2:
                    p1="chun_Li"
                    print("usted elije a chun_Li")
                    break
                elif opc==3:
                    p1="ken"
                    print("usted elije a ken")
                    break
                elif opc==4:
                    p1="blanka"
                    print("usted elije a blanka") 
                    break
                else:
                    print("opc invalida")
        elif op==2:
            while True:
                print("elija personaje")
                print("ryu=1")
                print("chun-Li=2")
                print("ken=3")
                print("Blanka=4")
                opc=int(input())
                if opc==1:
                    p2="ryu"
                    print("usted elije a ryu")
                    break
                elif opc==2:
                    p2="chun-li"
                    print("usted elije a chun_Li")
                    break
                elif opc==3:
                    p2="ken"
                    print("usted elije a ken")
                    break
                elif opc==4:
                    p2="blanka"
                    print("usted elije a blanka")
                    break
        elif op ==3:
            print("jugar")
            break
def jugar():
    while True:
        print("jugador 1 es tu turno=4")
        opcii=int(input())
        if opcii==4:
            while True:
                print("jugador 1 lanzara el primer ataque")
                print("para atakar selecione 8")
                atak=int(input())
                if atak==8:
                    ju2-ataki
                    print("lo dejaste a ",ju2)
        print("jugador 2 es tu turno")
        opcii=int(input())
        if opcii==4:
            while True:
                print("jugador 1 lanzara el primer ataque")
                print("para atakar selecione 8")
                atak=int(input())
                if atak==8:
                    ataki-ju1
                    print("lo dejaste a ",ju1)
                
                    
                    
                    
                
                
                
                
    
opi=int(input("1 para elejir personaje y 2 para jugar"))
match opi:
    case 1:
        persona()
        print(p1)
        print(p2)
        jugar()
    case 2:
        jugar()
        
        
    
    




       

            


