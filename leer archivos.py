with open("datos.txt", "w") as archivo:
    archivo.write("Nombre: Maria\n")
    archivo.write("Edad: 25\n")
    archivo.write("Carrera: Ing\n")
    archivo.write("Promedio: 6\n")

try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileExistsError as error:
    print("Archivo no existe", error)
else:        
    print("Archivo leido")
finally:
    print("Chao")    