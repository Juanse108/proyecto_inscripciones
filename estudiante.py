from materia import Materia


class Estudiante:
    def __init__(self, cedula: str, nombre: str):
        self.cedula = cedula
        self.nombre = nombre
        self.materias = []  # Lista de objetos Materia

    def adicionarMateria(self, codigo: str, nombre: str) -> None:
        """Agrega una materia a la lista del estudiante."""
        pass

    def __str__(self) -> str:
        """Representación textual del estudiante."""
        return f"Estudiante: {self.nombre} (Cédula: {self.cedula})"
