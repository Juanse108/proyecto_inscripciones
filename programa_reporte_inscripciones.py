from consolidado_inscripciones import ConsolidadoInscripciones


class ProgramaReporteInscripciones:
    def __init__(self):
        self.consolidado = ConsolidadoInscripciones()

    """Despliega el menú principal."""
    def mostrarMenu(self):
        while True:
            print("\n--- Menú Principal ---")
            print(" 1. Cargar archivo de inscripciones")
            print(" 2. Mostrar estudiantes y materias inscritas")
            print(" 3. Filtrar estudiantes por materia")
            print(" 4. Exportar datos")
            print(" 5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                ruta = input("Ingrese la ruta del archivo: ")
                self.consolidado.consolidarArchivo(ruta)
            elif opcion == "2":
                self.consolidado.mostrarEstudiantes()
            elif opcion == "3":
                codigo_materia = input("Ingrese el código de la materia: ")
                self.consolidado.filtrarPorMateria(codigo_materia)
            elif opcion == "4":
                formato = input("Seleccione el formato (JSON/CSV): ").lower()
                self.consolidado.exportarDatos(formato)
            elif opcion == "5":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida.")

