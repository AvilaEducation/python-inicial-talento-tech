# Se requiere calcular el promedio de 400 numeros. El usuario debe ingresar cuatro numeros y luego mostrar el promedio. 

# promedio = (n1 + n2 + n3 + n4) / 4

# carga de datos
numero = int( input("Ingrese un numero: ") )
suma = 0
cantidad_numeros_sumados = 0

print("SUMA: ", suma)
# se puede parar el bucle usando palabras?
while numero != -1:
    # forma uno de acumular valores
    suma = numero + suma

    # forma dos de acumular valores
    # promedio += numero

    # forma uno de sumar de a uno
    cantidad_numeros_sumados = cantidad_numeros_sumados + 1

    # forma dos de sumar de a uno
    # cantidad_numeros_sumados += 1

    print("SUMA: ", suma)
    numero = int( input("Ingrese un numero: ") )

# promedio = (numero_1 + numero_2 + numero_3 + numero_4) / 4

print("El promedio es: ", suma / cantidad_numeros_sumados)