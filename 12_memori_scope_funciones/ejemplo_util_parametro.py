productos = [
    {"nombre": "pc", "stock": 5},
    {
        "nombre": "reloj",
        "stock": 7
    },
    {"nombre": "celu", "stock": 5}
]

def mostrar_producto(producto: dict):
    print(f"nombre: {producto["nombre"]} - stock: {producto["stock"]}")

def mostrar_datos():
    print("Mostrar datos: ")
    for producto in productos:
        mostrar_producto(producto)

mostrar_datos()