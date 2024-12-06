from rich.console import Console
from rich.table import Table

# Crear una instancia de Console
console = Console()

# Imprimir texto con formato (negrita, colores, etc.)
console.print("¡Hola, esto es un ejemplo de rich!", style="bold red")

# Crear una tabla simple
tabla = Table(title="Ejemplo de Tabla con Rich")

# Agregar columnas a la tabla
tabla.add_column("ID", justify="right", style="cyan", no_wrap=True)
tabla.add_column("Nombre", style="magenta")
tabla.add_column("Edad", justify="right", style="green")

# Agregar filas a la tabla
tabla.add_row("1", "Juan", "28")
tabla.add_row("2", "María", "34")
tabla.add_row("3", "Pedro", "22")

# Mostrar la tabla
console.print(tabla)
