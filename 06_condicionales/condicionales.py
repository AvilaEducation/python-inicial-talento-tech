# boolean, valores de true o false

nota = float( input("Ingrese una nota entre 1 y 10: ") )


# 2 * 2 + 5 = 9
# 2 * (2 + 5) = 14
no_es_nota_valida = nota < 1 or nota > 10

if no_es_nota_valida:
    print("La nota no es correcta")
    print("La nota no es correcta")
    print("La nota no es correcta")
    print("La nota no es correcta")
    print("La nota no es correcta")


if nota >= 1 and nota < 7:
    print("Lo intentaste, pero falta camino por recorrer :(")

if nota >= 7:
    print("Aprobado :)")

if nota == 10:
    print("Perfecto! sacaste la nota maxima 🎉🎉🎉")