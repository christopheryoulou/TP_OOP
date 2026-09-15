pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

def quantite_piece(pieces_stock, modele, piece):

    return pieces_stock[modele][piece]

assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10

def consommer_piece(pieces_stock, modele, piece, quantite):
    pieces_stock[modele][piece] -= quantite

def ajouter_modele(pieces_stock, modele, **pieces):
    pieces_stock[modele] = pieces

def total_pieces(pieces_stock):
    totaux = {}
    for modele in pieces_stock:
        for piece, quantite in pieces_stock[modele].items():
            if piece not in totaux:
                totaux[piece] = 0
            totaux[piece] += quantite
    return totaux

consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7
ajouter_modele(pieces_stock, "ModeleC",
moteurs=4, capteurs=10, roues=16)
assert pieces_stock["ModeleC"] == \
{"moteurs": 4, "capteurs": 10, "roues": 16}
totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}

print("it works!")