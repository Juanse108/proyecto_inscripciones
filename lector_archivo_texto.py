class LectorArchivoTexto:
    def __init__(self, nombreArchivo: str):
        self.nombreArchivo = nombreArchivo

    """Lee el archivo y retorna las líneas como lista de strings."""
    def obtenerLineas(self):
        try:
            with open(self.nombreArchivo, "r",encoding='utf-8') as archivo:
                return archivo.readlines()
        except FileNotFoundError:
            print(f"Error: El archivo {self.nombreArchivo} no se encontró.")
            return []

