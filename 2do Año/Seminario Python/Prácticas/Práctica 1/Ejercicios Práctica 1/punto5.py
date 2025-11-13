#punto5

# Pedir al usuario que ingrese los números separados por espacios
entrada = input("Ingrese una lista de números separados por espacios: ")

# Convertir la entrada en una lista de enteros
numeros = list(map(int, entrada.split()))

for num in numeros:
    if num < 0 :
        break
    print (num) 