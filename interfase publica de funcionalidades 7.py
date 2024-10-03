class Persona:
    def _init_(self, nombre, edad):
        # Método constructor para inicializar nombre, edad y estado
        self.nombre = nombre
        self.edad = edad
        self.esta_despierto = True  # Por defecto, la persona está despierta

    def dormir(self):
        # Método para cambiar el estado a "durmiendo"
        self.esta_despierto = False

    def despertar(self):
        # Método para cambiar el estado a "despierto"
        self.esta_despierto = True

    def mostrar_estado(self):
        # Método para imprimir el estado actual de la persona
        estado = "despierto/a" if self.esta_despierto else "durmiendo/a"
        print(f"{self.nombre} (edad: {self.edad}) está {estado}.")

# Ejemplo de uso:
persona1 = Persona("Juan", 25)
persona1.mostrar_estado()  # Muestra que está despierto
persona1.dormir()          # Cambia el estado a durmiendo
persona1.mostrar_estado()  # Muestra que está durmiendo
persona1.despertar()       # Cambia el estado a despierto
persona1.mostrar_estado()  # Muestra que está despierto nuevamente