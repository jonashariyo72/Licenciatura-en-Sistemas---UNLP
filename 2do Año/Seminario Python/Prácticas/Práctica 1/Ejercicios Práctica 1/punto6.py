#punto6

lista = [1,2,3,4,5,6,7,8,9,10]

pares = []
impares = []

for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append (num)

print ("Lista de pares", pares)

print ("Lista de impares" , impares)
    
        