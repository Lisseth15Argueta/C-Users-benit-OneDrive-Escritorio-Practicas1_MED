numero = float(input("Ingrese un número real: "))

print("Tabla de multiplicar del número", numero)

for i in range(1, 11):
    producto = numero * i
    print("{:.2f} x {:2d} = {:.2f}".format(numero, i, producto))