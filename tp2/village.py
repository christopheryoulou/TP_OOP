from habitant import*

"""ajouter_habitant_composition represente une composition car l'habitant est cree dans la classe villageois
tandis qu'avec ajouter_habitant_agregation, il existe deja et est simplement ajoute a la liste des habitants du village. """

class Village:
    def __init__(self, nom):
        self.nom = nom
        self.__habitants = []

    def get_habitants(self):
        return self.__habitants
    
    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None):
        h = Habitant(nom, age, adresse, animaux)
        self.__habitants.append(h)

    def ajouter_habitant_agregation(self, habitant):
        self.__habitants.append(habitant)
        
    def afficher_habitants(self):
        for i in self.__habitants:
            print(i["nom"])



pytown = Village("PyTown")
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
elise = Habitant("Elise", 28, "Rue B", {"poules": 10})
pytown.ajouter_habitant_agregation(elise)
autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_agregation(elise) # meme habitant dans 2 villages
assert len(pytown.get_habitants()) == 2
assert elise in autre_village.get_habitants()