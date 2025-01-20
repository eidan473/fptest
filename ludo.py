from os import system
system("cls")
import random
import sys
ju1=0
ju2=0
def dado():
    return random.randint(1,6)
def juga1():
    global ju1
    while True:
        for i in range(1):
            print("jugador le toca",i+1)
            opc=int(input("presione 1 para iniciar"))
            if opc ==1:
                if i+1==1:
                    da=dado()
                    ju1=ju1+da
                    print("saco un ",da)
                    print("su posicion es ",ju1)
                    if ju1==24:
                        print("ganaste")
                        sys.exit()
                    elif ju1>24:
                        print("se paso")
                        ju1=ju1-da
def juga2():
    global ju1
    global ju2
    while True:
        for i in range(2):
            print("jugador",i+1)
            opc=int(input("presione 1 para iniciar"))
            if opc ==1:
                if i+1==1:
                    da=dado()
                    ju1=ju1+da
                    print("saco un ",da)
                    print("su posicion es ",ju1)
                    if ju1==24:
                        print("ganaste jugador 1")
                        sys.exit()
                    elif ju1>24:
                        print("se paso")
                        ju1=ju1-da
            if opc ==1:
                if i+1==2:
                    da=dado()
                    ju2=ju2+da
                    print("saco un ",da)
                    print("su posicion es ",ju2)
                    if ju2==24:
                        print("ganaste jugador 2")
                        sys.exit()
                    elif ju2>24:
                        print("se paso")
                        ju2=ju2-da


op=int(input("jugador cuanto queri ojo solo se puede de maximo 2"))
match op:
    case 1:
        juga1()
    case 2:
        juga2()




    