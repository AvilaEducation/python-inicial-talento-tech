listado_productos = [
    {"id":1,"nombre": "pc", "stock": 5},
    {
        "id":2,
        "nombre": "reloj",
        "stock": 7
    }
]

id_usuario = int( input("Ingrese el id para modificar: "))
hubo_cambios = False

for producto in listado_productos:
    if producto["id"] == id_usuario:
        nuevo_stock = int(input("Ingrese el nuevo stock: "))
        producto["stock"] = nuevo_stock
        print(producto)
        hubo_cambios = True

if not hubo_cambios:
    print("El producto no fue encontrado")

print(listado_productos)