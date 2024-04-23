def factorial(n):
    if n == 1:
        return 1
    resultado = n * factorial(n-1)
    return resultado

n = int(input("ingrese numero para calcular su factorial: "))
print("su resultado es: ", factorial(n))