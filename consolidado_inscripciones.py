import sqlite3
from estudiante import Estudiante
from lector_archivo_texto import LectorArchivoTexto


class ConsolidadoInscripciones:
    def __init__(self, db_path='universidad.db'):
        self.db_path = db_path

    def _connect_db(self):
        """Crea una conexión con la base de datos."""
        return sqlite3.connect(self.db_path)

    """Procesa un archivo de texto y actualiza el consolidado de inscripciones."""

    def consolidarArchivo(self, ruta):
        lector = LectorArchivoTexto(ruta)
        lineas = lector.obtenerLineas()
        for linea in lineas:
            self.procesarLinea(linea.strip())

    def procesarLinea(self, linea):
        partes = linea.split(',')
        if len(partes) == 4:
            cedula, nombre, codigo, nombre_materia = partes
            with self._connect_db() as conn:
                cursor = conn.cursor()
                # Insertar o ignorar estudiante
                cursor.execute('''
                    INSERT OR IGNORE INTO Estudiantes (cedula, nombre)
                    VALUES (?, ?)
                ''', (cedula, nombre))
                
                # Insertar o ignorar materia
                cursor.execute('''
                    INSERT OR IGNORE INTO Materias (codigo, nombre)
                    VALUES (?, ?)
                ''', (codigo, nombre_materia))
                
                # Insertar inscripción
                cursor.execute('''
                    INSERT INTO Inscripciones (cedula, codigo)
                    VALUES (?, ?)
                ''', (cedula, codigo))
        else:
            print(f"Error en el formato de línea: {linea}")

    def mostrarEstudiantes(self):
        with self._connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT e.cedula, e.nombre, m.codigo, m.nombre
                FROM Estudiantes e
                JOIN Inscripciones i ON e.cedula = i.cedula
                JOIN Materias m ON i.codigo = m.codigo
                ORDER BY e.cedula
            ''')
            estudiantes = cursor.fetchall()
            
            for cedula, nombre_estudiante, codigo_materia, nombre_materia in estudiantes:
                print(f"Cédula: {cedula}, Nombre: {nombre_estudiante}, "
                      f"Materia: {codigo_materia} - {nombre_materia}")

    def filtrarPorMateria(self, codigo_materia):
        with self._connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT e.cedula, e.nombre
                FROM Estudiantes e
                JOIN Inscripciones i ON e.cedula = i.cedula
                WHERE i.codigo = ?
            ''', (codigo_materia,))
            estudiantes = cursor.fetchall()
            
            if estudiantes:
                print(f"Estudiantes inscritos en la materia {codigo_materia}:")
                for cedula, nombre in estudiantes:
                    print(f"Cédula: {cedula}, Nombre: {nombre}")
            else:
                print(f"No se encontraron estudiantes inscritos en la materia {codigo_materia}")

    def exportarDatos(self, formato):
        # Implementar según el formato deseado (ej. CSV, JSON)
        pass
