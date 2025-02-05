# 1. Guess a number
# Écrire un programme qui choisit un nombre au hasard entre 1 et 10, puis laisse l’utilisateur le deviner de la
# manière suivante (les entrées de l’utilisateur sont en gras) :
import random
from itertools import count
from random import randint, choice


# 1 Guess a number
def guess_a_number():
    a_deviner = randint(1, 10)

    nombre = int(input("Devinez le nombre entre 1 et 10: "))

    while True:
        if nombre < a_deviner:
            print("Non, plus!")
            nombre = int(input("Devinez le nombre entre 1 et 10 : "))
        elif nombre > a_deviner:
            print("Non, moins!")
            nombre = int(input("Devinez le nombre entre 1 et 10 : "))
        else:
            print("Bravo!")
            break


# guess_a_number()


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


# repeteur_de_livrets(int(input("Quel livret voulez-vous répéter? ")))


# 3. Mots français
def mots_francais():
    words = [w.strip() for w in open("french_words.txt", encoding="utf-8")]
    # combien y a-t-il de mots en tout?
    print(len(words))
    # combien de mots de 4 lettres ?
    print(len([w for w in words if len(w) == 4]))
    # combien de mots commençant par z ?
    print(len([w for w in words if w.startswith("z")]))
    # combien de mots contenant la lettre z ?
    print(len([w for w in words if "z" in w]))
    # combien de mots commençant par a et finissant par s ?
    print(len([w for w in words if w.startswith("a") and w.endswith("z")]))


# mots_francais()

# 4. Tai Chi Chuan
# Écrire un programme qui trouver des mots français qui commencent par la lettre de la première carte et contiennent toutes les autres lettres.
# Exemple pour les lettres ublsr : Mots qui commencent par u et qui contiennent b,l,s,r (dans n'importe quel ordre)


def tai_chi_chuan(groupe_de_lettres):
    for w in open("french_words.txt", encoding="utf-8"):
        if w.startswith(groupe_de_lettres[0]) and all(
            [l in w for l in groupe_de_lettres[1:]]
        ):
            print(w.strip())


# tai_chi_chuan(input("Choisir le groupe de lettres: "))


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


# anagrammes()


# 6. Pendu
# Écrire un programme qui choisit un mot au hasard dans un fichier de mots français, puis laisse l’utilisateur le deviner
# en affichant des tirets pour les lettres inconnues. L’utilisateur a droit à 10 erreurs avant d’être pendu.
def jeu_du_pendu():

    from pendu import HANGMANPICS

    words = [w.strip() for w in open("french_words.txt", encoding="utf-8")]
    mot_a_deviner = choice(words).lower()
    mot_cache = "_" * len(mot_a_deviner)
    nbr_essais = len(HANGMANPICS)

    print("Bienvenue dans le jeu du pendu !")
    print(f"Vous avez droit à {nbr_essais} erreurs.")
    print(mot_cache)

    while nbr_essais > 0:

        if mot_a_deviner == mot_cache:
            print("🎉 Bravo! Vous avez trouvé le mot !")
            break

        lettre = input("Entrez une lettre : ").lower()

        if lettre == "":
            print("Entrez une lettre!")
            continue

        if len(lettre) > 1 or not lettre.isalpha():
            print("Entrez une seule lettre !")

        else:

            if len(lettre) == 1 and lettre in mot_a_deviner:
                for j in range(len(mot_a_deviner)):
                    if mot_a_deviner[j] == lettre:
                        mot_cache = mot_cache[:j] + lettre + mot_cache[j + 1 :]
                print("✅ Bonne réponse !")
                print(mot_cache)
            elif lettre not in mot_a_deviner and nbr_essais > 1:
                nbr_essais -= 1
                # Afficher le pendu pluto que le nombre d'essais restants
                print(HANGMANPICS[len(HANGMANPICS) - 1 - nbr_essais])
                print(f"❌ Non! Plus que {nbr_essais} erreurs permises.")
                print(mot_cache)
            else:
                print(HANGMANPICS[len(HANGMANPICS) - 1])
                print(
                    f"Désolé, vous avez été pendu! Le mot était ({mot_a_deviner.upper()})"
                )
                break


# jeu_du_pendu()


# 7. Répéteur de vocabulaire
# Écrire un programme qui permet de répéter du vocabulaire étranger de la manière suivante :
# Dans un premier temps: préparation du quizz. Le programme demande à l’utilisateur des couples question-réponse,
# jusqu’à ce que l’utilisateur entre une question vide.
# Dans un deuxième temps: quizz. Le programme pose les questions à l’utilisateur et vérifie si les réponses proposées
# sont conformes à celles de la première étape.
def repeteur_vocabulaire():

    tableau_questions = {}

    while True:

        question = input("Entrez une question: ")
        reponse = ""

        if question == "":
            break
        reponse = input("Entrez la réponse: ")

        if reponse == "":
            continue

        tableau_questions[question] = reponse

    if len(tableau_questions) == 0:
        print("Aucune question n'a été ajoutée!")
        return

    print("Début du quizz!")
    nbr_reponses_justes = 0
    for question, reponse in random.sample(
        list(tableau_questions.items()), len(tableau_questions)
    ):
        reponse_utilisateur = input(f"{question} : ")
        if reponse_utilisateur.lower().strip() == reponse.lower().strip():
            nbr_reponses_justes += 1
            print("Bravo!")
        else:
            print(f"Non, la réponse était {reponse}")

    else:
        # Pourcentage de réponses justes
        pourcentage = (nbr_reponses_justes / len(tableau_questions)) * 100
        print(f"Félicitations! Vous avez réussi! Note: {pourcentage}%")


repeteur_vocabulaire()
