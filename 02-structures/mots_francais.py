# 3. Mots français
def mots_francais():
    words = [w.strip() for w in open("french_words.txt", encoding="utf-8")]
    # combien y a-t-il de mots en tout?
    print(len(words))
    # combien de mots de 4 lettres ?
    print(len([w for w in words if len(w) == 4]))
    # combien de mots commençant par z ?
    print(len([w for w in words if w.startswith("z")]))
    # combien de mots contenant la lettre z ?
    print(len([w for w in words if "z" in w]))
    # combien de mots commençant par a et finissant par s ?
    print(len([w for w in words if w.startswith("a") and w.endswith("z")]))


mots_francais()
