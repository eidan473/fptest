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

import sys

while True:
    print("crear cuenta= 1")
    print("inciar seccion=2")
    print("salir")
    opc=int(input())
    if opc==1:
        while True:
            print("crear nombre usuario")
            nom=input()
            print("crear contraseña")
            contra=input()
            break
    if opc==2:
        while True:
             print("inciar seccion cual es su nombre de usuario")
             nom1=input()
             if nom1==nom:
                print ("correcto")
             elif nom1!=nom:
                 print("siguiente")
             con1=input("ingrese contra")
             if con1==contra:
                print("su contraseña es correcta")
                print("bienvenido")
                sys.exit()
             elif con1!=contra:
                print("contraseña o usuario incorrecta ")
                


       

            


