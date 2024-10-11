# Crea un programa que solicite al usuario dos números enteros.
# Realiza las siguientes operaciones: suma, resta, multiplicación, y módulo. 
# Muestra el resultado de cada operación en un formato claro y amigable. 
# Asegúrate de incluir mensajes personalizados que expliquen cada resultado, 
# por ejemplo: "La suma de tus números es: X".

# variables // esto son notas que se hacen al pensar el problema
numero_1: int
numero_2: int

# asignacion de variables
print("Te damos la bienvenida a la app calculadura")
numero_1 = int( input("Ingrese un numero: ") )
numero_2 = int( input("Ingrese un numero que no sea 0: ") )

# programa
suma = numero_1 + numero_2

resta = numero_1 - numero_2

multiplicacion = numero_1 * numero_2

modulo = numero_1 % numero_2 # resto de la division entera entre los numeros

print("Se ingresaron los numeros: ", numero_1, numero_2)

print("El resultado de sumar los dos valores que ingresaste es: ", suma)

print("Restando lo numeros obtengo: ", resta)

print("multiplicacion: ", multiplicacion)
print("modulo: ", modulo)

print("🤖 Gracias por usar la app 🤖")
