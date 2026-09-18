class Empleado:
    def __init__(self, horas, valor_hora):
        self.horas = horas
        self.valor_hora = valor_hora
        self.salario_bruto = 0
        self.retencion = 0
        self.salario_neto = 0

    def calcular_salario(self):
        # Calculamos el salario antes de la retención
        self.salario_bruto = self.horas * self.valor_hora

        # Calculamos el 12.5% de retención
        self.retencion = self.salario_bruto * 12.5 / 100

        # Restamos la retención para obtener el salario neto
        self.salario_neto = self.salario_bruto - self.retencion


empleado = Empleado(48, 5000)
empleado.calcular_salario()

print("SALARIO BRUTO =", empleado.salario_bruto)
print("RETENCION EN LA FUENTE =", empleado.retencion)
print("SALARIO NETO =", empleado.salario_neto)