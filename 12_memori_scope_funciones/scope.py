numeros = []
nombre = "python"

def demo():
    # intenta utilizar la variable que ya existe fuera de la funcion
    global nombre
    nombre = "java"
    nombre_curso = "23784"
    print(numeros)
    print(nombre)
    numeros.append(1)
   

def test2():
    nombre_curso = "23784"
    print(nombre)

print(nombre)
numeros.append(1)
demo()
print(nombre)
print(numeros)
test2()