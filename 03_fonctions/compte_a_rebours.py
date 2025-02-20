import time


# Compte à rebours.
# Écrivez une fonction countdown(n) qui affiche un compte à rebours de n secondes. L’appel sans argument fera un compte depuis 10 :
def countdown(n):
    while n > 0:
        print(f"Il reste {n} secondes.")
        time.sleep(1)
        n -= 1


nombre = int(input("Enter a number: "))
countdown(nombre)
