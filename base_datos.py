import sqlite3

# Conexión a la base de datos (se crea un archivo 'universidad.db')
conn = sqlite3.connect('universidad.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear tabla Estudiantes
cursor.execute('''
CREATE TABLE IF NOT EXISTS Estudiantes (
    cedula INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
)
''')

# Crear tabla Materias
cursor.execute('''
CREATE TABLE IF NOT EXISTS Materias (
    codigo INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
)
''')

# Crear tabla Inscripciones (relación entre Estudiantes y Materias)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Inscripciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cedula INTEGER NOT NULL,
    codigo INTEGER NOT NULL,
    FOREIGN KEY (cedula) REFERENCES Estudiantes(cedula),
    FOREIGN KEY (codigo) REFERENCES Materias(codigo)
)
''')

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()


