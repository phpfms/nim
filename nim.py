

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

#nb d'allumettes
lucifer = 21
players = []
new_game = True
# a qui le tour
must_play = ""

def verif_nb_sub (x):
    return x.isdigit

for i in range(2):
    nom = input("Nom du joueur " + str(i + 1) + " ?")
    players.append(nom)
    must_play = players[0]


while new_game == True:

    if lucifer != 1:

        print("c'est à ", must_play.upper(), " de jouer")

        if must_play == players[0]:
            must_play = players[1]
        elif must_play == players[1]:
            must_play = players[0]

        print ( "\rEnleve entre 1 et 4 allumettes" )

        ok = False

        #verif du nombre demandé
        while ok == False:
            nb = input("combien d'allumettes veux tu retirer?:")
            if nb.isdigit():
                ok = True
                nb = int(nb)
                if nb < 1 or nb > 4 or lucifer - nb < 1:
                    print ("Recommence ton choix doit être entre 1 et 4 allumettes et il doit rester au moins 1 allumette")
                    ok = False
                    nb = 0
                else:
                    lucifer -= nb
                    print("Il reste ", lucifer, "allumettes")

    elif lucifer == 1:
        if must_play == players[0]:
            must_play = players[1]
        elif must_play == players[1]:
            must_play = players[0]
        print ("Partie terminée, victoire de ", must_play.upper())
        new_game = False
        answer_nw_g = input("Nouvelle partie? Oui?")
        if answer_nw_g.lower() == "oui" or answer_nw_g.lower() == "o":
            new_game = True
            lucifer = 21
            ok = True

