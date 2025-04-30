"""
Desarrolle un programa que permita calcular el subcidio mensual del trasporte estudiantil para los estudiantes de duoc en el año 2025
considera su puntaje de admision, y luego su lugar de residencia, condiciones acamemicas, puntajes de ademision en duoc , rango de 450 y 800 puntos,
condiciones geograficas, distancia del hogar a las instalaciones de duoc san joaquin
beneficios, a continuacion se dictara una tabla,
beneficio :
puntaje de admision:       distancia al duoc           subcidio  
> 700                     mayor de 20 km            180.000  
> 700                     entre 10 y 20 km          130.000
600 =< 700                mayor de 20 km            100.000
600 =< 700                entre 10 a 20             80.000
bono adicional si el estudiante vive en una zona rural, debe indicar si o no
en el caso de ser positivo recibira un abono de 40.000 adicionalmente, si su puntaje es mayor a 750 recibira un bono de 20.000
requisitos del programa solciitar el puntaje, la distancia km, y si su residencia es rural o no, calcular el subcidio base segun la condicion,
verificar si corresponde alguno de los bonos, mostrar el subsidio en pantalla y el total,

"""

print("Bienvenido al sistema de cálculo del subsidio de transporte estudiantil para Duoc 2025")


# Solicitar datos al usuario
puntaje_admision = int(input("Introduce tu puntaje de admisión (entre 450 y 800): "))
distancia = float(input("Introduce la distancia desde tu hogar al Duoc San Joaquín (en km): "))
zona_rural = input("¿Vives en una zona rural? (sí/no): ").strip().lower()

# Validar rango del puntaje
if puntaje_admision < 450 or puntaje_admision > 800:
    print("Puntaje fuera del rango válido. Intenta nuevamente.")
    exit()

# Calcular el subsidio base
subsidio = 0
if puntaje_admision > 700:
    if distancia > 20:
        subsidio = 180000
    elif 10 <= distancia <= 20:
        subsidio = 130000
elif 600 <= puntaje_admision <= 700:
    if distancia > 20:
        subsidio = 100000
    elif 10 <= distancia <= 20:
        subsidio = 80000

# Evaluar bonos adicionales
bono_adicional = 0
if zona_rural == "sí":
    bono_adicional += 40000
if puntaje_admision > 750:
    bono_adicional += 20000

# Calcular total
subsidio_total = subsidio + bono_adicional

# Mostrar resultados
print("\nResultados del cálculo:")
if subsidio == 0:
    print("Lo sentimos, no calificas para el subsidio base.")
else:
    print(f"Subsidio base: ${subsidio}")
    print(f"Bonos adicionales: ${bono_adicional}")
    print(f"Subsidio total: ${subsidio_total}")