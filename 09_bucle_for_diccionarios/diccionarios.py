pais1 = {
    "nombre": "Argentina",
    "es_el_mejor_pais": True,
    "cantidad_habitantes": 45000000,
    "continente": "america",
    "cantidad_provincias": 23,
    "capital": "buenos aires",
    "cantidad_mundiales": "⭐⭐⭐"
}

pais2 = {
    "nombre": "Francia",
    "es_el_mejor_pais": True,
    "cantidad_habitantes": 45000000,
    "continente": "america",
    "cantidad_provincias": 23,
    "capital": "buenos aires",
    "cantidad_mundiales": "⭐⭐⭐"
}

paises = [pais1, pais2]

for pais in paises:
    print("#"*50)# separador
    print(pais["nombre"])
    print(f"cantidad de habitantes en el año 2024: {pais["cantidad_habitantes"]}")
    print("#"*50)# separador

