# traemos el modulo de sqlite
import sqlite3

# abrimos la conexion con la base de datos
conexion = sqlite3.connect("productos_db.db")

# creamos el <cursor> para interactuar con la base de datos
cursor = conexion.cursor()

# con esto creamso una tabla en la base de datos
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    stock INTEGER
)
""")

# esto solo usamos la primera vez, despues lo podemos borrar porque la data ya existe
cursor.execute("""
INSERT INTO productos (nombre, stock) VALUES
    ('HyperX Gaming Mouse', 50),
    ('Razer Kraken Headset', 30),
    ('Corsair K95 RGB Keyboard', 20),
    ('Logitech G Pro Wireless', 10),
    ('ASUS TUF Gaming Monitor', 60),
    ('MSI GeForce RTX 3080', 45),
    ('Samsung 970 EVO SSD', 25),
    ('Seagate 2TB HDD', 15),
    ('SteelSeries Arctis 7', 35),
    ('Gigabyte AORUS Z390 Motherboard', 75),
    ('Intel Core i9-12900K Processor', 100),
    ('AMD Ryzen 9 7900X', 85),
    ('Dell XPS 13 Laptop', 40),
    ('Lenovo Legion 5 Pro', 55),
    ('Apple MacBook Pro M1', 90),
    ('Samsung Odyssey G7 Curved Monitor', 80),
    ('Corsair Vengeance LPX RAM', 65),
    ('Kingston HyperX Cloud II', 70),
    ('TP-Link Archer AX6000 Router', 95),
    ('Cooler Master Hyper 212 Cooler', 50);
""")

# guardamos los cambios hechos
conexion.commit()
# cerramos la conexion del cursor
cursor.close()

# cerramos la conexion con la base de datos
conexion.close()