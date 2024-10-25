# puede usar cualquier valor que sea distinto a la compracion del while
opcion_compra = "INICIO_WHILE" # esto es solo para poder ingresar al bucle

# 1 <= opcion_compra <= 3 # a checkear
# 1 <= opcion_compra and opcion_compra <= 3

while opcion_compra != "0":
    print("#"*30) # si se usa el operador de multiplicacion con un string, el string se repite
    print()
    print("#"*30)
    print(" Productos a comprar:")
    # pueden usar esto para armar las opciones del menu
    # usando la triple comilla de apertura y cierre pueden agregar cualquier salto de linea
    print("""
        1 - pizza
        2 - empanada
        3 - milanesa
        0 - salir
    """)

    opcion_compra = input("Ingrese una opcion para comprar: ")

    # aca ingrese al bucle (la app)
    if opcion_compra == "1":
        print("Compraste pizza")
    elif opcion_compra == "2":
        print("compraste empanada")
    elif opcion_compra == "3":
        print("compraste milanesa")
    else:
        print("Opcion incorrecta, intente de nuevo")
    

