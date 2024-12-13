# traemos el modulo de sqlite
import sqlite3

# FUNCIONES
def mostrar_producto(producto: dict):
    print(f"nombre: {producto["nombre"]} - stock: {producto["stock"]}")

# version con base de datos
def cargar_nuevo_producto():
    # CARGA DE DATOS
    print("cargando datos...")
    nombre_producto = input("Ingrese el nombre del producto: ")
    stock_producto = int( input("Ingrese el stock: ") )
    
    # guardarlo en la base de datos
    cursor = conexion.cursor()
    
    cursor.execute("""
        INSERT INTO productos (nombre, stock) values (?, ?)                   
    """, (nombre_producto, stock_producto))
    
    conexion.commit()
    cursor.close()

# version con base de datos
def mostrar_productos():
    # MOSTRAR DATOS
    print("mostrando datos")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, stock FROM productos")
    productos_db = cursor.fetchall()
    
    for producto in productos_db:
        print(f"id: {producto[0]} - nombre: {producto[1]} - stock: {producto[2]}")
    
    # traten de dejarlo al final de la funcion
    cursor.close()

def borrar_producto():
    id_usuario = int( input("Ingrese el id para borrar: "))
    # tarea completarlo con base de datos

def editar_producto():
    id_usuario = int( input("Ingrese el id para modificar: "))
    
    cursor = conexion.cursor()
    
    # validamos que el producto existe
    # la coma es solo para indicar que es una tupla
    cursor.execute("SELECT * FROM productos where id=?", (id_usuario,))
    
    productos_encontrados = cursor.fetchall()
    
    if len(productos_encontrados) == 0:
        print("El producto no fue encontrado")
        return
    
    stock = int( input("Ingrese el nuevo stock") )
    # actualiamos el stock sabiendo que el producto existe
    cursor.execute("UPDATE productos SET stock=? where id=?", (stock, id_usuario))
    conexion.commit()
    cursor.close()


def reporte_bajo_stock():
    cantidad_minima = int( input("Ingrese el numero desde el cual considera bajo stock: ") )
    
    # MOSTRAR DATOS
    print("mostrando datos")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, stock FROM productos where stock < ?", (cantidad_minima,))
    
    # cursor.execute("SELECT id, nombre, stock FROM productos where stock_actual < stock_minimo")
    productos_db = cursor.fetchall()
    
    # mostrar la data que obtuvimos
    if len(productos_db) == 0:
        print("No hay ningun producto de bajo stock")
        return
    
    for producto in productos_db:
        print(f"id: {producto[0]} - nombre: {producto[1]} - stock: {producto[2]}")
    
    # traten de dejarlo al final de la funcion
    cursor.close()
    
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

# INICIO DE APLICACION
# abrimos la conexion con la base de datos
conexion = sqlite3.connect("productos_db.db")

listado_productos = []
opcion = "in"

# MENU PRINCIPAL
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
        # cerramos la conexion con la base de datos
        conexion.close()
    else:
        print("Opcion incorrecta, intente de nuevo")
