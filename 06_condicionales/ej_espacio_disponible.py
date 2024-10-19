# Google meet solo admite 100 personas por reunión, dado la cantidad de estudiantes en un curso, 
# indicar si es posible tener la clase por meet o se debe buscar otra alternativa.

cantidad_estudiantes = int( input("Ingrese la cantidad de estudiantes: ") )

# cantidad valida de estudiantes
if cantidad_estudiantes >= 1 and cantidad_estudiantes <= 100:
    print("Podemos tener la clase en meet")
 
# se supera la cantidad admitada por meet
elif cantidad_estudiantes > 100: 
    print("hay que buscar alternativas")

# el dato es incorrecto
else:
    print("El dato ingresado es incorrecto")
