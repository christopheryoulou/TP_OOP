# TP0 - Manipulation de structures de données en Python

Ce dossier contient des exercices d'introduction à la programmation orientée objet et aux structures de données en Python (tuples, ensembles, dictionnaires, etc.).

Structure principale
- `dictionnaires.py` : fonctions d'inventaire (dictionnaires).
- `ensembles.py` : fonctions manipulant des ensembles (flottes de robots).
- `tuples.py` : exemples et fonctions travaillant sur des tuples (relevés de capteurs).
- `qualite.py` : fonctions utilitaires pour la qualité des données.
- `tests.py` : suite de tests unitaires pour valider les fonctions.

Exécuter les tests
1. Ouvrez un terminal dans le dossier racine du projet.
2. Lancez les tests en vous plaçant dans le dossier `tp0` puis en exécutant la découverte de tests :

```bash
cd tp0
python -m unittest -v
```

Remarques
- Les modules utilisent des imports relatifs simples (par nom de module); exécuter les tests depuis le dossier `tp0` évite des problèmes d'import.
- La fonction `recalibrer` dans `tuples.py` retourne une nouvelle liste de relevés en remplaçant la valeur des tuples dont le nom correspond; elle remplace toutes les occurrences du nom donné. Le comportement lorsqu'aucun capteur n'est trouvé est de retourner la liste inchangée.

Améliorations possibles
- Transformer les tuples en `namedtuple` ou `dataclass` pour une meilleure lisibilité.
- Ajouter `__init__.py` et rendre `tp0` un package pour faciliter l'import lorsqu'on exécute les tests depuis la racine du dépôt.

Contact
Pour toute question sur ces exercices, demandez ici et je vous aide à adapter ou tester le code.
