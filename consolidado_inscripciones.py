import csv
import os
from lector_archivo_texto import LectorArchivoTexto
import json
import sqlite3


class ConsolidadoInscripciones:
    def __init__(self, db_path='universidad.db'):
        self.db_path = db_path

    def _connect_db(self):
        """Crea una conexión con la base de datos."""
        try:
            return sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    """Procesa un archivo de texto y actualiza el consolidado de inscripciones."""

    def consolidarArchivo(self, ruta):
        lector = LectorArchivoTexto(ruta)
        lineas = lector.obtenerLineas()
        for linea in lineas:
            self.procesarLinea(linea.strip())

    def procesarLinea(self, linea):
        try:
            partes = linea.split(',')
            if len(partes) == 4:
                cedula, nombre, codigo, nombre_materia = partes
                with self._connect_db() as conn:
                    if conn is None:
                        return
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
                    conn.commit()
            else:
                print(f"Error en el formato de línea: {linea}")
        except sqlite3.Error as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Error inesperado al procesar la línea: {e}")

    def mostrarEstudiantes(self):
        try:
            with self._connect_db() as conn:
                if conn is None:
                    return
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT e.cedula, e.nombre, m.codigo, m.nombre
                    FROM Estudiantes e
                    JOIN Inscripciones i ON e.cedula = i.cedula
                    JOIN Materias m ON i.codigo = m.codigo
                    ORDER BY e.cedula
                ''')
                estudiantes = cursor.fetchall()

                if estudiantes:
                    for cedula, nombre_estudiante, codigo_materia, nombre_materia in estudiantes:
                        print(f"Cédula: {cedula}, Nombre: {nombre_estudiante}, "
                              f"Materia: {codigo_materia} - {nombre_materia}")
                else:
                    print("No se encontraron estudiantes.")
        except sqlite3.Error as e:
            print(f"Error al consultar la base de datos: {e}")
        except Exception as e:
            print(f"Error inesperado al mostrar estudiantes: {e}")

    def filtrarPorMateria(self, codigo_materia):
        try:
            with self._connect_db() as conn:
                if conn is None:
                    return
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
        except sqlite3.Error as e:
            print(f"Error al filtrar estudiantes por materia: {e}")
        except Exception as e:
            print(f"Error inesperado al filtrar estudiantes: {e}")

    def exportarDatos(self, formato):
        try:
            with self._connect_db() as conn:
                if conn is None:
                    return
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT e.cedula, e.nombre, m.codigo, m.nombre
                    FROM Estudiantes e
                    JOIN Inscripciones i ON e.cedula = i.cedula
                    JOIN Materias m ON i.codigo = m.codigo
                    ORDER BY e.cedula
                ''')
                datos = cursor.fetchall()

                # Asegurarse de que la carpeta 'exportados' exista
                export_folder = 'exportados'
                os.makedirs(export_folder, exist_ok=True)

                if formato == 'json':
                    self._exportar_json(datos, export_folder)
                elif formato == 'csv':
                    self._exportar_csv(datos, export_folder)
                else:
                    print("Formato no reconocido. Use 'json' o 'csv'.")
        except sqlite3.Error as e:
            print(f"Error al exportar datos: {e}")
        except Exception as e:
            print(f"Error inesperado al exportar datos: {e}")

    def _exportar_json(self, datos, folder):
        try:
            estudiantes = []
            for cedula, nombre_estudiante, codigo_materia, nombre_materia in datos:
                estudiantes.append({
                    "cedula": cedula,
                    "nombre": nombre_estudiante,
                    "codigo_materia": codigo_materia,
                    "nombre_materia": nombre_materia
                })

            file_path = os.path.join(folder, 'inscripciones.json')
            with open(file_path, 'w', encoding='utf-8') as archivo_json:
                json.dump(estudiantes, archivo_json, ensure_ascii=False, indent=4)

            print(f"Datos exportados a {file_path}")
        except Exception as e:
            print(f"Error al exportar a JSON: {e}")

    def _exportar_csv(self, datos, folder):
        try:
            file_path = os.path.join(folder, 'inscripciones.csv')
            with open(file_path, 'w', encoding='utf-8', newline='') as archivo_csv:
                writer = csv.writer(archivo_csv)
                # Escribir encabezados
                writer.writerow(["Cédula", "Nombre Estudiante", "Código Materia", "Nombre Materia"])
                # Escribir filas
                writer.writerows(datos)

            print(f"Datos exportados a {file_path}")
        except Exception as e:
            print(f"Error al exportar a CSV: {e}")
