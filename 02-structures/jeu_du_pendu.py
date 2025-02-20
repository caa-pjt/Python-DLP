from random import choice


# 6. Pendu
# Écrire un programme qui choisit un mot au hasard dans un fichier de mots français, puis laisse l’utilisateur le deviner
# en affichant des tirets pour les lettres inconnues. L’utilisateur a droit à 10 erreurs avant d’être pendu.
def jeu_du_pendu():

    from pendu import HANGMANPICS

    words = [w.strip() for w in open("french_words.txt", encoding="utf-8")]
    mot_a_deviner = choice(words).lower()
    mot_cache = "_ " * len(mot_a_deviner)
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


jeu_du_pendu()
