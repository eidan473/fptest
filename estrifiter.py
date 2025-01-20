ju1=60
ju2=60

p1=""
p2=""
import random
def atake():
    return random.randint(2,10)
def persona():
    global ju1
    global ju2
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
                    p1="ryu"
                    print("usted elije a ",p1)
                    
                    break
                elif opc==2:
                    p1="chun_Li"
                    print("usted elije a ",p1)
                    break
                elif opc==3:
                    p1="ken"
                    print("usted elije a ",p1)
                    break
                elif opc==4:
                    p1="blanka"
                    print("usted elije a ",p1) 
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
                    print("usted elije a",p2)
                    break
                elif opc==2:
                    p2="chun-li"
                    print("usted elije a",p2)
                    break
                elif opc==3:
                    p2="ken"
                    print("usted elije a ",p2)
                    break
                elif opc==4:
                    p2="blanka"
                    print("usted elije a ",p2)
                    break
        elif op ==3:
            print("jugar")
            break
def jugar():
    global p1
    global p2
    global ju1
    global ju2
    while True:
        for i in range(2):
            print("turno del jugador 1 presione uno para atakar")
            jugar=int(input("presione 1"))
            if jugar==1:
                if  i==0:
                    ju2=ju2-atake()
                    
                    print(" la vida que lo dejo es a",ju2)
                    if ju2==0:
                        print ("gana",p1)
                        break
            print("turno del jugador 2 presione 2 para atakar")
            jugar=int(input("ingrese 2"))
            if jugar==2:
                if i==1:
                    ju1=ju1-atake()
                    print(" la vida que lo dejo es a",ju2)
                    if ju2==0:
                        print ("gana",p2)
                        break
persona()
jugar()         