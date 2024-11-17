from estudiante import Estudiante
from lector_archivo_texto import LectorArchivoTexto


class ConsolidadoInscripciones:
    def __init__(self):
        self.estudiantes = {}  # Diccionario con cédula como clave y objeto Estudiante como valor

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
            estudiante = self.estudiantes.get(cedula, Estudiante(cedula, nombre))
            estudiante.adicionarMateria(codigo, nombre_materia)
            self.estudiantes[cedula] = estudiante
        else:
            print(f"Error en el formato de línea: {linea}")

    def mostrarEstudiantes(self):
        for estudiante in self.estudiantes.values():
            print(estudiante)

    def filtrarPorMateria(self, codigo_materia):
        pass

    def exportarDatos(self, formato):
        pass
