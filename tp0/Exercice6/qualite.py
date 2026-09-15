"""
def f(d, t, x1, y1, x2, y2):
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if t == 'R':
        c = dist * 1.0
    elif t == 'H':
        c = dist * 1.5
    elif t == 'S':
        c = dist * 2.0
    else:
        c = dist * 3.0
    print("cout:", c)
    return c
"""

from math import dist


def cout_deplacement_propre(type_terrain, x1, y1, x2, y2):
    """
    Calcule le coût de déplacement d'un robot en fonction de la distance et du type de terrain.

    :param d: La distance entre les deux points (x1, y1) et (x2, y2).
    :param type_terrain: Le type de terrain ('R' pour route, 'H' pour herbe, 'S' pour sable, autre pour obstacles).
    :param x1: La coordonnée x du point de départ.
    :param y1: La coordonnée y du point de départ.
    :param x2: La coordonnée x du point d'arrivée.
    :param y2: La coordonnée y du point d'arrivée.
    :return: Le coût de déplacement calculé.
    """
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if type_terrain == 'R':
        cout = distance * 1.0
    elif type_terrain == 'H':
        cout = distance * 1.5
    elif type_terrain   == 'S':
        cout = distance * 2.0
    else:
        cout = distance * 3.0
    return cout