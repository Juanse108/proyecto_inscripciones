from materia import Materia


class Estudiante:
    def __init__(self, cedula: str, nombre: str):
        self.cedula = cedula
        self.nombre = nombre
        self.materias = []  # Lista de objetos Materia

    """Agrega una materia a la lista del estudiante."""

    def adicionarMateria(self, codigo, nombre):
        self.materias.append(Materia(codigo, nombre))

    """Representación textual del estudiante."""

    def __str__(self) -> str:
        materias_str = ", ".join(str(materia) for materia in self.materias)
        return f"Estudiante: {self.nombre}, Cédula: {self.cedula}, Materias:[ {materias_str} ]"
