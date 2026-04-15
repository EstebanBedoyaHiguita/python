numero = int(input("Ingresa un número para calcular su factorial: "))

if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    factorial = 1
    contador = 1

    while contador <= numero:
        factorial *= contador
        contador += 1

    print(f"El factorial de {numero} es: {factorial}")
