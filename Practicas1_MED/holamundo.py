#Este es un comentario de una linea
#Este mensaje se mostrara por consola
print("Hola Mundo")

#Capturando datos de usuario
user_name = input("Cual es tu nombre: ")
user_age = input("Cuantos años tienes: ")

#Convirtiendo la edad en un numero entero
user_age = int(user_age)
#mostramos la informacion al usuario
print("Hola ", user_name)

#Evaluamos si el usuario es mayor de edad
if (user_age >= 18):
    print ("Eres mayor de edad por que tienes", user_age, "años")
else:
    print ("Eres menor de edad porque tienes", user_age,"años")