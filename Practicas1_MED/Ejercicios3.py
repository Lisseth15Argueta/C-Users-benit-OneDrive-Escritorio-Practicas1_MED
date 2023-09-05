numeros = []
for i in range(5):
    numero = float(input("Ingrese un número: "))
    numeros.append(numero)

ordenados = []
while numeros:
    minimo = numeros[0]
    for numero in numeros:
        if numero < minimo:
            minimo = numero
    ordenados.append(minimo)
    numeros.remove(minimo)

print("Números ordenados de forma ascendente:", ordenados)