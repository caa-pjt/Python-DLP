# Structures de données et de contrôle
## Guess a number

Écrire un programme qui choisit un nombre au hasard entre 1 et 10, puis laisse l’utilisateur le deviner de la 
manière suivante (les entrées de l’utilisateur sont en gras) :

```bash
Devinez un nombre entre 1 et 10
Votre proposition: 5
Non, plus!
Votre proposition: 7
Non, moins!
Votre proposition: 6
Bravo!
```
## Répéteur de livrets

Écrire un programme qui permet d’entraîner ses livrets:
```bash
5 x 2 = 10
Bravo!
2 x 8 = 16
Bravo!
2 x 3 = 7
Non, ré-essayez!
2 x 3 = 8
Non, ré-essayez!
2 x 3 = 6
Bravo!
```
1. Première version : en boucle infinie (ctrl-c pour arrêter).

2. Pose des questions jusqu’à ce que l’utilisateur entre 5 réponses correctes à la suite.

3. (Optionnel) Pour être sûr d’apprendre complètement ses livrets :
    - Construire une liste de toutes les questions possibles
    - Tirer une question au hasard
    - Demander la réponse jusqu’à ce qu’elle soit juste
    - Si l’utilisateur a répondu juste du premier coup, retirer la question de la liste
    - Si la liste de questions n’est pas vide, reprendre à 2.
## Mots français

Dans un nouveau fichier, tapez
```bash
words = [w.strip() for w in open('french_words.txt', encoding='utf-8')]
```
(Ne vous inquiétez pas si vous ne comprenez pas ce code – ça viendra plus tard!)

Sauvez le fichier french_words.txt au même endroit que votre code (source: http://www.pallier.org/liste-de-mots-francais.html#liste-de-mots-francais).

Dans la variable words, vous avez maintenant une grande liste de mots français. Trouvez une manière de répondre aux questions suivantes: dans cette liste de mots,
- combien y a-t-il de mots en tout ?
- combien de mots de 4 lettres ?
- combien de mots commençant par z ?
- combien de mots contenant la lettre z ?
- combien de mots commençant par a et finissant par s ?

## Tai Chi Chuan

Le jeu de société Tai Chi Chuan se compose de cartes avec des lettres; étant donné un certain nombre de cartes, il s’agit de trouver des mots français qui commencent par la lettre de la première carte et contiennent toutes les autres lettres.

En utilisant la liste de mots de l’exercice précédent, implémentez un assistant pour ce jeux: le programme demandera la liste de lettres et trouvera tous les mots qui correspondent:

```
Vos lettres: ublsr
Mots qui commencent par u et qui contiennent b,l,s,r (dans n'importe quel ordre):
ultrasensible
ultra-sensible
ultrasensibles
ultra-sensibles
urobilines
urobilinogènes
urobilinuries
```

Remarque Le jeu original est un peu plus subtil… mais nous nous limiterons à cette version !

## Anagrammes

Toujours avec la même liste de mot, écrivez un chercheur d’anagrammes: le programme demande un mot à l’utilisateur et affiche tous ses anagrammes (mots s’écrivant avec exactement les mêmes lettres, mais pas focrément dans le même ordre). Le programme demandera ensuite un nouveau mot, jusqu’à ce que l’utilisateur tape sur enter sans avoir entré aucun mot:
```bash
Entrez un mot: python
python
typhon
Entrez un mot: chien
chien
chine
niche
Entrez un mot:
Au revoir
```

Indice : Il existe différentes manières d’aborder le problème. Une possibilité est d’utiliser `sorted` : comparez `sorted
('python')` et `sorted('typhon')` et regardez si cela vous donne une piste…

Améliorations possibles (optionnel): modifiez votre programme pour qu’il

- Ne tienne pas compte des majuscules/minuscules
- Ne tienne pas compte des accents
- Ne tienne pas compte des tirets
- …
```bash
Entrez un mot: Paris
    pairs
    paris
    parsi
    prias
    prisa
    ripas
Entrez un mot: à-coup
    à-coup
    coupa
```
## Pendu
Implémentez le [jeu du pendu :](https://fr.wikipedia.org/wiki/Pendu_(jeu))
```bash
Devinez le mot!
_ _ _ _ _ _ _
Entrez une lettre: e
_ _ _ _ _ e _
Entrez une lettre: a
Non! Plus que 9 erreurs permises.
_ _ _ _ _ e _
Entrez une lettre: i
_ _ i _ _ e _
Entrez une lettre: o
_ o i _ _ e _
Entrez une lettre: u
Non! Plus que 8 erreurs permises.
_ o i _ _ e _
Entrez une lettre: s
Non! Plus que 7 erreurs permises.
_ o i _ _ e _
Entrez une lettre: r
_ o i _ _ e r
Entrez une lettre: t
Non! Plus que 6 erreurs permises.
_ o i _ _ e r
Entrez une lettre: m
Non! Plus que 5 erreurs permises.
_ o i _ _ e r
Entrez une lettre: n
_ o i n _ e r
Entrez une lettre: p
Non! Plus que 4 erreurs permises.
_ o i n _ e r
Entrez une lettre: t
Non! Plus que 3 erreurs permises.
_ o i n _ e r
Entrez une lettre: c
c o i n c e r
Bravo!
```

## Répéteur de vocabulaire

Écrire un programme qui permet de répéter du vocabulaire étranger de la manière suivante :

- Dans un premier temps: préparation du quizz. Le programme demande à l’utilisateur des couples question-réponse, 
jusqu’à ce que l’utilisateur entre une question vide.
- Dans un deuxième temps: quizz. Le programme pose les questions à l’utilisateur et vérifie si les réponses proposées 
  sont conformes à celles de la première étape.

```bash
Préparation du quizz
Question (<enter> pour terminer): computer
Réponse: ordinateur
Question (<enter> pour terminer): printer
Réponse: imprimante
Question (<enter> pour terminer): mouse
Réponse: souris
Question (<enter> pour terminer): 

==================================
Début du quizz!
computer
> ordinateur
Oui!
printer
> écran
Non!
mouse
> souris
Oui!
```
**Amélioration** (optionnelle) Plutôt que de poser les questions dans l’ordre où elles ont été entrées, posé les 
questions dans un ordre aléatoire et continuer jusqu’à ce que toutes les questions aient reçu une réponse correcte.
