"""
la gente de certifica nesesita desarrollar un sofwer en python que le colabore para realizar un estudio social
donde se tomara en cuenta las calificaciones de cada uno de los estudiantes aquellos con mejor calificacion obtendran mayor descuento.
los estudiantes igual o mayor a 6 obtendran decuento del 20%
los estudiantes igual o mayor a 5 obtendran un descuento del 15%
los estudiantes igual o mayor a 4 obtendran un 5%
el curso que se encuentra propocionando tiene un valor de $200.000 pesos
se nesesita: dar bienvenida, preguntar calificacion
"""


def bienvenida():
    print("¡Bienvenido al programa de Certifica!")
    print("Basado en tu calificación, recibirás un descuento en el curso de $200,000 pesos.")

# Calculo
def calcular_descuento(calificacion):
    if calificacion >= 6:
        return 0.20
    elif calificacion >= 5:
        return 0.15
    elif calificacion >= 4:
        return 0.05
    else:
        return 0.0

bienvenida()
calificacion = float(input("Introduce tu calificación (1-10): "))

descuento = calcular_descuento(calificacion)
if descuento > 0:
    valor_final = 200000 * (1 - descuento)
    print(f"¡Felicidades! Con tu calificación de {calificacion}, tienes un descuento del {int(descuento*100)}%. El curso te queda en: ${valor_final:.2f} pesos.")
else:
    print(f"Lo sentimos, con tu calificación de {calificacion}, no obtienes descuento.")



