from estudiante import Estudiante
from lector_archivo_texto import LectorArchivoTexto


class ConsolidadoInscripciones:
    class ConsolidadoInscripciones:
        def __init__(self):
            self.estudiantes = {}  # Diccionario con cédula como clave y objeto Estudiante como valor

        def consolidarArchivo(self, ruta: str) -> None:
            """Procesa un archivo de texto y actualiza el consolidado de inscripciones."""
            pass

        def procesarLinea(self, linea: str) -> None:
            """Procesa una línea de texto y actualiza el consolidado."""
            pass

        def buscarEstudiante(self, cedula: str):
            """Busca y retorna un estudiante por su cédula."""
            return self.estudiantes.get(cedula, None)

        def mostrarEstudiantes(self) -> None:
            """Itera por los estudiantes y muestra sus datos."""
            pass

        def filtrarPorMateria(self, codigo: str) -> list:
            """Retorna una lista de estudiantes inscritos en una materia específica."""
            pass

        def exportarDatos(self, formato: str) -> None:
            """Exporta los datos procesados en JSON o CSV."""
            pass
