import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.area = 0
        self.longitud = 0

    def calcular(self):
        # Calculamos el área del círculo
        self.area = math.pi * self.radio ** 2

        # Calculamos la longitud de la circunferencia
        self.longitud = 2 * math.pi * self.radio


radio = float(input("Ingrese el radio del círculo: "))

circulo = Circulo(radio)
circulo.calcular()

print("El área del círculo es:", circulo.area)
print("La longitud de la circunferencia es:", circulo.longitud)