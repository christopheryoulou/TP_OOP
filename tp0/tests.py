from dictionnaires import*
from ensembles import*
from qualite import*
from tuples import*
import unittest

class TestJournalDeBord(unittest.TestCase):
    """Tests pour les fonctions sur les relevés (tuples)."""

    def test_recalibrer_capteur_existant(self):
        """Cas nominal : le capteur demandé existe."""
        releves = [("laser_avant", 2.35, "m"), ("laser_arriere", 1.10, "m"), ("gyroscope", 87.5, "deg")]
        nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
        assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
        assert nouveaux_releves[1] == ("laser_arriere", 1.10, "m")
        assert nouveaux_releves[2] == ("gyroscope", 87.5, "deg")
    
    def test_recalibrer_capteur_absent(self):
        """Cas limite : le capteur demande n’existe pas."""
        releves = [("laser_avant", 2.35, "m"), ("laser_arriere", 1.10, "m"), ("gyroscope", 87.5, "deg")]
        nouveaux_releves = recalibrer(releves, "laser_central", 2.40)
        assert nouveaux_releves == releves

    def test_recalibrer_plusieurs_occurrences(self):
        """Cas : plusieurs relevés portent le même nom; tous doivent être recalibrés."""
        releves = [("laser_avant", 2.00, "m"), ("laser_avant", 2.10, "m"), ("gyroscope", 87.5, "deg")]
        nouveaux_releves = recalibrer(releves, "laser_avant", 2.50)
        assert nouveaux_releves[0] == ("laser_avant", 2.50, "m")
        assert nouveaux_releves[1] == ("laser_avant", 2.50, "m")
        assert nouveaux_releves[2] == ("gyroscope", 87.5, "deg")

if __name__ == "__main__":
    unittest.main(verbosity=2)

class TestFlotteRobots(unittest.TestCase):
    """Tests pour les fonctions sur les ensembles (flotte de robots)."""

    def test_robots_double_mission(self):
        """Cas nominal : intersection de deux ensembles."""
        robots_exploration = {"R2", "R5", "R7"}
        robots_transport = {"R5", "R9", "R7", "R3"}
        double_mission = robots_double_mission(robots_exploration, robots_transport)
        assert double_mission == {"R5", "R7"}

    def test_ajouter_robot_mission(self):
        """Cas limite : ajout d’un robot déjà présent dans l’ensemble."""
        robots_exploration = {"R2", "R5", "R7"}
        ajout = ajouter_robot_mission(robots_exploration, "R5")
        assert ajout == {"R2", "R5", "R7"}
        assert robots_exploration == {"R2", "R5", "R7"}  # L’ensemble d’origine ne doit pas avoir été modifié

class TestInventaire(unittest.TestCase):
    """Tests pour les fonctions sur les dictionnaires (inventaire de pièces)."""

    def test_consommer_piece(self):
        """Cas nominal : consommation d’une quantité de pièces."""
        pieces_stock = {
            "ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
            "ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
        }
        consommation = consommer_piece(pieces_stock, "ModeleA", "moteurs", 5)
        assert consommation == {"moteurs": 5, "capteurs": 25, "roues": 40}
        assert pieces_stock["ModeleA"]["moteurs"] == 5

    def test_total_pieces(self):
        """Cas limite : calcul du total de pièces pour un inventaire vide."""
        pieces_stock = {}
        totaux = total_pieces(pieces_stock)
        assert totaux == {"moteurs": 0, "capteurs": 0, "roues": 0}