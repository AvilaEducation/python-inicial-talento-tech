# parametros de las funciones
def mensaje(mensaje):
    print(mensaje)

# argumentos de las funciones
# mensaje("hola mundo")

# mensaje_para_funcion = "muy buenas gente de talent tech"

# mensaje(mensaje_para_funcion)

# TODO: si quieren agregar documentacion a las funciones
# buscar <docstrings>
def agregar_y_mostrar(numeros_funcion: list):
    numeros_funcion.append(20)
    print(numeros_funcion)

numeros = [1, 2, 3]

agregar_y_mostrar(numeros)

print(numeros)

# el uso del return