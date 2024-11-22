listado_productos = [
    {"id":1,"nombre": "pc", "stock": 5},
    {
        "id":2,
        "nombre": "reloj",
        "stock": 7
    }
]

id_usuario = int( input("Ingrese el id para borrar: "))

for producto in listado_productos:
    if producto["id"] == id_usuario:
        print(producto)
        borrar= input("Quiere confirmar el borrado del producto? S/N: ")
        if borrar.lower() == "s":
            listado_productos.remove(producto)
            print("borrado con exito 🗑")
        break # con esto sale del bucle y el "else" que tambien pertenece al bucle no se ejecuta
else:
    print("El producto no fue encontrado")
    

print(listado_productos)