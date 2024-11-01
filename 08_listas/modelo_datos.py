# necesitamos describir un poco mejor cada elemento
# POR AHORA USAMOS LISTAS, DESPUES USAREMOS DICCIONARIOS
# NOTA: si vienen bien, pueden investigar y usar diccionarios
# FULL OPCIONAL, DEMASIADO OPCIONAL: pueden usar clases si saben lo que es (no se ve en el curso)

producto = ["pc", 3]

producto_2 = ["celu", 5]

producto_3 = ["reloj", 1]

productos = [producto, producto_2, producto_3]

# NUEVO PRODUCTO
nombre_producto = input("Ingrese el nombre del producto: ")
stock_producto = int( input("Ingrese el stock del producto: "))

nuevo_producto = [nombre_producto, stock_producto]

productos.append(nuevo_producto)