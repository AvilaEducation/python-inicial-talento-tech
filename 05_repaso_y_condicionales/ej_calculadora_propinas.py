# Escribe un programa en Python que calcule la propina que se debe dejar en un restaurante. 

# El script debe solicitar al usuario el monto total de la cuenta y el porcentaje de propina que desea dejar.
 
# Utilizando operadores aritméticos, calcula la cantidad de propina y el total a pagar (incluyendo la propina). 
# Finalmente, muestra los resultados en la pantalla.

# variables // notas para entender el problema

# datos de entrada
precio_comida: float
porcentaje_propina: int

# datos a calcular
propina: float

# asignacion de variables
precio_comida = float( input("Ingrese el monto total a pagar: ") )
porcentaje_propina = int( input("Ingrese el pocentaje de propina, un numero entre 0 y 100: ") )

# programa
# regla de 3 o calculo de porcentaje
# precio_comida -> 100%
# propina(tenemos que calcular) -> porcentaje_propina(20%)

propina = (precio_comida * porcentaje_propina) / 100

monto_total = precio_comida + propina

print("la comida salio: ", precio_comida)
print("la propina es: ", propina)

print("💲 el saldo a pagar es: ", monto_total)