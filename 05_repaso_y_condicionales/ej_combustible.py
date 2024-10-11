# Realizar una aplicación en Python que;
# # A partir de la cantidad de litros de combustible que consume un coche por cada 100 km de recorrido,
#  el costo de cada litro de combustible y la longitud del viaje realizado (en kilómetros), 
# muestra un detalle de los litros consumidos y el dinero gastado.

# variables // notas del problema
# datos de entrada
consumo_combustible_100km: float
costo_litro_combustible: float
distancia_viaje: float

# variables a calcular
litros_usados: float
dinero_gastado: float

# asignar variables
consumo_combustible_100km = float( input("Ingrese el consumo de combustible cada 100km: ") )
costo_litro_combustible = float( input("Ingrese el precio de cada litro de combustible: ") )
distancia_viaje = float( input("Ingrese cuantos kilometros viajo: ") )

# regla de 3
# consumo_combustible_100km L -> 100 km
# x                         L -> distancia_viaje km

litros_usados = (consumo_combustible_100km * distancia_viaje) / 100

print("litros usados: ", litros_usados)

# regla de 3
# 1L            -> costo_litro_combustible
# litros_usados -> x

dinero_gastado = (litros_usados * costo_litro_combustible) / 1

print("dinero gastado en el viaje: ", dinero_gastado)