class Algoritmo:
    def __init__(self, numero):
        self.numero = numero
        self.cuadrado = 0
        self.cubo = 0

    def calcular(self):
        # Calculamos el cuadrado y el cubo del número
        self.cuadrado = self.numero ** 2
        self.cubo = self.numero ** 3


numero = float(input("Ingrese un número: "))

algoritmo = Algoritmo(numero)
algoritmo.calcular()

print("El cuadrado es:", algoritmo.cuadrado)
print("El cubo es:", algoritmo.cubo)


