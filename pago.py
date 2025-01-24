from os import system
system("cls")
total=0
total2=0
total3=0
c=0
p=0
a=0
car=0



while True:
    print("comprar=1")
    print ("con que quiere pagar=2")
    print("mostrar boleta=3")
    opc=int(input())
    if opc ==1:
        while True:
            print("coca 1000=1")
            print("pepsi 2000=2")
            print("agua 500=3")
            print("carne perro 500=4")
            print("volver al menu principal=5")
            op=int(input())
            if op==1:
                total=total+1000
                c=c+1
                print("usted quiere coca",total)
            elif op==2:
                p=p+1
                total=total+2000
                print("usted quiere pepsi",total)
            elif op==3:
                a=a+1
                total=total+500
                print("usted quiere agua",total)
            elif op==4:
                car=car+1
                total=total+500
                print("usted quiere carnesita de perro",total)
            elif op==5:
                print("volvera al menu principal")
                total3=total*1.19
                break
            else:
                print("opc invalida")
    elif opc==2:
        while True:
            total2=total*1.19
            print("efectivo=1")
            print("devito=2")
            print("credito=3")
            opci=int(input())
            if opci==1:
                
                print("su pago no suma nada y el total a pagar es",total3)
                break
            elif opci==2:
                total2=total2*1.5
                print("su pago suma un 1,5 y su total es ",total2)
                break
            elif opci==3:
                total2=total2*2.89
                print ("su pago suma un 2,89 con credito",total2)
                break
    elif opc==3:
        print("coca",c)
        print("pepsi",p)
        print("agua",a)
        print("carne perro",car)
        print("sin iva",total)
        print("con iva",total3)
        print("en total",total2)
        break
        
                
            
            
        
            