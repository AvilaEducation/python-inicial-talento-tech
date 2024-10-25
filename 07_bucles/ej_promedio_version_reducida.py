# en este ejemplo el promedio se calcula siempre entonces
# al terminar el bucle ya tengo el promedio calculado en la variable numero

# aca ingreso los primeros dos numeros para poder realizar el calculo del promedio
calculo = int( input("Ingrese un numero: ") )
numero = int( input("Ingrese un numero: ") )

while numero >= 0:
    calculo = calculo + numero
    # calculo el promedio hasta ahora
    calculo = calculo / 2

    numero = int( input("Ingrese un numero: ") )


print("El promedio es: ", calculo)