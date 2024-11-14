peliculas = [
    {
        "nombre": "...",
        "genero": "...",
        "fecha_lanzamiento": 2010,
        "taquilla": 35000,
        "valoracion": 4.2,
        "en_cartelera": False
    }
]

opcion = "in"

while opcion != "0":
    # print opciones
    print("""1 - cargar datos # 2 - mostrar datos # 0 - salir""")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        # CARGA DE DATOS
        print("cargando datos...")
        nombre = input("Ingrese el nombre del producto: ")
        fecha_lanzamiento = int(input("Ingrese el año de lanzamiento: "))
        genero = input("Ingrese el genero: ")

        # aca se pueden hacer validaciones

        nueva_pelicula = {
            "nombre": nombre,
            "genero": genero,
            "fecha_lanzamiento": fecha_lanzamiento,
            "valoracion": 0,
            "taquilla": 0,
            "en_cartelera": True
        }
        peliculas.append(nueva_pelicula)

    elif opcion == "2":
        print("🟦"*30)
        for pelicula in peliculas:
            print(f"Titulo: {pelicula["nombre"]}")
            print(f"Genero: {pelicula["genero"]}")
            print(f"la pelicula fue lanzada en el año {pelicula["fecha_lanzamiento"]}, recaudando {pelicula["taquilla"]}$")
            print(f"la misma fue valorada con una puntuacion de {pelicula["valoracion"]} por la critica")
            if pelicula["en_cartelera"]:
                print("Actualmente se encuentra en cartelera")

            print("🟦"*30)
