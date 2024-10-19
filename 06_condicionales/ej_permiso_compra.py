# Ejercicio - permiso para comprar
# Escribir un programa que pida al usuario su edad y determine si puede comprar bebidas alcohólicas.
# tip: usar la funcion int()

edad = int( input("Ingrese su edad: ") )
dinero = 0

# la persona es mayor de edad?
# if edad >= 18:
#     print("Tienes permiso para comprar bebibas alcoholicas")

# if edad < 18 or dinero < 2000:
#     print("No podes compras bebidas alcoholicas")

if edad >= 18 and dinero > 2000:
    print("Tienes permiso para comprar bebibas alcoholicas")
else:
    print("No podes compras bebidas alcoholicas")