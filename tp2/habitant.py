from multipledispatch import dispatch

class Habitant:
    def __init__(self, __nom, __age, __adresse, __animaux=None):
        self.__nom = __nom
        self.__age = __age
        self.__adresse = __adresse
        self.__animaux = __animaux if __animaux is not None else {}

    def get_nom(self):
        return self.__nom
    def get_age(self):
        return self.__age
    def get_adresse (self):
        return self.__adresse
    def get_animaux(self):
        return self.__animaux

    def set_nom(self, nom):
        self.__nom = nom
    def set_age(self, age):
        self.__age = age
    def set_adresse(self, adresse):
        self.__adresse = adresse
    def set_animaux(self, animaux):
        self.__animaux = animaux
    
    def affichage_adresse(self):
        return f"{self.__nom} habite a {self.__adresse}"

    def compte_animal(self, animal):
        return self.__animaux[animal] if animal in self.__animaux else 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, valeur):
        if valeur < 0 or valeur > 130:
            raise ValueError("L'age doit être compris entre 0 et 130 ans.")
        self.__age = valeur

    @dispatch(object, str)
    def set_info(habitant, nom):
        habitant.set_nom(nom)

    @dispatch(object, str, int)
    def set_info(habitant, nom, age):
        habitant.set_nom(nom)
        habitant.set_age(age)

h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
assert h1.get_nom() == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"


h1.age = 26
assert h1.age == 26
try:
    h1.age = -5
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass
