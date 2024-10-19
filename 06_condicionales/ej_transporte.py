# Una persona trabaja de miércoles a domingo, los días de semana el colectivo tarda mucho por el tráfico 
# y en los fines de semana los trenes tardan mucho porque hay menos unidades. Dado un día, 
# indicar si es mejor tomar el tren o tomar el colectivo para viajar.

print("Eliga un numero que represente el dia")
print("1 - miercoles")
print("2 - jueves")

dia = input("Ingrese un dia")

# podemos tomar el tren si es: 1, 2 o 3
puedo_usar_tren = dia == "1" or dia == "2" or dia == "3"
if puedo_usar_tren:
    print("es mejor ir en tren")

# podemos tomar el colectivo si es: 4 o 5
elif dia == "4" or dia == "5":
    print("es mejor ir en colectivo")
else:
    print("hoy podes descanzar o usar el transporte que prefieras")


