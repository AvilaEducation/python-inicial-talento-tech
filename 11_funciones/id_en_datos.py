# id = indentificacion
# usamos el id para principalmente borrar o editar cosas

proximo_id = 1

productos = [
    {"nombre": "pc", "stock": 5},
    {"nombre": "reloj", "stock": 7},
    {"nombre": "celu", "stock": 5},
    {"nombre": "celu", "stock": 5},
    {"nombre": "celu", "stock": 5},
    {"nombre": "celu", "stock": 5},
    {"nombre": "celu", "stock": 5},
]

# agregar producto
producto_nuevo = {"comida_id": proximo_id, "nombre": "celu", "stock": 5, "correo": ""}

productos.append(producto_nuevo)

proximo_id = proximo_id + 1
