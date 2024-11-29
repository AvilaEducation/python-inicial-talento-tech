nombre_curso = "python"
nombre_lenguaje = nombre_curso

print(nombre_curso)
print(nombre_lenguaje)

nombre_lenguaje = "aksjhd"

print(nombre_curso)
print(nombre_lenguaje)
print(id(nombre_curso))
print(id(nombre_lenguaje))
numeros = [1, 2]

numeros_copia = numeros

print(numeros)
print(numeros_copia)

numeros.append(20)

numeros_copia.append(123)

print(numeros)
print(numeros_copia)

print(id(numeros))
print(id(numeros_copia))