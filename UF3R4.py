class Soldado:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
        self.fuerza = 100

    def perdida(self, cantidad):

        self.fuerza -= cantidad
        if self.fuerza <= 0:
            self.fuerza = 0
            return "¡El soldado ha muerto! (Fuerza = 0)"
        return f"El soldado ha perdido fuerza. Fuerza actual: {self.fuerza}"

    def ganancia(self, cantidad):

        self.fuerza += cantidad
        if self.fuerza > 100:
            self.fuerza = 100
        return f"El soldado ha ganado fuerza. Fuerza actual: {self.fuerza}"

soldado1 = Soldado(peso=80, altura=180)
print(f"Soldado creado - Peso: {soldado1.peso}, Altura: {soldado1.altura}, Fuerza inicial: {soldado1.fuerza}")
print(soldado1.perdida(30))
print(soldado1.ganancia(20))