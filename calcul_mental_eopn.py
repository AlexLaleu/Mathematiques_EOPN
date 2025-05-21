import random
from fractions import Fraction

def jeu1():
    km_initial = random.randint(10, 1000)

    denom1 = random.randint(2, 8)
    num1 = random.randint(1, denom1)
    frac1 = Fraction(num1, denom1)

    while True:
        denom2 = random.randint(2, 8)
        num2 = random.randint(1, denom2)
        frac2 = Fraction(num2, denom2)
        if frac2 != frac1:
            break

    print(f"{km_initial} km avec les réservoirs aux {num1}/{denom1},")
    print(f"combien de km avec les réservoirs aux {num2}/{denom2} ?")

    bonne_reponse = km_initial * (frac2 / frac1)

    reponse = input("Votre réponse (arrondie à l'unité) : ")

    try:
        reponse_utilisateur = int(reponse)
        if abs(reponse_utilisateur - round(bonne_reponse)) <= 1:
            print("Bonne réponse !")
        else:
            print(f"Faux. La bonne réponse était environ {round(bonne_reponse)} km.")
    except ValueError:
        print(f"Entrée invalide, la réponse était {round(bonne_reponse)}.")


def jeu2():
    distance_totale = random.randint(500, 2000)
    pourcentage_avion = random.randint(60, 98)
    vitesse_avion = random.randint(150, 300)
    vitesse_train = random.randint(40, 120)
    temps_transfert = random.randint(10, 60)

    distance_avion = distance_totale * (pourcentage_avion / 100)
    distance_train = distance_totale - distance_avion

    temps_avion = distance_avion / vitesse_avion
    temps_train = distance_train / vitesse_train
    temps_transfert_h = temps_transfert / 60

    duree_totale = temps_avion + temps_train + temps_transfert_h

    print(f"Un homme parcourt une distance de {distance_totale} km.")
    print(f"Il effectue {pourcentage_avion}% de cette distance en avion à une vitesse moyenne de {vitesse_avion} km/h.")
    print(f"Il fait le reste de son voyage en chemin de fer à une vitesse de {vitesse_train} km/h.")
    print(f"En estimant à {temps_transfert} minutes le temps nécessaire pour passer de l'avion au chemin de fer,")
    print("quelle sera la durée totale du voyage ?")

    reponse = input("Votre réponse (en heures, avec 1 chiffre après la virgule) : ")

    try:
        reponse_utilisateur = float(reponse.replace(',', '.'))
        if abs(reponse_utilisateur - round(duree_totale, 1)) <= 0.2:
            print("Bonne réponse !")
        else:
            print(f"Faux. La bonne réponse était environ {round(duree_totale, 1)} h.")
    except ValueError:
        print(f"Entrée invalide, la réponse était {round(duree_totale, 1)}.")


def jeu3():
    while True:
        temps_ensemble = random.randint(5, 40)
        temps_A_seul = random.randint(temps_ensemble + 1, 59)

        if temps_ensemble < temps_A_seul:
            break

    taux_ensemble = 1 / temps_ensemble
    taux_A = 1 / temps_A_seul

    taux_B = taux_ensemble - taux_A
    temps_B_seul = 1 / taux_B

    print(f"A et B ensemble peuvent installer tous les signaux d'avertissement de tempête")
    print(f"sur une base aérienne en {temps_ensemble} minutes.")
    print(f"Sachant que A seul peut installer les signaux en {temps_A_seul} minutes,")
    print("combien de temps faudra-t-il à B pour installer seul ?")

    reponse = input("Votre réponse (en minutes, arrondie à l’unité) : ")

    try:
        reponse_utilisateur = int(reponse)
        if abs(reponse_utilisateur - round(temps_B_seul)) <= 1:
            print("Bonne réponse !")
        else:
            print(f"Faux. La bonne réponse était environ {round(temps_B_seul)} minutes.")
    except ValueError:
        print(f"Entrée invalide, la réponse était {round(temps_B_seul)}.")


def jeu4():
    vitesse_train = random.randint(30, 100)
    vitesse_avion = random.randint(vitesse_train + 30, 300)

    delai_heure = random.choice([i * 0.5 for i in range(1, 11)])

    distance_train = vitesse_train * delai_heure

    vitesse_relative = vitesse_avion - vitesse_train

    temps_rattrapage = distance_train / vitesse_relative

    print(f"Un train s'éloigne de la ville A à une vitesse de {vitesse_train} km/h.")
    print(f"{delai_heure} heure(s) plus tard, un avion part de la même ville pour rattraper le train.")
    print(f"Si l’avion vole à {vitesse_avion} km/h, combien de temps lui faudra-t-il pour rattraper le train en marche ?")

    reponse = input("Votre réponse (en heures, avec 1 chiffre après la virgule) : ")

    try:
        reponse_utilisateur = float(reponse.replace(',', '.'))
        if abs(reponse_utilisateur - round(temps_rattrapage, 1)) <= 0.2:
            print("Bonne réponse !")
        else:
            print(f"Faux. La bonne réponse était environ {round(temps_rattrapage, 1)} h.")
    except ValueError:
        print(f"Entrée invalide, la réponse était {round(temps_rattrapage, 1)}.")


def menu():
    while True:
        print("\n=== MENU DES JEUX ===")
        print("1 - Jeu 1 : Proportions (km et réservoirs)")
        print("2 - Jeu 2 : Durée d’un voyage (avion/train)")
        print("3 - Jeu 3 : Travail en équipe (A et B)")
        print("4 - Jeu 4 : Train et avion (poursuite)")
        print("5 - Choisir un jeu au hasard")
        print("0 - Quitter\n")

        choix = input("Votre choix : ")

        if choix == "1":
            jeu1()
        elif choix == "2":
            jeu2()
        elif choix == "3":
            jeu3()
        elif choix == "4":
            jeu4()
        elif choix == "5":
            random.choice([jeu1, jeu2, jeu3, jeu4])()
        elif choix == "0":
            print("À bientôt !")
            break
        else:
            print("Choix invalide. Veuillez entrer un chiffre de 0 à 5.")

menu()
