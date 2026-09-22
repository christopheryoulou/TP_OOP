from abc import ABC, abstractmethod
from multipledispatch import dispatch

class Habitant(ABC):
    def __init__(self, __nom, __prenom, __age, __adresse, __animaux=None):
        self.__nom = __nom
        self.__prenom = __prenom
        self.__age = __age
        self.__adresse = __adresse
        self.__animaux = __animaux if __animaux is not None else {}

    def get_nom(self):
        return self.__nom
    def get_prenom(self):
        return self.__prenom
    def get_age(self):
        return self.__age
    def get_adresse (self):
        return self.__adresse
    def get_animaux(self):
        return self.__animaux

    def set_nom(self, nom):
        self.__nom = nom
    def set_prenom(self, prenom):
        self.__prenom = prenom
    def set_age(self, age):
        self.__age = age
    def set_adresse(self, adresse):
        self.__adresse = adresse
    def set_animaux(self, animaux):
        self.__animaux = animaux
    
    def affichage_adresse(self):
        return f"{self.__nom} {self.__prenom} habite a {self.__adresse}"

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

    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self):
        pass
        #return 62 - self.get_age() if 62 - self.get_age >= 0 else
    
    def __str__(self):
        return f"{self.__prenom} {self.__nom}, {self.__age} ans, habite à {self.__adresse}"
        

class Adulte(Habitant):
    def __init__(self, nom, prenom, age, adresse):
        if age < 18:
            raise ValueError("Un adulte doit avoir au moins 18 ans")
        super().__init__(nom, prenom, age, adresse)
    
    def calcul_nombre_annee_avant_retraite(self):
        return 62 - self.get_age() if 62 - int(self.get_age()) > 0 else "deja a la retraite"

class Enfant(Habitant):
    def __init__(self, nom, prenom, age, adresse):
        if age >= 18:
            raise ValueError("Un enfant doit avoir moins de 18 ans")
        super().__init__(nom, prenom, age, adresse)

    def calcul_nombre_annee_avant_retraite(self):
        return "c'est un enfant qui ne travaille probablement pas"

"""
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
"""

adulte = Adulte("Dupont", "Marie", 35, "Rue A")
enfant = Enfant("Martin", "Lucas", 12, "Rue B")
assert isinstance(adulte, Habitant)
assert adulte.calcul_nombre_annee_avant_retraite() == 27
assert "enfant" in enfant.calcul_nombre_annee_avant_retraite()
try:
    Enfant("Oups", "mince", 25, "Rue C")
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass
print(adulte)
def affichage(h: Habitant):
    print(h)
print(enfant)

"""Cela garantit que chaque sous-classe implémente obligatoirement la méthode, évitant 
ainsi les erreurs d'exécution ou les oublis silencieux qu'un simple pass aurait permis."""