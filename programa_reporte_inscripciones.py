from consolidado_inscripciones import ConsolidadoInscripciones


class ProgramaReporteInscripciones:
    def __init__(self):
        self.consolidado = ConsolidadoInscripciones()

    def mostrarMenu(self) -> None:
        """Despliega el menú principal."""
        pass

    def cargarArchivo(self, ruta: str) -> None:
        """Carga un archivo de texto y procesa sus datos."""
        pass

    def mostrarEstudiantes(self) -> None:
        """Muestra todos los estudiantes y sus materias inscritas."""
        pass

    def filtrarPorMateria(self, codigo: str) -> None:
        """Muestra estudiantes inscritos en una materia específica."""
        pass

    def exportarDatos(self, formato: str) -> None:
        """Exporta los datos en formato JSON o CSV."""
        pass
