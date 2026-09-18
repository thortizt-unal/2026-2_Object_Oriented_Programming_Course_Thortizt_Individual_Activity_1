class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"{self.nombre} = {self.edad}")


# La edad de Juan
edad_juan = float(input("Ingrese la edad de Juan: "))
# deje la edad de Juan como float debido a que las operaciones sueltan valores float, los cuales no deberian ser pasados a int, ya que se perderia la informacion decimal. Por ejemplo, si Juan tiene 5 años, Alberto tendria 3.33 años, y Ana 6.66 años. Si se pasa a int, Alberto tendria 3 años y Ana 6 años, lo cual no es correcto.

# Calculamos las edades de los otros miembros de la famlia
edad_alberto = 2 * edad_juan / 3
edad_ana = 4 * edad_juan / 3
edad_mama = edad_alberto + edad_juan + edad_ana

# Empezamos a crear las instancias
juan = Persona("Juan", edad_juan)
alberto = Persona("Alberto", edad_alberto)
ana = Persona("Ana", edad_ana)
mama = Persona("Mamá", edad_mama)

# Mostrar resultados
print("\nLAS EDADES SON:")
alberto.mostrar_info()
juan.mostrar_info()
ana.mostrar_info()
mama.mostrar_info()