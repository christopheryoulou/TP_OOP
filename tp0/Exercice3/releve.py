releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

def afficher_releve(releve):
    """
    Affiche un relevé de capteur sous forme de chaîne de caractères.
    
    :param releve: Un tuple contenant le nom du capteur, la valeur mesurée et l'unité.
    :return: Une chaîne de caractères formatée représentant le relevé.
    """
    nom_capteur, valeur, unite = releve
    return f"Capteur {nom_capteur} : {valeur} {unite}"

assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"

print("it works!")