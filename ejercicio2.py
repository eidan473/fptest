def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


num = 5
print("la factorial de", num, "es", factorial(num))
