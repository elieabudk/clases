#Animales

class Herbivoro:
    def comer(self):
        print("Comiendo plantas")

class Carnivoro:
    def comer(self):
        print("Comiendo carne")

class Omnivoro(Herbivoro, Carnivoro):
    def comer(self):
        Herbivoro.comer(self)
        Carnivoro.comer(self)

oso = Omnivoro()
oso.comer()  # Comiendo plantas
             # Comiendo carne
