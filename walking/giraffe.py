
from datetime import date

class Giraffe:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

gerry = Giraffe("Gerry", "GirAFFE")