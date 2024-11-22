listado_productos = [
    {"id":1,"nombre": "pc gamer ultra hd", "stock": 5},
    {
        "id":2,
        "nombre": "reloj smartwatch",
        "stock": 7
    },
    {"id":3,"nombre": "smart tv", "stock": 5},
]

nombre_a_buscar = input("Ingrese el nombre a buscar: ")
encontramos_producto = False

for producto in listado_productos:
    # nos fijamos si el "nombre_a_buscar" pertence al texto del nombre del producto
    if nombre_a_buscar in producto["nombre"]:
        print(producto)
        encontramos_producto = True

if not encontramos_producto:
    print("El producto no fue encontrado")

# buscar por stock, en un rango de valores