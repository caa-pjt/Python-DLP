import math


# Factorielle
# Écrire une fonction qui retourne la factorielle d’un nombre :
def factoriel(n):
    nombre_a_factoriser = n
    for i in range(1, n):
        n = n * i

    print(f"La factorielle de {nombre_a_factoriser} est {n}.")


nombre = int(input("Enter a number à factoriser : "))
factoriel(nombre)
