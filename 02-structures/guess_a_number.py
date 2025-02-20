# 1. Guess a number
# Écrire un programme qui choisit un nombre au hasard entre 1 et 10, puis laisse l’utilisateur le deviner de la
# manière suivante (les entrées de l’utilisateur sont en gras) :
import random
from itertools import count
from random import randint


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


guess_a_number()
