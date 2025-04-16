# Bienvenida a la página
print("¡Bienvenido a nuestra página web! Por favor, inicia sesión o regístrate.")

def registrar_usuario():
    print("--- Registro ---")
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))

    if edad < 18:
        print("Lo sentimos, debes ser mayor de edad para registrarte. Adiós.")
        return None

    usuario = input("Crea un nombre de usuario único: ")
    clave = input("Crea tu clave: ")
    print(f"¡Registro exitoso, {nombre}! Ahora puedes iniciar sesión.")
    return {"usuario": usuario, "clave": clave}

def login(credenciales):
    print("--- Login ---")
    usuario = input("Introduce tu usuario: ")
    clave = input("Introduce tu clave: ")

    if usuario == credenciales["usuario"] and clave == credenciales["clave"]:
        print("¡Bienvenido a PlayBoy!")
    else:
        print("Usuario o clave incorrectos. Inténtalo de nuevo.")

# Programa principal
credenciales = None
while True:
    print("\n1. Login\n2. Registro\n3. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        if credenciales:
            login(credenciales)
        else:
            print("Primero necesitas registrarte.")
    elif opcion == 2:
        credenciales = registrar_usuario()
    elif opcion == 3:
        print("Gracias por visitar nuestra página. Adiós.")
        break
    else:
        print("Opción no válida. Por favor, elige de nuevo.")