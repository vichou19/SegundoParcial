"""
desarrollo un programa en pyton que le permita generer un numero aleatorio dentro de un rango definido por 
el usuario 

y ajustarlo dividiendo entre 4 

luego el usuario deveria adivinar el numero
entre un maximo de 3 intentos luego el usuario deberia adivinar el maximo en un rango de 3 intentos


cindicion 1
ingreso de datos
condicion a y b
el usuario ingresa 2 numeros enteros
que representan el rango numerico
el primer numero debe ser menor que el segundo

#-------------no entendi si era otro ejercicio o seguia con el mismo----------------

numero 2 generacion del numero aleatorio a se elige un numero aletorio dentro del rango ingresado b el numero 
se ajusta dividiendo entre 4 y 
redondealo al numero
3 intento del usuario
a, si el usuario asierta se muestra un mensaje de felicitacion
segundo intento , si el usuario no asierta se le indica si el numero es mayor o menor
tercer intento si no asierta nuevamente se le devuelve a dar una pista
si no asierta en los 3 intentos el programa muestra un :intenta nuevamente

"""

#1


#importamos la carpeta
import random

# Pedimos los límites
lower_limit = int(input("Introduce el límite inferior: "))
print()
upper_limit = int(input("Introduce el límite superior: "))
print()

# Validamos los límites
while lower_limit >= upper_limit:
    print("El límite inferior debe ser menor al límite superior. Intenta de nuevo.")
    print()
    lower_limit = int(input("Introduce el límite inferior: "))
    upper_limit = int(input("Introduce el límite superior: "))

# Generamos el número aleatorio
numero_generado = random.randint(lower_limit, upper_limit)
numero_dividido = numero_generado // 4

print("He generado un número aleatorio entre los límites y lo he dividido entre 4.")
print()
#juego

print("Tienes 3 intentos para adivinar el numero dividivo entre 4")
print()
for intentos in range(1,4):
    respuesta = int(input(f"intento,{intentos} :cual crees que es el numero dividido entre 4?:"))
    if respuesta == numero_dividido:
        print(f"!CORRECTO!El numero era {numero_dividido}")
        break
    elif intentos == 3:
        print(f"1Se te acabaron los intentos! El numero era {numero_dividido}")
    else:
        print("Incorrecto, intenta nuevamente")





