VD = 0
J1 = 1
J2 = 2
grille = [
    [VD, VD, VD, VD, VD, VD],  
    [VD, VD, VD, VD, VD, VD],
    [VD, VD, VD, VD, VD, VD],
    [VD, VD, VD, VD, VD, VD],
    [VD, VD, VD, VD, VD, VD],
    [VD, VD, VD, VD, VD, VD],  
]

INACTIF = 0
EN_COURS = 1
FINI = 2

def verification(grille, joueur_actuel):
    # verification dans rangés
    for row in grille:
        for i in range(4):
            if all(cell == joueur_actuel for cell in row[i:i + 4]):
                return True

    # verification dans colonnes
    for col in range(6):
        for i in range(3):
            if all(grille[i + j][col] == joueur_actuel for j in range(4)):
                return True

    # verification de victoire diagonale (gauche-droite)
    for i in range(3):
        for j in range(4):
            if all(grille[i + k][j + k] == joueur_actuel for k in range(4)):
                return True

    # Verification de victoire diagonale (droite-gauche)
    for i in range(3):
        for j in range(3, 6):
            if all(grille[i + k][j - k] == joueur_actuel for k in range(4)):
                return True

    return False

def afficher_grille(grille):
    for row in grille:
        print(row)
    print()

def tour_jeu(grille, joueur_actuel):
    colonne = -1
    while colonne not in [0, 1, 2, 3, 4, 5] or grille[0][colonne] != VD:
        saisie = -1
        while saisie not in ["0", "1", "2", "3", "4", "5"]:
            saisie = input("Colonne ? ")
        colonne = int(saisie)
        if grille[0][colonne] != VD:
            print("Colonne pleine")

    ligne = 5
    while grille[ligne][colonne] != VD:
        ligne -= 1
    grille[ligne][colonne] = joueur_actuel
    return grille

def jeu():
    grille = [
        [VD, VD, VD, VD, VD, VD],  
        [VD, VD, VD, VD, VD, VD],
        [VD, VD, VD, VD, VD, VD],
        [VD, VD, VD, VD, VD, VD],
        [VD, VD, VD, VD, VD, VD],
        [VD, VD, VD, VD, VD, VD],  
    ]
    joueur_actuel = J1
    game_state = EN_COURS

    while game_state == EN_COURS:
        afficher_grille(grille)
        grille = tour_jeu(grille, joueur_actuel)

        if verification(grille, joueur_actuel):
            afficher_grille(grille)
            print(f'Joueur {joueur_actuel} a gagné!')
            game_state = FINI
        elif all(cell != VD for row in grille for cell in row):
            afficher_grille(grille)
            print("Match nul !")
            game_state = FINI
        else:
            joueur_actuel = J1 if joueur_actuel == J2 else J2

    print("Partie terminée.")

# pr commencer le jeu
jeu()
