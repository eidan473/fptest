
n = int(input("Introduce el número de porte"))


if n <= 1:
    print("El número debe ser mayor que 1.")
else:
   
    for i in range(1, n + 1):
       
        print('*' * i)
