"""
 Debemos realizar un programa, que indique un rango numerico insertando un valor para 
 generar otro aleatorio dentro de ese mismo rango continuando con la misma suma el programa debe calcular el 
 promedio
 
 ejercicio por encima
 
 dato:
 ocupar flag  en el examen 
 ocupar librelia import ramdom
 
  n1 = ? Ej: 100
  100 tope, aleatorio genere otro numero
  n2 = ? Ej: 80 a este sacar un %
  pedir el porcentaje: Ej: 10%
 el 10% de 80 = 8
 dame un numero otra vez pero con la condicion si decide sumar o restar
 Ej si es un 20 + 8 = 28 y lo mismo con restar
 """


# pedir numero 1
Num_1 = int(input("Dame un número aleatorio: "))


#recalcar que este sera el tope
print()
print("Este será el tope máximo:", Num_1)
print()


#pedir numero 2
Num_2 = int(input("Dame otro número aleatorio entre el tope: "))


#proceso para que el numero 2 no pase el tope del numero 1
while Num_2 > Num_1:
    print()
    print(f"El número no puede ser mayor que {Num_1}. Inténtalo de nuevo:")
    print()
    Num_2 = int(input("Dame otro número aleatorio entre el tope: "))


#pedir numero en %
NumPorcent = int(input("Dame otro número aleatorio el cual será en %: "))


#proceso para sacar el %
Resultado = int((Num_2 * NumPorcent) / 100)

print(f"El {NumPorcent}% de {Num_2} es: {Resultado}")


#pedir el ultimo numero para sumarlo o restarlo
Num_3 = int(input("Dame el último número aleatorio: "))


#proceso para sumar o restar
operacion = input("Escribe 'sumar' para sumar o 'restar' para restar: ")

if operacion == 'sumar':
    resultado_final = Resultado + Num_3
    print(f"El resultado de sumar {Resultado} y {Num_3} es: {resultado_final}")
elif operacion == 'restar':
    resultado_final = Resultado - Num_3
    print(f"El resultado de restar {Resultado} y {Num_3} es: {resultado_final}")
else:
    print("Opción no válida. Por favor, intenta nuevamente.")

    