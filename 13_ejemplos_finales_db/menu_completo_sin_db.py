# FUNCIONES
def mostrar_producto(producto: dict):
    print(f"nombre: {producto["nombre"]} - stock: {producto["stock"]}")

def borrar_producto():
    id_usuario = int( input("Ingrese el id para borrar: "))

    for producto in listado_productos:
        if producto["id"] == id_usuario:
            mostrar_producto(producto)
            borrar= input("Quiere confirmar el borrado del producto? S/N: ")
            if borrar.lower() == "s":
                listado_productos.remove(producto)
                print("borrado con exito 🗑")
            break # con esto sale del bucle y el "else" que tambien pertenece al bucle no se ejecuta
    else:
        print("El producto no fue encontrado")

def editar_producto():
    id_usuario = int( input("Ingrese el id para modificar: "))
    hubo_cambios = False

    for producto in listado_productos:
        if producto["id"] == id_usuario:
            nuevo_stock = int(input("Ingrese el nuevo stock: "))
            producto["stock"] = nuevo_stock
            mostrar_producto(producto)
            hubo_cambios = True

    if not hubo_cambios:
        print("El producto no fue encontrado")

def buscar_por_nombre():
    nombre_a_buscar = input("Ingrese el nombre a buscar: ")
    encontramos_producto = False

    for producto in listado_productos:
        # nos fijamos si el "nombre_a_buscar" pertence al texto del nombre del producto
        if nombre_a_buscar in producto["nombre"]:
            mostrar_producto(producto)
            encontramos_producto = True

    if not encontramos_producto:
        print("El producto no fue encontrado")

def cargar_nuevo_producto():
    global id_siguiente
    # CARGA DE DATOS
    print("cargando datos...")
    nombre = input("Ingrese el nombre del producto: ")
    stock = int( input("Ingrese el stock: ") )
    
    nuevo_producto = {
        "id": id_siguiente,
        "nombre": nombre,
        "stock": stock
    }
    listado_productos.append(nuevo_producto)
    id_siguiente += 1

def mostrar_productos():
    # MOSTRAR DATOS
    print("mostrando datos")
    for producto in listado_productos:
        mostrar_producto(producto)

def reporte_bajo_stock():
    cantidad_minima = int( input("Ingrese el numero desde el cual considera bajo stock: ") )
    productos_bajo_stock = []
    
    # filtrar/calcular la data de interes
    for producto in listado_productos:
        if producto["stock"] <= cantidad_minima:
            productos_bajo_stock.append(producto)
    
    # mostrar la data que obtuvimos
    if len(productos_bajo_stock) == 0:
        print("No hay ningun producto de bajo stock")
    else:
        print("PRODUCTOS CON BAJO STOCK")
        for producto in productos_bajo_stock:
            mostrar_producto(producto)

id_siguiente = 4
listado_productos = [
    {"id": 1, "nombre": "pc", "stock": 5},
    {
        "id": 2,
        "nombre": "reloj",
        "stock_actual": 7
    },
    {"id": 3, "nombre": "celu", "stock": 5}
]

# MENU PRINCIPAL
opcion = "in"

while opcion != "0":
    # print opciones
    print("""
    menu de ejemplo:
          1 - cargar datos
          2 - mostrar datos
          3 - buscar por nombre
          4 - editar producto
          5 - borrar producto
          6 - reporte bajo stock
          0 - salir
    """)
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        cargar_nuevo_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        buscar_por_nombre()
    elif opcion == "4":
        editar_producto()
    elif opcion == "5":
        borrar_producto()
    elif opcion == "6":
        reporte_bajo_stock()
    elif opcion == "0":
        print("Gracias por usar la app")
    else:
        print("Opcion incorrecta, intente de nuevo")
