def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    resultado = fibonacci(n-2) + fibonacci(n-1)
    print(resultado)
    return resultado

n = int(input("ingrese numero: "))
fibonacci(n)