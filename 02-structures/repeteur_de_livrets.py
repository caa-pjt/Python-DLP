from random import choice


# 2. Répéteur de livrets
def repeteur_de_livrets(livret_a_repete):
    livret = {}
    nbr_reponses_justes = 0
    for i in range(1, 11):
        # print(i, "x", livret_a_repete, "=", i * livret_a_repete)
        livret[i] = i * livret_a_repete
    # print(livret)
    a_deviner = choice(list(livret.keys()))
    while True:
        nombre = int(input(f"Combien font {a_deviner} x {livret_a_repete} ? "))
        if nombre == livret[a_deviner]:
            nbr_reponses_justes += 1
            del livret[a_deviner]
            print("Bravo!")
            # print(livret)
            a_deviner = choice(list(livret.keys()))
            if nbr_reponses_justes == 5:
                print("Félicitations! Vous avez réussi!")
                break
        else:
            if nbr_reponses_justes > 0:
                nbr_reponses_justes -= 1
            print("ré-essayez!")


repeteur_de_livrets(int(input("Quel livret voulez-vous répéter? ")))
