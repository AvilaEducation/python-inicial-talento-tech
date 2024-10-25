contador = 1 
# validacion de datos para el bucle, que pasa si cargo -1?
cantidad_repeticiones = int(input("Ingrese cuantos numeros desea cargar: "))
suma = 0

while contador <= cantidad_repeticiones:
    # sumamos
    suma = suma + int(input("Ingrese un numero: "))

    # nos acercamos a la meta
    contador = contador + 1

print("SUMA: ", suma)