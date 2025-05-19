# ----------------------------------------------
# Parte 1: ¿Qué es un número primo?
# ----------------------------------------------

"""
Un número primo es como un superhéroe: ¡solo le gusta jugar con el 1 y consigo mismo! 
Por ejemplo, el número 2 solo puede ser dividido por 1 y por 2. 
Pero el 4 no es primo, porque 4 también puede ser dividido por 2.

Pasos para hacerlo en Python:
1. Le vamos a preguntar al niño cuántos números quiere revisar.
2. Luego le pedimos que nos diga uno por uno los números. 
3. Con cada número, revisamos si tiene más amigos (divisores) aparte del 1 y él mismo.
4. Al final, decimos cuántos números fueron súper héroes (primos) y cuántos no.

Ejemplo:
Mamá, quiero revisar 3 números.
Primer número: 5 → Es primo 
Segundo número: 4 → No es primo 
Tercer número: 2 → Es primo 

Resultado:
→ Se ingresaron 2 números primos.
→ Se ingresó 1 número no primo.
"""

print("Mama, revisa estos 3 numeros")

numero = [5,6,7,]

#contadores

N_primos = 0
N_no_primos = 0

def Es_Primo(n):
    if n <= 1:
        return False
    for i in range (2, int(n / 2)+ 1):
        if n % i == 0:
            return False
    return True

#Recorrido
for i, numero in enumerate(numero):
    print(f"{i+1} numero: {numero}", end="->")
    if Es_Primo(numero):
        print("Es primo")
    N_primos +=1
else:
    print("No es primo")
    N_no_primos +=1 

print(f"\nResultado")                      
print(f"→ Se ingresaron {N_primos} números primos.")
print(f"→ Se ingresó {N_no_primos} número{"s" if N_no_primos > 1 else ""} no primo.")
