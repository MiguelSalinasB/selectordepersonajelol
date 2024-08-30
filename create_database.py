import sqlite3
import json

# Nombre de la base de datos
db_name = 'league_of_legends.db'

# Leer el archivo JSON
with open('champions.json', 'r') as file:
    champions_data = json.load(file)

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Crear la tabla 'champions'
cursor.execute('''
CREATE TABLE IF NOT EXISTS champions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    image TEXT NOT NULL
)
''')

# Crear la tabla 'matches'
cursor.execute('''
CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    champion_id INTEGER NOT NULL,
    result TEXT NOT NULL,
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (champion_id) REFERENCES champions (id)
)
''')

# Insertar los campeones en la base de datos
for champion in champions_data:
    cursor.execute('''
    INSERT INTO champions (name, image)
    VALUES (?, ?)
    ''', (champion['name'], champion['image']))

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos creada y campeones insertados exitosamente.")
