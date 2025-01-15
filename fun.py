from os import system
system("cls")

# def suma():
#     num1=int(input("ingrese numero"))
#     num2=int(input("ingrese numero"))
#     num1+num2
# def resta():
#     num1=int(input("ingrese numero"))
#     num2=int(input("ingrse numer"))
#     num1-num2
# def multiplicacion():
#     num1=int(input("ingrese numero"))
#     num2=int(input("ingrese numero"))
#     num1*num2
# def division():
#     num1=int(input("ingrse numero"))
#     num2=int(input("ingrese numero"))
#     num1/num2





# while True:
#     print("sumar")
#     print("restar")
#     print("multiplicar")
#     print("dividir")
#     print("salir")
#     op=int(input("ingrese ejercicio"))
#     match op:
#         case 1:
#             print("la suma de los nuemro es ",suma())
#         case 2:
#             print("la resta de los numeros es ", resta())
#         case 3:
#             print("la multiplicacion d los numeros es ", multiplicacion())
#         case 4:
#             print("la division de los numeros es ", division())
#         case 5:
#             break
#         case _:
#             print("invalido")



# num=int(input("ingrese numero"))
# for i in range(num+1):
#     print("*"*((i+1)-1))


deuda=100000


while True:
    print("pago de tarjeta de credito=1")
    print("comprar=2")
    print("salir=3")
    op=int(input())
    if op==1:
        print("su deuda es de 100000")
        print("ingrese monto a pagar")
        monto=int(input())
        if monto==deuda and monto<deuda:
            deuda=deuda-monto
            print("su deuda es de",deuda)          
        else :
            print("usted exede su deuda")
    elif op==2:
        while True:
            print("ingrese precio de la compra")
            compra=int(input())
            if compra>=0:
                compra=compra+deuda
                print("su deuda ahora es ",deuda)
                
              
        
    
