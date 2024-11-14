productos = [
    ["pc", 5],
    ["reloj", 7],
    ["celu", 5]
]

# MENU PRINCIPAL
opcion = "in"

while opcion != "0":
    # print opciones
    print("""
    menu de ejemplo:
          1 - cargar datos
          2 - mostrar datos
          0 - salir
    """)
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        # CARGA DE DATOS
        print("cargando datos...")
        nombre = input("Ingrese el nombre del producto: ")
        stock = int( input("Ingrese el stock: ") )
        precio = int( input("Ingrese el precio: ") )
        nuevo_producto = [nombre, stock, precio]
        # aca se pueden hacer validaciones
        productos.append(nuevo_producto)

    elif opcion == "2":
        # MOSTRAR DATOS
        print("mostrando datos")
        for producto in productos:
            print(f"Producto: {producto[0]} - Stock: {producto[1]}")

    elif opcion == "0":
        print("Gracias por usar la app")
    else:
        print("Opcion incorrecta, intente de nuevo")