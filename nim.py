

"""
Deux joueurs s’affrontent dans ce jeu en se partageant un tas d’allumettes composé au départ de 21
allumettes.
Chaque joueur à son tour enlève entre une et quatre allumettes du tas. Celui qui enlève la dernière
allumette a perdu.
Le programme doit arbitrer une partie se déroulant entre deux joueurs humains, dont leur nom est
demandé au démarrage, ainsi que le joueur qui commence.
Optionnel : donner la possibilité à un joueur humain de jouer contre l'ordinateur appliquant la
stratégie suivante :
• premier cas : le joueur démarre la partie : quand le joueur enlève k allumettes, l'ordinateur
en enlève 5 - k, ce qui entraîne fatalement le joueur à enlever la dernière allumette ;
• deuxième cas : l'ordinateur démarre la partie : se ramener dès que possible au cas précédent
(ce qui ne sera bien sûr possible que si le joueur ne connait pas la stratégie gagnante exposée
dans le premier cas).
Optionnel : ajouter la variante du jeu de Marienbad1, dans laquelle il y a au
départ quatre tas, avec respectivement 1, 3, 5 et  7 allumettes. À chaque tour,
le joueur (dont c'est le tour) prend le nombre d'allumettes qu'il veut, au moins
une et dans un même tas. Celui qui prend la dernière allumette perd.
Permettre dans un premier temps d’arbitrer une telle partie entre deux
joueurs humains, puis proposer de pouvoir joueur contre l’ordinateur
appliquant une stratégie de votre cru (peu importe s’il ne joue pas très bien).
"""

# 10/07/2026

########################## ALGO #####################


###################### FIN ALGO #####################


lucifer = 21
players = []
new_game = 1

def verif_nb_sub (x):
    return x.isdigit


for i in range(2):
    nom = input("Nom du joueur " + str(i) +" ?")
    players.append(nom)

while new_game == 1:
    if lucifer != 1:
        print ( "\rEnleve entre 1 et 4 allumettes" )
        print ("c'est à ", players [0] , " de jouer")
        ok = False

        #verif du nombre demandé
        while ok == False:
            nb = input("combien d'allumettes veux tu retirer?:")
            if nb.isdigit():
                ok = True
                nb = int(nb)
            if nb < 1 or nb > 4:
                print ("Recommence ton choix doit être entre 1 et 4 allumettes")
                ok = False

        lucifer -= nb
        print("Il reste ", lucifer, "allumettes")