# 4. Tai Chi Chuan
# Écrire un programme qui trouver des mots français qui commencent par la lettre de la première carte et contiennent
# toutes les autres lettres.
# Exemple pour les lettres ublsr : Mots qui commencent par u et qui contiennent b,l,s,r (dans n'importe quel ordre)


def tai_chi_chuan(groupe_de_lettres):
    for w in open("french_words.txt", encoding="utf-8"):
        if w.startswith(groupe_de_lettres[0]) and all(
            [l in w for l in groupe_de_lettres[1:]]
        ):
            print(w.strip())


tai_chi_chuan(input("Choisir le groupe de lettres: "))
