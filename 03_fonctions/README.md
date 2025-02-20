# Fonctions

## Fibonacci

Écrivez une fonction `fibonacci(n)` qui affiche les termes de la suite de Fibonacci inférieurs à n. La suite commence
par `1, 1` et chaque terme est la somme des deux termes précédents :

```bash
>>> fibonacci(50)
1
1
2
3
5
8
13
21
34
>>>
```
*Remarque* Dans Thonny, vous pouvez écrire cette fonction dans l’éditeur, puis exécuter votre fichier (<F5>). Votre
fonction sera alors disponible dans le shell pour la tester. Hors de Thonny, vous pouvez obtenir ce comportement
avec `python -i myfile.py. Ou alors, ajouter à votre fichier un appel à la fonction avant de l’exécuter.

## Compte à rebours

Écrivez une fonction `countdown(n)` qui affiche un compte à rebours de n secondes. L’appel sans argument fera un
compte depuis 10 :

```bash
>>> countdown(3)
Il reste 3 secondes.
Il reste 2 secondes.
Il reste 1 secondes.
>>> countdown()
Il reste 10 secondes.
Il reste 9 secondes.
Il reste 8 secondes.
Il reste 7 secondes.
Il reste 6 secondes.
Il reste 5 secondes.
Il reste 4 secondes.
Il reste 3 secondes.
Il reste 2 secondes.
Il reste 1 secondes.
>>>
```

Indice Jetez un coup d’oeil à [time.sleep](https://docs.python.org/fr/3/library/time.html#time.sleep)

## Factorielle

Écrire une fonction qui retourne la factorielle d’un nombre:

Remarque Il existe bien sûr déjà math.factorial… mais l’idée est de la ré-implémenter vous-même!

```bash
>>> fact(6)
720
>>> import math
>>> fact(100) == math.factorial(100)
True
>>> 
```

## Mediane

Écrivez une fonction `mediane` qui prend un nombre variable de nombres en paramètres et calcule leur mediane.

D’après [Wikipedia](https://fr.wikipedia.org/wiki/M%C3%A9diane_(statistiques)#Mode_de_calcul) :

> La méthode consiste à ordonner les valeurs en une liste croissante et à choisir la valeur qui est au centre de cette liste.
> Pour une liste ordonnée de n éléments, n étant impair, la valeur de l’élément à la position (n+1)/2 est la médiane.
> Si le nombre n d’éléments est pair, toute valeur comprise entre les éléments en positions n/2 et n/2+1 est une médiane;
> en pratique, dans le cas d’une liste de nombres, c’est la moyenne arithmétique de ces deux valeurs centrales qui est en général utilisée.


```bash
>>> mediane(1,2,3,4)
2.5
>>> mediane(1,2,3,4,8)
3
>>> 
```

Utilisez cette fonction dans un programme qui demande à l’utilisateur d’entrer des nombres, et les mémorise dans une liste.
Quand l’utilisateur entre une ligne vide, le programme calcule la mediane de ces nombres et l’affiche avec deux chiffres après la virgule.

```bash
Entrez un nombre par ligne, ligne vide pour terminer.
12
5
6
89
5
1

Vous avez entré 6 nombres; leur mediane est 5.50
```

*NB* Là aussi, une fonction plus ou moins équivalente existe: `statistics.median.
Dans un cas réel, c’est bien sûr celle-ci qu’il faudrait utiliser… mais rien n’empêche de la ré-implémenter pour
l’exercice !

## Trouver les éléments communs

1. Écrire une fonction `common qui implémente la recherche d’éléments communs en utilisant le type `set`
2. Écrire une fonction `common2` qui implémente aussi la recherche d’éléments communs, mais sans utiliser les sets.

```bash
>>> word1 = 'anticonstitutionnellement'
>>> word2 = 'ecclésiastique'
>>> common(word1, word2)
['a', 't', 'i', 'c', 's', 'u', 'e', 'l']
>>> common2(word1, word2)
{'i', 'e', 'l', 's', 'u', 'c', 'a', 't'}
>>> sorted(common(word1, word2)) == sorted(common2(word1, word2))
True
>>> 
```

3. (Optionnel) Comparer l’efficacité des deux implémentations avec le module [timeit[(https://docs.python.org/3/library/timeit.html), qui permet d’exécuter un code
   un grand nombre de fois (par défaut 1 million) en mesurant le temps que cela prend :
```bash
import timeit
print(timeit.timeit('common(word1, word2)', globals=globals()))
print(timeit.timeit('common2(word1, word2)', globals=globals())) 
```
## Fonction de debug (optionnel)

Avertissement Cet exercice est difficile ! Il se résoud en quelques lignes de code, mais nécessite de s’être
vraiment bien familiarisé avec la notion de fonction en python. Faites-le s’il vous intéresse, mais il n’est en
aucun cas nécessaire pour la réussite du module !

1. Écrire une fonction `debug` qui prend en argument une fonction f et un ou plusieurs arguments; cette fonction va :
- Afficher la fonction f et ses arguments
- Appeler la fonction f avec les arguments donnés et stocker le résultat
- Afficher le résultat
- Retourner le résultat

```bash
>>> import math
>>> f = debug(math.factorial, 6)
Calling <built-in function factorial> with args (6,) and kwargs {}
The result is 720
>>> f
720
>>> 
>>> g = debug(math.gcd, 10, 12)
Calling <built-in function gcd> with args (10, 12) and kwargs {}
The result is 2
>>> g
2
>>>
```

2. Écrire une fonction debug2 qui permet d’afficher les mêmes informations de debug qui ci-dessus, mais de la
   manière suivante :

```bash
>>> import math
>>> d_fact = debug2(math.factorial)
>>> d_fact(6)
Calling <built-in function factorial> with args (6,) and kwargs {}
The result is 720
720
>>> 
```
## Et pour finir…

Créez un dépôt git sur github. Déposez-y les exercices que vous avez déjà faits et, dorénavant, tous ceux que vous
ferez pour ce cours, selon une structure du type

```bash
Dépôt git
|
+- 01_bases
|  |
|  +- ex_06_01_degrees.py
|  +- ex_06_02_numbers.py
|
+- 02_structures
|  |
|  +- ex_01_guess.py
|  +- ex_02_01_livrets.py
|  +- ...
```
Donnez des droits de lecture sur ce dépôt aux utilisateurs `amiguet` et `lucalaissue`.

