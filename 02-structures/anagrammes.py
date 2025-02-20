# 5 : Anagrammes
# Écrire un programme demande un mot à l’utilisateur et affiche tous ses anagrammes (mots s’écrivant avec exactement
# les mêmes lettres, mais pas forcément dans le même ordre).
# Le programme demandera ensuite un nouveau mot, jusqu’à ce que l’utilisateur tape sur enter sans avoir entré aucun mot :
def anagrammes():
    print(
        """Bienvenue dans le jeu des anagrammes! 
Entrez un mot pour trouver tous ses anagrammes.
Pour quitter le programme appuyez sur Enter sans taper de mot."""
    )
    anagramme = True
    words = [w.strip() for w in open("french_words.txt", encoding="utf-8")]
    while anagramme == True:
        mot = input("Entrez un mot: ")
        for w in words:
            if sorted(w.strip()) == sorted(mot):
                print(w.strip())
        if mot == "":
            anagramme = False
            print("Merci d'avoir joué!")


anagrammes()
