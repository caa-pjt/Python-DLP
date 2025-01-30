import math
import cmath
# sqrt() est une fonction de la bibliothèque math qui permet de calculer la racine carrée d'un nombre
# print(math.sqrt(100)) # 10.0
# print(cmath.sqrt(-100)) # 10.0j

# Exercice sur les chaines de caractères
a = 'C\'est une chaine de caractères'
b = "hello"
c = '''
hello

world
'''
d = """
hello
world

"""
'''
print(a)
print(b)
print(c)
print(d)
'''

# Exercices avec les f-string (format string) et les input

# Écrivez un programme qui demande une température en degrés Celsius à l’utilisateur et la convertit en degrés Fahrenheit
# Calcule de transformation °c en Fahrenheit : F = C * 9/5 + 32
def celsius_to_fahrenheit():
    temp_celsius = float(input("Entrez une température en °C:"))
    print(f"{temp_celsius}°C = {temp_celsius * 9/5 + 32:.2f}°F") # :.2f permet d'afficher 2 chiffres après la virgule

celsius_to_fahrenheit()

# Écrivez un programme qui permet à l’utilisateur d’entrer deux nombres et effectue des calculs de la manière suivante:
# Entrez le nombre a: 123
# Entrez le nombre b: 456
# a + b = 579
# a * b = 56088
# L'élévation de a à la puissance b est 992...561.
# Ce nombre s'écrit avec 953 chiffres et contient 113 fois le chiffre 1.

def calculer():
    a = int(input("Entrez le nombre a: "))
    b = int(input("Entrez le nombre b: "))
    # Addition
    print(f"{a} + {b} = {a + b}")

    # Multiplication
    print(f"{a} * {b} = {a * b:.0f}")

calculer()


