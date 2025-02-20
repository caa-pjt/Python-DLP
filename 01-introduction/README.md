
# Prise en main de python 
## Préliminaire

Installez [thonny](https://thonny.org/) (ou travaillez avec vos outils préférés si vous en avez).
## Python comme calculette

Lancez thonny, puis dans sa console (shell), faites quelques calculs en utilisant les quatre opérations `+`, `-`, `*`, `/` ainsi que l’élévation à la puissance `**`.

- avec des entiers (int): `1 + 2`
- avec des floats: `1.2 * 2.6`

Expérimentez:

1. Que se passe-t-il quand vous mélangez les types? quel est le type du résultat? (en cas de doute, essayez `type(2+2.0))`
    - **Réponse :** le résultat est un float.

2. Que se passe-t-il quand le résultat d’un calcul est un très grand nombre `(2**2048)`? Quelle est la limite de taille 
   pour un entier? Les entiers et les floats se comportent-ils de la même manière?
   - **Réponse :** les entiers n’ont pas de limite de taille, les floats si.

3. Pour tous les types natifs de python, vous pouvez utiliser le nom du type pour transformer un type en un autre : 
   essayez `float(1)` et d’autres conversions.
4. Quel est le résultat de `int(float(10**100)) - (10 ** 100)`? Expliquez.
    - **Réponse :** le résultat n'est pas égal à zéro à cause des erreurs d'arrondi qui se produisent lorsqu'un très 
      grand nombre est converti en `float`, puis reconverti en `int` (perte de précision, car les floats ont une 
      limite de taille).

5. Les nombres complexes sont aussi gérés nativement par python, au détail près que le `i` des mathématiciens est 
remplacé par un `j`. Essayez `1j ** 2` et d’autres calculs.
   - **Réponse :** `1j ** 2` est égal à `(-1+0j)`.

## Le module `math

En tapant `import math`, vous avez accès à une multitude de fonctions mathématiques.

1. Essayez la racine carrée: `math.sqrt(100)`

2. Parcourez la [documentation](https://docs.python.org/fr/3/library/math.html) du module math et expérimentez quelques fonctions.

3. Dans Thonny, si vous tapez `math.`, puis `ctrl-space`, vous devriez avoir un menu proposant les divers éléments 
disponibles dans ce module. Expérimentez! Vous pouvez aussi configurer Thonny pour que cette complétion apparaisse automatiquement lorsque vous tapez le `.`

Optionnel:

3. Le module `cmath` propose des fonctions pour les nombres complexes. Importez-le puis essayez `cmath.sqrt(-1)`. Utilisez 
la [doc](https://docs.python.org/fr/3/library/cmath.html) ou la complétion pour trouver les autres fonctions disponibles.

## Les chaînes de caractères

Les chaînes de caractères peuvent être délimitées par

- des guillemets simples (apostrophes): `'hello'`
- des guillemets doubles: `"hello"`
- de plus, les délimiteurs peuvent être triplés : `'''hello'''` ou `"""hello"""`

1. Quelles sont les différences entre toutes ces possibilités ?
    - **Réponse :** les guillemets simples et doubles sont équivalents, mais les guillemets simples doivent être 
      échappés `''C\'est une chaine de caractères''`
    - les délimiteurs triplés simple ou double permettent d'écrire des chaînes de caractères sur plusieurs lignes.
    
2. Quel est l’avantage d’avoir autant de variantes pour un même type ?
    - **Réponse :** Chaque type de guillemet offre une fonctionnalité particulière qui peut être utile dans certaines 
      situations.
      - Si l'on veut inclure un guillemet simple dans une chaîne, on peut utiliser des guillemets doubles pour 
        délimiter la chaîne. `"C'est une chaine de caractères"`
      - Si l'on veut inclure inclure un guillemet double dans une chaîne, on peut utiliser des guillemet simples pour 
        délimiter la chaîne. `'Ceci est une "chaine de caractères"'`
      - Ceci est particulièrement utile pour les chaînes de caractères multilignes.

3. Expérimentez avec les chaînes de caractères et les 4 opérations (`'a' + 'b'`). Qu’est-ce qui marche, qu’est-ce qui ne 
   marche pas ?
   - **Réponses :** 
     - `''a' + 'b''`     Résultat : `SyntaxError: invalid syntax`
     - `"'a' + 'b'"`     Résultat :  `"'a' + 'b'"`
     - `"""'a' + 'b'"""` Résultat :  `"'a' + 'b'"`
     - `''''a' + 'b''''` Résultat :  `SyntaxError: unterminated string literal (ligne 1)`

4. Mélangez les types `('a' * 2)`. Là aussi, déterminez ce qui marche et ce qui ne marche pas.
    - Réponse : 
      - `''a' * 2'`       Résultat : `SyntaxError: invalid syntax`
      - `"'a' * 'b'"`     Résultat : `"'a' * 2"`
      - `"""'a' * 2"""` Résultat : `"'a' * 2"`
      - `''''a' * 2'''`   Résultat : `"'a' * 2"`

Le type chaîne de caractères `(str)` en python est un type dit séquentiel. Consultez le [tableau](https://docs.python.org/fr/3/library/stdtypes.html#common-sequence-operations) des opérations 
   communes sur les séquences et testez-les sur différentes chaînes de caractères.



## Variables

Toute valeur peut être stockée dans une variable :
```bash
>>> my_string = 'abc'
>>> n = 2
>>> result = my_string * n
>>> result
'abcabc'
```

1. Quels sont les noms de variables possibles ? essayez de trouver des contre-exemples.
2. On peut intégrer les valeurs de variables dans des chaînes de caractères en utilisant les f-strings. [Lisez cette 
   description](https://rtavenar.github.io/poly_python/content/chaines.html#pour-aller-plus-loin-les-f-strings) (uniquement la section sur les f-strings) et faites quelques expérimentations pour vous 
   familiariser avec cet outil.

    [Voir le site :](https://realpython.com/python-f-strings/#using-an-objects-string-representations-in-f-strings)

Exemple 1 :
```python
name = "Jane"
age = 25

f"Hello, {name}! You're {age} years old."
```
Exemple 2 :
```python
integer = -1234567
f"Comma as thousand separators: {integer:,}"
# 'Comma as thousand separators: -1,234,567'

sep = "_"
f"User's thousand separators: {integer:{sep}}"
# 'User's thousand separators: -1_234_567'

floating_point = 1234567.9876
f"Comma as thousand separators and two decimals: {floating_point:,.2f}"
# 'Comma as thousand separators and two decimals: 1,234,567.99'

date = (9, 6, 2023)
f"Date: {date[0]:02}-{date[1]:02}-{date[2]}"
# 'Date: 09-06-2023'

from datetime import datetime
date = datetime(2023, 9, 26)
f"Date: {date:%m/%d/%Y}"
# 'Date: 09/26/2023'
```

## Expression vs print

Comparez ces deux manières de faire un calcul :
```bash
>>> 1+1
2
>>> print(1+1)
2
```

Elles semblent équivalentes… pouvez-vous imaginer une situation où elles se distingueraient ?
 - **Réponse :** 
   - `1 + 1`  Ne s'affiche pas (renvoi le résultat de l'opération)
   - `print(1 + 1)`  Affiche le résultat de l'opération
6. Premiers programmes python

Dans la partie éditeur de thonny, tapez
```python
name = input('Quel est votre nom? ')
print(f'Bonjour, {name}!')
```

La première ligne demande à l’utilisateur d’entrer son nom, puis stocke le résultat dans la variable name. La seconde utilise les f-strings vu ci-dessus pour afficher une salutation personnalisée.

Sauvez votre fichier (avec l’extension .py), puis choisissez Exécuter→Exécuter le script courant (ou simplement la touche <F5>). Dans la partie console, vous pourrez interagir avec votre programme.

1. Écrivez un programme qui demande une température en degrés Celsius à l’utilisateur et la convertit en degrés 
Fahrenheit:
```text
Entrez une température en °C: 37
Équivalent en °F: 98.60
```

2. Écrivez un programme qui permet à l’utilisateur d’entrer deux nombres et effectue des calculs de la manière suivante:
```text
Entrez le nombre a: 123
Entrez le nombre b: 456
a + b = 579
a * b = 56088
L'élévation de a à la puissance b est 992...561.
Ce nombre s'écrit avec 953 chiffres et contient 113 fois le chiffre 1.
```
## Débogueur

Un débogueur est un utilitaire qui permet de retracer pas à pas l’exécution d’un programme pour en comprendre le fonctionnement et aider à y débusquer des bugs. Thonny dispose d’un débogueur intégré.

Commencez par activer Affichage→Variables; ceci ouvre un nouvel onglet affichant une représentation des variables en mémoire (qui devrait être vide pour l’instant).

Reprenez votre programme du point 5.1. Plutôt que de simplement l’exécuter, choisissez Exécuter→Déboguer le script courant (plus joli) ou simplement <CTRL-F5>. Thonny met en évidence la première ligne du programme pour indiquer que c’est la prochaine chose à faire.

Appuyez de manière répétée sur <F7> et suivez attentivement chaque étape de l’exécution de votre programme. Notez également comme les affectations de variables sont observables dans l’onglet correspondant.

Re-lancez le programme en mode debug autant de fois qu’il vous est nécessaire pour avoir bien compris chaque étape: que fait python actuellement et pourquoi?

Faites de même avec votre programme du point 5.2.
## Et pour finir…

Contemplez le programme suivant :
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]
a[0] = 2
print(a)
print(b)
print(c)
```
1. Sans l’exécuter, essayez de prévoir ce qu’il affichera.
    - **Réponse :** `[2, 2, 3]`, `[2, 2, 3]`, `[1, 2, 3]`
2. Exécutez-le et comparez. Êtes-vous surpris ? Pourquoi ?
 - **Réponse :** Non, car les variables `a` et `b` pointent vers la même liste, alors que la variable `c` pointe vers une autre liste.

