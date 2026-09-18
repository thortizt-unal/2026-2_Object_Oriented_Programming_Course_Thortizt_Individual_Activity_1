class Operacion:
    def __init__(self):
        self.suma = 0
        self.x = 20
        self.y = 0

    def calcular(self):
        # Primero sumamos X a la suma
        self.suma = self.suma + self.x

        # Le damos el valor de 40 a Y
        self.y = 40

        # Elevamos Y al cuadrado y se lo sumamos a X
        self.x = self.x + self.y ** 2

        # Actualizamos la suma con el nuevo valor de X
        self.suma = self.suma + self.x / self.y


operacion = Operacion()
operacion.calcular()

print("EL VALOR DE LA SUMA ES:", operacion.suma)