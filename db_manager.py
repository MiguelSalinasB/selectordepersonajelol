import sqlite3

class DBManager:
    def __init__(self, db_name="league_of_legends.db"):
        # Conexión a la base de datos (se crea si no existe)
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        # Crear las tablas necesarias
        self.create_tables()

    def create_tables(self):
        # Crear la tabla 'champions' si no existe
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS champions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            image TEXT NOT NULL
        )
        ''')

        # Crear la tabla 'matches' si no existe
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            champion_id INTEGER NOT NULL,
            result TEXT NOT NULL,
            date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (champion_id) REFERENCES champions (id)
        )
        ''')

        self.conn.commit()

    def insert_champion(self, name, image):
        # Insertar un nuevo campeón en la tabla 'champions'
        self.cursor.execute('''
        INSERT INTO champions (name, image) 
        VALUES (?, ?)
        ''', (name, image))
        self.conn.commit()

    def update_victory(self, champion_id):
        # Registrar una victoria en la tabla 'matches'
        self.cursor.execute('''
        INSERT INTO matches (champion_id, result) 
        VALUES (?, 'win')
        ''', (champion_id,))
        self.conn.commit()

    def update_defeat(self, champion_id):
        # Registrar una derrota en la tabla 'matches'
        self.cursor.execute('''
        INSERT INTO matches (champion_id, result) 
        VALUES (?, 'loss')
        ''', (champion_id,))
        self.conn.commit()

    def delete_champion(self, champion_id):
        # Borrar todas las partidas asociadas al campeón
        self.cursor.execute('''
        DELETE FROM matches WHERE champion_id = ?
        ''', (champion_id,))
        self.conn.commit()

        # Borrar el campeón de la tabla 'champions'
        self.cursor.execute('''
        DELETE FROM champions WHERE id = ?
        ''', (champion_id,))
        self.conn.commit()

    def get_champion_by_name(self, name):
        # Obtener la información de un campeón por su nombre
        self.cursor.execute('''
        SELECT id, name, image FROM champions WHERE name = ?
        ''', (name,))
        return self.cursor.fetchone()

    def get_all_champions(self):
        # Obtener la información de todos los campeones
        self.cursor.execute('''
        SELECT id, name, image FROM champions
        ''')
        return self.cursor.fetchall()

    def get_match_history(self, champion_id):
        # Obtener el historial de partidas de un campeón
        self.cursor.execute('''
        SELECT result, date FROM matches WHERE champion_id = ?
        ORDER BY date DESC
        ''', (champion_id,))
        return self.cursor.fetchall()

    def close(self):
        # Cerrar la conexión a la base de datos
        self.conn.close()
