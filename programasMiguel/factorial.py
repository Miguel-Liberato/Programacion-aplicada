def calcular_factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos"
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

# Solicitar al usuario un número para calcular su factorial
numero = int(input("Introduce un número para calcular su factorial: "))

resultado = calcular_factorial(numero)

if isinstance(resultado, int):
    print(f"El factorial de {numero} es {resultado}")
else:
    print(resultado)
