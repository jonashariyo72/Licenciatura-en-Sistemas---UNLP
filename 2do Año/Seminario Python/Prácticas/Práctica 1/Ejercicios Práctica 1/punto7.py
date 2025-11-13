#punto7

# Pedir al usuario que ingrese los números separados por espacios
entrada = input("Ingrese una lista de números separados por espacios: ")

# Convertir la entrada en una lista de enteros
numeros = list(map(int, entrada.split()))

cadena = ""

for num in numeros:
    if num % 3 == 0:
        continue
    else:
        cadena = cadena + "-" + str(num)

print (cadena)