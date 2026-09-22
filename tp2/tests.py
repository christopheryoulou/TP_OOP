from habitant import Habitant, Adulte, Enfant
from village import Village 
import unittest 

class TestHabitant(unittest.TestCase):
    """Tests pour la classe Habitant et l’encapsulation."""
    def test_age_setter_valide(self):
        """Cas normal : age valide."""
        habitant = Habitant("Dupont", "Jean", 30, "123 Rue Principale")
        habitant.age = 35
        self.assertEqual(habitant.age, 35)
        
    def test_age_setter_invalide(self):
        """Cas limite : age negatif."""
        habitant = Habitant("Dupont", "Jean", 30, "123 Rue Principale")
        with self.assertRaises(ValueError):
            habitant.age = -5


class Testvillage(unittest.TestCase):
    """Tests pour la classe Village et l’agregation/composition."""
    def test_ajouter_habitant_composition(self):
        """Cas normal : ajout d’un habitant via composition."""
        village = Village("TestVillage")
        village.ajouter_habitant_composition("Alice", 25, "456 Rue Secondaire")
        self.assertEqual(len(village.get_habitants()), 1)
        self.assertEqual(village.get_habitants()[0].get_nom(), "Alice")

    def test_ajouter_habitant_agregation(self):
        """Cas normal : ajout d’un habitant via agregation."""
        village = Village("TestVillage")
        habitant = Habitant("Bob", "Martin", 40, "789 Rue Tertiaire")
        village.ajouter_habitant_agregation(habitant)
        self.assertEqual(len(village.get_habitants()), 1)
        self.assertEqual(village.get_habitants()[0], habitant)

class testheritage(unittest.TestCase):
    """Tests pour l’héritage et le polymorphisme."""
    def test_adulte_retraite(self):
        """Cas normal : calcul du nombre d’années avant la retraite pour un adulte."""
        adulte = Adulte("Dupont", "Marie", 35, "Rue A")
        self.assertEqual(adulte.calcul_nombre_annee_avant_retraite(), 27)

    def test_enfant_retraite(self):
        """Cas normal : calcul du nombre d’années avant la retraite pour un enfant."""
        enfant = Enfant("Durand", "Paul", 10, "Rue B")
        self.assertIn("enfant", enfant.calcul_nombre_annee_avant_retraite())
        try:
            enfant = Enfant("Durand", "Paul", 20, "Rue B")
        except ValueError:
            pass
        else:
            self.fail("Une ValueError aurait dû être levée pour un enfant de 20 ans.")


if __name__ == "__main__":
    unittest.main(verbosity=2)