def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def calcular_primos_en_rango(inicio, fin):
    primos = []
    for num in range(max(2, inicio), fin + 1):
        if es_primo(num):
            primos.append(num)
    return primos

# Solicitar al usuario el rango
inicio = int(input("Introduce el inicio del rango: "))
fin = int(input("Introduce el final del rango: "))

if inicio > fin:
    print("El inicio del rango debe ser menor o igual al final del rango.")
else:
    numeros_primos = calcular_primos_en_rango(inicio, fin)
    if numeros_primos:
        print(f"Números primos en el rango ({inicio}, {fin}):")
        print(numeros_primos)
    else:
        print (f"No se encontraron números primos en el rango ({inicio}, {fin}).")
