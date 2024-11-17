class Materia:
    class Materia:
        def __init__(self, codigo: str, nombre: str):
            self.codigo = codigo
            self.nombre = nombre

        def __str__(self) -> str:
            """Representación textual de la materia."""
            return f"Materia: {self.nombre} (Código: {self.codigo})"
