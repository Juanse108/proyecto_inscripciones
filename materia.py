
class Materia:
    def __init__(self, codigo: str, nombre: str):
        self.codigo = codigo
        self.nombre = nombre

    """Representación textual de la materia."""
    def __str__(self) -> str:
        return f"Materia: {self.nombre} (Código: {self.codigo})"
