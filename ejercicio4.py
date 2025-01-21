

cantidad = int(input("Introduce un numero "))

a, b = 0, 1
contador = 0


print("La sucesión de Fibonacci es:")
while contador < cantidad:
    print(a, end=" ")

    a, b = b, a + b
    contador += 1

