from datetime import date

class Tiger:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

tony = Tiger("Tony", "tiger")