producto = {
    "nombre": "reloj",
    "stock": 7
}

# el usuario eligio editar el stock
print(f"Stock actual: {producto['stock']}")
nuevo_stock = int( input("Ingrese el nuevo stock: ") )

producto["stock"] = nuevo_stock

# mostrar diccinario
print(producto)