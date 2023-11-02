# from time import *
# kp = keypushed
# KE = KEY_EXE
# KO = KEY_OK

VD=0 #case vide
J1=1 #case remplie par joueur 1
J2=2 #case remplie par joueur 2
grille = [
	[VD, VD, VD, VD, VD, VD],  #Ligne d'indice 0 affichée en haut de l'écran
	[VD, VD, VD, VD, VD, VD],
	[VD, VD, VD, VD, VD, VD],
	[VD, VD, VD, VD, VD, VD],
	[VD, VD, VD, VD, VD, VD],
	[VD, VD, VD, VD, VD, VD],  # Ligne d'indice 6 affichée en bas de l'écran
]

INACTIF = 1 # jeu n'a pas débuté.
EN_COURS = 1 # les joueurs sont en train de jouer
FINI = 2 # la partie est finie car l'un des joueurs a gagné ou la grille est pleine

def verification(grille):
	pass
    # Vérification en colonne 
    for k in range(6):
        for i in range(3):
            if grille [i] [k] == numero_dujoueur \
                and grille [i+1] [k] == numero_dujoueur \
                    and grille [i+2] [k] == numero_dujoueur \
                        and grille [i+3] [k] == numero_dujoueur :
                        return True
    
    # Vérification en ligne
    for i in range(6):
        for k in range(3):
            if grille [k] [I] == numero_dujoueur \
                and grille [k+1] [i] == numero_dujoueur \
                    and grille [k+2] [i] == numero_dujoueur \
                        and grille [k+3] [i] == numero_dujoueur :
                        return True

# Vérification en diagonale
    for i in range(3):
        for k in range(3):
            if grille [k] [I] == numero_dujoueur \
                and grille [k+1] [i+1] == numero_dujoueur \
                    and grille [k+2] [i+2] == numero_dujoueur \
                        and grille [k+3] [i+3] == numero_dujoueur :
                        return True
				
def tour_jeu(grille, joueur_actuel):
    # Choix de la colonne par le joueur
    colonne = -1
    while colonne not in [0,1,2,3,4,5] or grille[0][colonne] != 0:
        saisie = -1
        while saisie not in ["0","1","2","3","4","5"]:
            saisie = input("Colonne ? ")
        colonne = int(saisie)
        if grille[0][colonne] != 0:
            print("Colonne pleine")
    print(colonne)
    print('joueur' ,joueur_actuel,',', 'ton tour est fini')
    
    # Changement de la valeur dans la grille
    ligne = 5
    while grille[ligne][colonne] != 0:
        ligne -= 1
    grille[ligne][colonne] = joueur_actuel
    return grille

def jeu():
    VD=0 #case vide
    grille = [
        [VD, VD, VD, VD, VD, VD],  #Ligne d'indice 0 affichée en haut de l'écran
        [VD, VD, VD, VD, VD, VD],
        [VD, VD, VD, VD, VD, VD],
        [VD, VD, VD, VD, VD, VD],
        [VD, VD, VD, VD, VD, VD],
        [VD, VD, VD, VD, VD, VD],  # Ligne d'indice 6 affichée en bas de l'écran
    ]
    joueur_actuel = 1
    while True:
        grille = tour_jeu(grille, joueur_actuel)
        # Changement de joueur
        joueur_actuel = 3- joueur_actuel
        print(grille)
