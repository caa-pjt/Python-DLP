# Fonction de debug (optionnel)
# Avertissement Cet exercice est difficile ! Il se résout en quelques lignes de code, mais nécessite de s’être vraiment bien familiarisé avec
# la notion de fonction en python. Faites-le s’il vous intéresse, mais il n’est en aucun cas nécessaire pour la réussite du module !
#
# Écrire une fonction debug qui prend en argument une fonction f et un ou plusieurs arguments ; cette fonction va :
# Afficher la fonction f et ses arguments
# Appeler la fonction f avec les arguments donnés et stocker le résultat
# Afficher le résultat
# Retourner le résultat

from trouver_elements_communs import common


def debug(f, *args):
    print(f"Function: {f.__name__}")
    print(f"args : {args}")
    return f(*args)


result = debug(common, "hello", "world")
print(result)
