class Recargo:
    """Representa un recargo fijo de matrícula."""

    def __init__(self, monto):
        self.monto = monto

    def aplicar(self, costo):
        return costo + self.monto


class Beca:
    """Representa un descuento porcentual."""

    def __init__(self, porcentaje):
        self.porcentaje = porcentaje

    def aplicar(self, costo):
        return costo * (1 - self.porcentaje / 100)


class Matricula:
    """Calcula la matrícula aplicando ajustes en orden."""

    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.ajustes = []

    def agregar_ajuste(self, ajuste):
        self.ajustes.append(ajuste)

    def costo(self):
        total = 60.0

        for ajuste in self.ajustes:
            total = ajuste.aplicar(total)

        return total


# Primera matrícula: recargos antes de la beca
luis = Matricula("Luis Huamaní Cárdenas")
luis.agregar_ajuste(Recargo(15))
luis.agregar_ajuste(Recargo(15))
luis.agregar_ajuste(Beca(50))

# Segunda matrícula: beca antes de los recargos
rosa = Matricula("Rosa Ccahuana Prado")
rosa.agregar_ajuste(Beca(50))
rosa.agregar_ajuste(Recargo(15))
rosa.agregar_ajuste(Recargo(15))

print(f"Luis: S/ {luis.costo():.2f}")
print(f"Rosa: S/ {rosa.costo():.2f}")

# Salida

# Luis: S/ 45.00
# Rosa: S/ 60.00