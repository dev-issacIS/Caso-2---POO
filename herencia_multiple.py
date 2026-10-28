# Clase base
class Matricula:
    """Representa una matrícula con un costo base."""

    def costo(self):
        """Devuelve el derecho base de matrícula."""
        return 60.0


class MatriculaExtemporanea(Matricula):
    """Agrega un recargo por matrícula fuera de fecha."""

    def costo(self):
        return super().costo() + 15


class MatriculaDesaprobatoria(Matricula):
    """Agrega un recargo por índice desaprobatorio."""

    def costo(self):
        return super().costo() + 15


class MatriculaBeca(Matricula):
    """Aplica un descuento del 50 %."""

    def costo(self):
        return super().costo() * 0.5


#### Primera versión: programador 1 ####

# El programador coloca primero la beca, después el índice desaprobatorio y finalmente la matrícula extemporánea


class MatriculaCombinada1( MatriculaBeca,
    MatriculaDesaprobatoria,
    MatriculaExtemporanea
):
    """Combina las tres modalidades especiales."""
    pass


luis = MatriculaCombinada1()

print(luis.costo())
print([clase.__name__ for clase in MatriculaCombinada1.mro()])

#### Segunda versión: programador 2 ####

# El programador coloca primero la de índice académico desaprobatorio, luego la extemporánea y al final la de beca

class MatriculaCombinada2(
    MatriculaDesaprobatoria,
    MatriculaExtemporanea,
    MatriculaBeca
):
    """Combina las tres modalidades en otro orden."""
    pass


rosa = MatriculaCombinada2()

print(rosa.costo())
print([clase.__name__ for clase in MatriculaCombinada2.mro()])