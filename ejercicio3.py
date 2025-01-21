from os import system
system("cls")
contra = "1234"
maximo = 3
intentos = 0
while True:  
    PIN= input("Introduce el PIN : ")  
    if PIN ==contra:
        print("Login correcto")
        break 
    else:
        intentos += 1
        print("pin incorrecto")
    if intentos == maximo:
        print("Llamando a la policía")
        break  
