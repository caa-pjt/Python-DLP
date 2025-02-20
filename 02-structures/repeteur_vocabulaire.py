import random


# 7. Répéteur de vocabulaire
# Écrire un programme qui permet de répéter du vocabulaire étranger de la manière suivante :
# Dans un premier temps : préparation du quizz. Le programme demande à l’utilisateur des couples question-réponse,
# jusqu’à ce que l’utilisateur entre une question vide.
# Dans un deuxième temps : quizz. Le programme pose les questions à l’utilisateur et vérifie si les réponses proposées
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
