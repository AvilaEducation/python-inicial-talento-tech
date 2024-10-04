# el usuario ingresa 3 numeros, calculamos el promedio y lo mostramos por la consola

# definir variables
# esto es opcional, y mas como una ayuda memoria para entender mejor el problema
numero_1: int
numero_2: int
numero_3: int
promedio: float

# asignar valores
# casi siempre usamos la conversion de tipos de datos junto con el input
numero_1 = int( input("Ingrese un numero: ") )
numero_2 = int( input("Ingrese un numero: ") )
numero_3 = int( input("Ingrese un numero: ") )

# programa
promedio = (numero_1 + numero_2 + numero_3) / 3

# salida
print("El promedio de los tres numeros es: ")
print(promedio)