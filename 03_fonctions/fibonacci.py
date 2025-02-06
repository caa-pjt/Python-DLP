# 1. Suite Fibonacci
# Demander à l'utilisateur de saisir un nombre
# Afficher les n premiers termes de la suite de Fibonacci
def fibonacci(n):
    a = 1
    b = 1
    while a <= n:
        print(a)
        temp = a
        a = b
        b = temp + b


nombre = int(input("Enter a number: "))
fibonacci(nombre)
