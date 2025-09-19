import random

def choisir_bornes():
    print("Choisissez les bornes du nombre à deviner.")
    try:
        borne_min = int(input("Entrer la borne minimale (défaut 0) : ") or 0)
        borne_max = int(input("Entrer la borne maximale (défaut 100) : ") or 100)
        if borne_max <= borne_min:
            print("La borne maximale doit être supérieure à la minimale. Valeurs par défaut utilisées.")
            borne_min, borne_max = 0, 100
    except ValueError:
        print("Valeurs non valides. Bornes par défaut utilisées (0 à 100).")
        borne_min, borne_max = 0, 100
    return borne_min, borne_max

def partie():
    borne_min, borne_max = choisir_bornes()
    nombre_secret = random.randint(borne_min, borne_max)
    nb_essais = 0
    print(f"\nJ'ai choisi un nombre au hasard entre {borne_min} et {borne_max}.")
    print("À vous de le deviner...")

    while True:
        try:
            essai = int(input("Entrer votre essai : "))
        except ValueError:
            print("Veuillez entrer un nombre entier.")
            continue

        nb_essais += 1

        if essai < borne_min or essai > borne_max:
            print(f"Veuillez choisir un nombre entre {borne_min} et {borne_max}.")
            continue

        if essai < nombre_secret:
            print(f"Mauvais choix, le nombre est plus grand que {essai}")
        elif essai > nombre_secret:
            print(f"Mauvais choix, le nombre est plus petit que {essai}")
        else:
            print(f"Bravo! Vous avez trouvé le nombre en {nb_essais} essai(s).")
            break

if __name__ == "__main__":
    partie()
