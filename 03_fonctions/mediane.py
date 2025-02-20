# Mediane
# Écrivez une fonction mediane qui prend un nombre variable de nombres en paramètres et calcule leur mediane.
# Utilisez cette fonction dans un programme qui demande à l’utilisateur d’entrer des nombres, et les mémorise dans une liste.
# Quand l’utilisateur entre une ligne vide, le programme calcule la mediane de ces nombres et l’affiche avec deux chiffres après la virgule.
def mediane():

    # Créer une liste vide pour stocker les nombres
    nombres = []

    # Tant que l'utilisateur n'entre pas une ligne vide, ajouter les nombres à la liste
    while True:
        # Demander à l'utilisateur d'entrer un nombre
        nombre = input("Entrez un nombre : ")
        # Si l'utilisateur entre une ligne vide, sortir de la boucle
        if nombre == "":
            break
        # Ajouter le nombre à la liste
        nombres.append(nombre)

    # Trier la liste des nombres
    liste_nombres = sorted([int(i) for i in nombres])

    # Calcule de l'index du milieu de la liste
    milieu = len(liste_nombres) // 2

    # Si la liste a un nombre pair d'éléments, la médiane est la moyenne des deux éléments du milieu
    if len(liste_nombres) % 2 == 0:
        median = (liste_nombres[milieu - 1] + liste_nombres[milieu]) / 2

    # Si la liste a un nombre impair d'éléments, la médiane est l'élément du milieu
    else:
        median = liste_nombres[milieu]

    print(f"Vous avez entré {len(nombres)} nombres; leur mediane est {median}.")


mediane()
