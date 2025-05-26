#1 ejercicio practica

"""
LA GENTE DE DIREC TV NESECITA MEJORAR SU MENU DE OPCIONES POR ENDE ELLOS NOS PRESENTAN
EL SIGUIENTE MENU
1 Para navegar dentro de las peliculas
2 Para grabar una pelicula
3 Configurar decodificador
4 Para salir
"""

#2 ejercicio para la prueba 3(●'◡'●)

"""
Haga un menu que permita hacer la siguiente function
menu principar
1 ingrese un numero
2 mostrar mayor
3 mostrar promedio
4 salir del ejercicio

opcion numero 1/ debe permitir ingresar un numero entero entre el 0 y el 100
por excepcion ya que incluso podria ingresar un string o un numero si el usuario no
ingresaun numero entero deberia sollicitar en pantalla (debe ingresar un numero entero)

opcion 2/ debe mostrar el numero mayor ingresadohasta ese momento
opcion 3/ debe mostrar el promedio ingresado hasta ese momento
si no se ah ingresado ningun numero, pedir estimado ingrese primero el valor

opcion 4/ salir, dar un mensaje de adios
"""

numeros = []

# Funciones auxiliares
def ingresar_numero():
    while True:
        entrada = input("Introduce un número entero entre 0 y 100: ")
        if entrada.isdigit():
            numero = int(entrada)
            if 0 <= numero <= 100:
                numeros.append(numero)
                print("Número ingresado correctamente.")
                break
            else:
                print("El número debe estar entre 0 y 100. Intenta nuevamente.")
        else:
            print("Debes ingresar un número entero.")

def mostrar_mayor():
    if numeros:
        print(f"El número mayor ingresado hasta ahora es: {max(numeros)}")
    else:
        print("No se han ingresado números. Por favor, utiliza la opción 1 primero.")

def mostrar_promedio():
    if numeros:
        promedio = sum(numeros) / len(numeros)
        print(f"El promedio de los números ingresados es: {promedio:.2f}")
    else:
        print("No se han ingresado números. Por favor, utiliza la opción 1 primero.")

# Menú principal
opcion = -1
while opcion != 4:
    print("\nMenú Principal")
    print("1. Ingresar un número")
    print("2. Mostrar número mayor")
    print("3. Mostrar promedio")
    print("4. Salir")

    try:
        print()
        opcion = int(input("Elige una opción: "))
        print()
        if opcion == 1:
            ingresar_numero()
        elif opcion == 2:
            mostrar_mayor()
        elif opcion == 3:
            mostrar_promedio()
        elif opcion == 4:
            print("Gracias por utilizar el programa. ¡Adiós!")
        else:
            print("Opción no válida. Intenta nuevamente.")
    except ValueError:
        print("Debes ingresar una opción válida numérica.")

#3 ejercicio para prueba 3

"""
contruya un programa en python que permita verificar si una persona a completado
su esquema de vacunacion, el programa debe comenzar preguntandole
ingresa un numero indicando la cantidad de personas a ingresar, el numero debe ser entero
luego para cada persona generar el registro
el registro a nuestra discrecion
el programa debe solicitar la dosis que an sido administraba
esquema completo en caso contrario con ✖️, y si no ✅
una vez ingresado los datos a mostrar en pantalla
deberia tener una opcion para entrar y salir
validar si pone un decimal mandar mensaje( ingresa numero entero)
"""

print("Bienvenido al registro de esquemas de vacunación")
while True:
    cantidad = input("Introduce la cantidad de personas a registrar (número entero): ")
    if cantidad.isdigit():
        cantidad = int(cantidad)
        break
    else:
        print("Ingresa un número entero válido.")





registros = []

for i in range(cantidad):
    print(f"\nRegistro de la persona {i + 1}:")
    dosis = int(input("Introduce el número de dosis administradas: "))
    esquema = "✅" if dosis >= 2 else "✖️"
    registros.append({"persona": i + 1, "dosis": dosis, "esquema": esquema})



print("\nResumen de esquemas de vacunación:")
for registro in registros:
    print(f"Persona {registro['persona']} - Dosis: {registro['dosis']} - Esquema: {registro['esquema']}")



while True:
    opcion = input("¿Quieres realizar otro registro? (sí/no): ").strip().lower()
    if opcion == "no":
        print("¡Gracias por utilizar el programa! ¡Adiós!")
        break
    elif opcion == "sí":
        # Aquí puedes reiniciar el proceso si lo necesitas
        pass
    else:
        print("Opción no válida. Inténtalo nuevamente.")



#1
"""
Se desea contriur un programa en python que permita calcular el area de varios triangulos
para esto, se le solicitara indicar cuantos triangulos desea procesar
por cada triangulo, se debera ingresar la base y la altura, amnos valores positivos y reales
la formula: area = base x altura entre 2
si el alumno ingresa un valor incorrecto debe mostrar un mensaje de error
"""










#2
"""
Se desea contriur un programa en python que permita gestionar un sistema simple de venta de entradas para el cine
por medio de un menu de opciones el cual d un stock de entradas previamente cargadas
(el programa debe empezar con 70 entradas), debe realizar distitas accciones


1. dar la bienvenida

MENU
2. ver disponibilidad de sillas
3. ofrecxer la venta de la entrada
4. consultar el numero de entradas a comprar
5. salir


"""

entradas_dispo = 70
opcion = -1

while opcion != 5:
    print("\nMENÚ PRINCIPAL")
    print("1. Ver disponibilidad de sillas")
    print("2. Comprar una entrada")
    print("3. Consultar el número de entradas a comprar")
    print("4. Mostrar disponibilidad actual")
    print("5. Salir")

    try:
        opcion = int(input("Escoge una opción: "))
    except ValueError:
        print("Debes ingresar una opción válida.")
        continue

    if opcion == 1:
        print(f"\nDisponibilidad de entradas: {entradas_dispo} sillas.")
    elif opcion == 2:
        if entradas_dispo > 0:
            entradas_dispo -= 1
            print("Entrada comprada con éxito. ¡Disfruta tu experiencia en el cine!")
        else:
            print("¡Lo sentimos! No hay entradas disponibles.")
    elif opcion == 3:
        consulta = int(input("¿Cuántas entradas deseas comprar?: "))
        if consulta <= entradas_dispo:
            entradas_dispo -= consulta
            print(f"Has comprado {consulta} entradas. Disfruta tu película.")
        else:
            print(f"Lo sentimos, solo quedan {entradas_dispo} entradas disponibles.")
    elif opcion == 4:
        print(f"\nActualmente hay {entradas_dispo} entradas disponibles.")
    elif opcion == 5:
        print("\nGracias por usar el sistema. ¡Adiós!")
    else:
        print("\nOpción no válida, intenta nuevamente.")
