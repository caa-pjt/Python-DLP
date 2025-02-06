# Trouver les éléments communs
# 1. Écrire une fonction common qui implémente la recherche d’éléments communs en utilisant le typeset`
# 2. Écrire une fonction common2 qui implémente aussi la recherche d’éléments communs, mais sans utiliser les sets.
def common(word1, word2):
    # Convertir les mots en minuscules et créer des ensembles
    set_word_1 = set(word1.lower())
    set_word_2 = set(word2.lower())

    # Retourner l'intersection des deux ensembles
    return set_word_1 & set_word_2


def common2(word1, word2):
    result = []  # liste vide
    word1, word2 = word1.lower(), word2.lower()  # convertir les mots en minuscules

    # Parcourir les lettres du premier mot
    for i in word1:
        if (
            i in word2 and i not in result
        ):  # si la lettre est dans le deuxième mot et n'est pas déjà dans la liste
            result.append(i)
    return result


# Test
print(common("hello", "world"))  # {'o', 'l'}
print(common2("hello", "world"))  # ['o', 'l']
