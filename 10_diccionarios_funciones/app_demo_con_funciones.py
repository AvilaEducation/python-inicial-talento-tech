# FUNCIONES
def cargar_nuevo_producto():
    # CARGA DE DATOS
    print("cargando datos...")
    nombre = input("Ingrese el nombre del producto: ")
    stock = int( input("Ingrese el stock: ") )
    
    # aca se pueden hacer validaciones
    # VERSION VIEJA
    # nuevo_producto = [nombre, stock]
    # VERSION NUEVA
    nuevo_producto = {
        "name": nombre,
        "stock": stock
    }
    productos.append(nuevo_producto)

def mostrar_productos():
    # MOSTRAR DATOS
    print("mostrando datos")
    for producto in productos:
        # FORMA VIEJA - para listas
        # print(f"Producto: {producto[0]} - Stock: {producto[1]}")
        # FORMA NUEVA - para diccionarios
        print(f"Producto: {producto["nombre"]} - Stock: {producto["stock"]}")

def editar_stock_producto():
    print("Editar dato")

# VERSION VIEJA
# productos = [
#     ["pc", 5, 5, 5, 5],
#     ["reloj", 7],
#     ["celu", 5]
# ]

# VERSION NUEVA
# primero hay que definir todos los nombres de los atributos que usaremos
# en todos los diccionarios
# para este caso serian: "nombre" y "stock"
productos = [
    {"nombre": "pc", "stock": 5},
    {
        "nombre": "reloj",
        "stock": 7
    },
    {"nombre": "celu", "stock": 5}
]

# MENU PRINCIPAL
opcion = "in"

while opcion != "0":
    # print opciones
    print("""
    menu de ejemplo:
          1 - cargar datos
          2 - mostrar datos
          3 - editar dato
          0 - salir
    """)
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        cargar_nuevo_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        editar_stock_producto()
    elif opcion == "0":
        print("Gracias por usar la app")
    else:
        print("Opcion incorrecta, intente de nuevo")
