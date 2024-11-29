productos = []
siguiente_id = 1

def cargar_nuevo_producto():
    global siguiente_id
    # CARGA DE DATOS
    print("cargando datos...")
    nombre = input("Ingrese el nombre del producto: ")
    stock = int( input("Ingrese el stock: ") )
    
    # aca se pueden hacer validaciones
    # VERSION VIEJA
    # nuevo_producto = [nombre, stock]
    # VERSION NUEVA
    nuevo_producto = {
        "id": siguiente_id,
        "name": nombre,
        "stock": stock
    }
    productos.append(nuevo_producto)
    siguiente_id += 1

cargar_nuevo_producto()
siguiente_id += 1

cargar_nuevo_producto()
siguiente_id += 1