# BACCALAURÉAT GÉNÉRAL NSI TERMINALE - ÉPREUVE PRATIQUE - SUJETS - SESSION 2023

# ------------------------------ SUJET 1 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-01.pdf !

# Exercice 2 :

urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = ...
    for bulletin in urne:
        if ...:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            ...
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if ... > ...:
            nmax = ...
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == ...]
    return ...

# ------------------------------ SUJET 2 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-02.pdf !

# Exercice 2 :

def positif(pile):
    pile_1 = ...(pile)
    pile_2 = ...
    while pile_1 != []:
        x = ...
        if ... >= 0:
            pile_2.append(...)
    while pile_2 != ...:
        x = pile_2.pop()
        ...
    return pile_1

# ------------------------------ SUJET 3 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-03.pdf !

# Exercice 2 :

coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *", end = "")
            else:
                print("  ", end = "")
        print()

def zoomListe(liste_depart, k):
    liste_zoom = ...
    for elt in ... :
        for i in range(k):
            ...
    return liste_zoom

def zoomDessin(grille, k):
    grille_zoom = []
    for elt in grille:
        liste_zoom = ...
        for i in range(k):
            ... .append(...)
    return grille_zoom

# ------------------------------ SUJET 4 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-04.pdf !

# Exercice 2 :

bombes = [(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]
grille_test = [[1, 1, 1, 0, 0], [1, -1, 1, 1, 1], [2, 2, 3, 2, -1], [1, -1, 2, -1, 3], [1, 1, 2, 2, -1]]

def voisinage(n, ligne, colonne):
    voisins = []
    for l in range(max(0, ligne - 1), min(n, ligne + 2)):
        for c in range(max(0, colonne - 1), min(n, colonne + 2)):
            if (l, c) != (ligne, colonne):
                voisins.append((l, c))
    return voisins

def incrémente_voisins(grille, ligne, colonne):
    voisins = ...
    for l, c in voisins:
        if grille[l][c] != ...:
            ... 

def génère_grille(bombes):
    n = len(bombes)
    grille = [[0 for colonne in range(n)] for ligne in range(n)]
    for ligne, colonne in bombes:
        grille[ligne][colonne] = ... 
        ...  
    return grille

# ------------------------------ SUJET 5 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-05.pdf !

# Exercice 2 :

img = [[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]

def nbLig(image):
    return ...

def nbCol(image):
    return ...

def negatif(image):
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(...):
            L[i][j] = ...
    return L

def binaire(image, seuil):
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(...):
            if image[i][j] < ...:
                L[i][j] = ...
            else:
                L[i][j] = ...
    return L

# ------------------------------ SUJET 6 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-06.pdf !

# Exercice 2 :

from math import sqrt 

def distance(point1, point2):
    return sqrt((...)**2 + (...)**2)

def plus_courte_distance(tab, depart):
    point = tab[0]
    min_dist = ...
    for i in range (1, ...):
        if distance(tab[i], depart) ...:
            point = ...
            min_dist = ...
    return point

# ------------------------------ SUJET 7 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-07.pdf !

# Exercice 2 :

romains = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def traduire_romain(nombre):
    if len(nombre) == 1:
        return ...
    elif romains[nombre[0]] >= ...:
        return romains[nombre[0]] + ...
    else:
        return ...

# ------------------------------ SUJET 8 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-08.pdf !

# Exercice 2 :

class Pile:

    def __init__(self):
        self.contenu = []

    def est_vide(self):
        return self.contenu == []

    def empiler(self, v):
        self.contenu.append(v)

    def depiler(self):
        if not self.est_vide():
            return self.contenu.pop()

def eval_expression(tab):
    p = Pile()
    for ... in tab:
        if element != '+' ... element != '*':
            p.empiler(...)
        else:
            if element == ...:
                resultat = p.depiler() + ...
            else:
                resultat = ...
            p.empiler(...)
    return ...

# ------------------------------ SUJET 9 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-09.pdf !

# Exercice 2 :

def chercher(tab, n, i, j):
    if i < 0 or j > len(tab):
        return None
    elif i > j:
        return None
    m = (i + j) // ...
    if ... < n:
        return chercher(tab, n, ..., ...)
    elif ... > n:
        return chercher(tab, n, ..., ...)
    else:
        return ...
    
# ------------------------------ SUJET 10 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-10.pdf !

# Exercice 2 :

class Pile:

    def __init__(self):
        self.valeurs = []

    def est_vide(self):
        return self.valeurs == []

    def empiler(self, c):
        self.valeurs.append(c)

    def depiler(self):
        if self.est_vide() == False:
            self.valeurs.pop()

def parenthesage(ch):
    p = Pile()
    for c in ch:
        if c == ...:
            p.empiler(c)
        elif c == ...:
            if p.est_vide():
                return ...
            else:
                ...
    return p.est_vide()

# ------------------------------ SUJET 11 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-11.pdf !

# Exercice 2 :

liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[...]
        j = ...
        while j > ... and valeur_insertion < tab[...]:
            tab[j] = tab[j - 1]
            j = ...
        tab[j] = ...

# ------------------------------ SUJET 12 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-12.pdf !

# Exercice 2 :

def empaqueter(liste_masses, c):
    n = len(liste_masses)
    nb_boites = 0
    boites = [0] * n
    for masse in ...:
        i = 0
        while i <= nb_boites and boites[i] + ... > c:
                i = i + 1
        if i == nb_boites + 1:
                ...
        boites[i] = ...
    return ...

# ------------------------------ SUJET 13 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-13.pdf !

# Exercice 2 :

pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):
    rendu = ...
    a_rendre = ...
    i = len(pieces) - 1
    while ... :
        if pieces[i] <= a_rendre:
            rendu.append(...)
            a_rendre = ...
        else:
            i = ...
    return rendu

# ------------------------------ SUJET 14 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-14.pdf !

# Exercice 2 :

def insere(a, tab):
    l = list(tab)
    l.append(a)
    i = ...
    while a < ... and i >= 0: 
      l[i + 1] = ...
      l[i] = a
      i = ...
    return l

# ------------------------------ SUJET 15 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-15.pdf !

# Exercice 2 :

def inverse_chaine(chaine):
    result = ...
    for caractere in chaine:
       result = ...
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return ...
    
def est_nbre_palindrome(nbre):
    chaine = ...
    return est_palindrome(chaine)

# ------------------------------ SUJET 16 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-16.pdf !

# Exercice 2 :

resultats = {'Dupont': {
                           'DS1': [15.5, 4],
                           'DM1': [14.5, 1],
                           'DS2': [13, 4],
                           'PROJET1': [16, 3],
                           'DS3': [14, 4]
                       },
             'Durand': {
                           'DS1': [6 , 4],
                           'DM1': [14.5, 1],
                           'DS2': [8, 4],
                           'PROJET1': [9, 3],
                           'IE1': [7, 2],
                           'DS3': [8, 4],
                           'DS4': [15, 4]
                       }
            }

def moyenne(nom, dico_result):
    if nom in ...:
        notes = dico_result[nom]
        total_points = ...
        total_coefficients = ...
        for ... in notes.values():
            note, coefficient = valeurs
            total_points = total_points + ... * coefficient
            total_coefficients = ... + coefficient
        return round(... / total_coefficients, 1)
    else:
        return -1

# ------------------------------ SUJET 17 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-17.pdf !

# Exercice 2 :

def pascal(n):
    triangle = [[1]]
    for k in range(1, ...):
        ligne_k = [...]
        for i in range(1, k):
            ligne_k.append(triangle[...][i - 1] + triangle[...][...])
        ligne_k.append(...)
        triangle.append(ligne_k)
    return triangle

# ------------------------------ SUJET 18 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-18.pdf !

# Exercice 2 :

def est_un_ordre(tab):
    for i in range(1, ...):
        if ...:
            return False
    return True

def nombre_points_rupture(ordre):
    assert ...
    n = len(ordre)
    nb = 0
    if ordre[...] != 1:
        nb = nb + 1
    i = 0
    while i < ...:
        if ... not in [-1, 1]: 
            nb = nb + 1
        i = i + 1
    if ordre[...] != n:
        nb = nb + 1
    return nb

# ------------------------------ SUJET 19 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-19.pdf !

# Exercice 2 :

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    resultat = ''
    for ... in message:
        if 'A' <= c and c <= 'Z':
            indice = ( ... ) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = ...
    return resultat

# ------------------------------ SUJET 20 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-20.pdf !

# Exercice 2 :

from random import randint

def nbre_coups():
    n = ...
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while ... < ...:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + ...) % ...
        if ...:
            cases_vues.append(case_en_cours)
        n = ...
    return n

# ------------------------------ SUJET 21 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-21.pdf !

# Exercice 2 :

e = Noeud(Noeud(Noeud(None, 3, None),
    '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))),
    '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))

class Noeud:

    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __str__(self):
        return str(self.valeur)

    def est_une_feuille(self):
        return self.gauche is None and self.droit is None

def expression_infixe(e):
    s = ...
    if e.gauche is not None:
        s = '(' + s + expression_infixe(...)
    s = s + ...
    if ... is not None:
        s = s + ... + ...
    return s

# ------------------------------ SUJET 22 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-22.pdf !

# Exercice 2 :

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

def est_parfait(mot):
    code_concatene = ""
    code_additionne = ...
    for c in mot:
        code_concatene = code_concatene + ...
        code_additionne = ...
    code_concatene = int(code_concatene)
    if ...:
        mot_est_parfait = True
    else:
        mot_est_parfait = False
    return code_additionne, code_concatene, mot_est_parfait

# ------------------------------ SUJET 23 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-23.pdf !

# Exercice 2 :

tab_a = [3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8, 8, 5, 5, 5]
tab_b = [8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3]
tab_c = [5, 5, 5, 1, 1, 1, 0, 0, 0, 6, 6, 6, 3, 8, 8, 8]

def trouver_intrus(tab, g, d):
    if g == d:
        return ...
    else:
        nombre_de_triplets = (d - g) // ...
        indice = g + 3 * (nombre_de_triplets // 2)
        if ...:
            return ...
        else:
            return ...

# ------------------------------ SUJET 24 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-24.pdf !

# Exercice 2 :

def fusion(lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    lst12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and ...:
        if lst1[i1] < lst2[i2]:
            lst12[i] = ...
            i1 = ...
        else:
            lst12[i] = lst2[i2]
            i2 = ...
        i += 1
    while i1 < n1:
        lst12[i] = ...
        i1 = i1 + 1
        i = ...
    while i2 < n2:
        lst12[i] = ...
        i2 = i2 + 1
        i = ...
    return lst12

# ------------------------------ SUJET 25 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-25.pdf !

# Exercice 2 :

class Arbre:

    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def parcours(arbre, liste):
    if arbre != None:
        parcours(arbre.fg, liste)
        liste.append(arbre.v)
        parcours(arbre.fd, liste)
    return liste

def insere(arbre, cle):
    if ...:
        if ...:
            insere(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if ...:
            insere(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)

# ------------------------------ SUJET 26 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-26.pdf !

# Exercice 2 :

def dichotomie(tab, x):
    debut = 0 
    fin = len(tab) - 1
    while debut <= fin:
        m = ...
        if x == tab[m]:
            return ...
        if x > tab[m]:
            debut = m + 1
        else:
             fin = ...			
    return ...

# ------------------------------ SUJET 27 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-27.pdf !

# Exercice 2 :

def separe(tab):
    gauche = 0
    droite = ...
    while gauche < droite:
        if tab[gauche] == 0:
            gauche = ...
        else:
            tab[gauche], tab[droite] = ...
            droite = ...
    return tab

# ------------------------------ SUJET 28 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-28.pdf !

# Exercice 2 :

def dichotomie(tab, x):
    if ...:
        return False, 1
    if (x < tab[0]) or ...:
        return False, 2
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = ...
        if x == tab[m]:
            return ...
        if x > tab[m]:
            debut = m + 1
        else:
            fin = ...			
    return ...

# ------------------------------ SUJET 29 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-29.pdf !

# Exercice 2 :

def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if ...:
        for i in range(indice):
            L[i] = ...
        L[...] = ...
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = ...
    else:
        for i in range(nbre_elts):
            L[i] = ...
        L[...] = ...
    return L

# ------------------------------ SUJET 30 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-30.pdf !

# Exercice 2 :

def binaire(a):
    bin_a = ...
    a = a // 2
    while a ...:
        bin_a = ... + bin_a
        a = ...
    return bin_a

# ------------------------------ SUJET 31 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-31.pdf !

# Exercice 2 :

def binaire(a):
    bin_a = str(...)
    a = a // 2
    while a ...:
        bin_a = ...(a % 2) + ...
        a = ...
    return bin_a

# ------------------------------ SUJET 32 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-32.pdf !

# Exercice 2 :

class Carte:

    def __init__(self, c, v):
        self.couleur = c
        self.valeur = v

    def get_valeur(self):
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def get_couleur(self):
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:

    def __init__(self):
        ...

    def get_carte(self, pos):
        ...

# ------------------------------ SUJET 33 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-33.pdf !

# Exercice 2 :

def tri_selection(tab):
    N = len(tab)
    for k in range(...):
        imin = ...
        for i in range(... , N):
            if tab[i] < ...:
                imin = i
        ..., tab[imin] = tab[imin], ...


# ------------------------------ SUJET 34 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-34.pdf !

# Exercice 2 :

def tri(tab):
    i = ...
    j = ...
    while i != j:
        if tab[i] == 0:
            i = ...
        else:
            valeur = tab[j]
            tab[j] = ...
            ...
            j = ...
    ...

# ------------------------------ SUJET 35 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-35.pdf !

# Exercice 2 :

c2 = [[1, 7], [7, 1]]
c3 = [[3, 4, 5], [4, 4, 4], [5, 4, 3]]
c3bis = [[2, 9, 4], [7, 0, 3], [6, 1, 8]]

class Carre:

    def __init__(self, liste, n):
        self.ordre = n
        self.tableau = [[liste[i + j * n] for i in range(n)] for j in range(n)]

    def affiche(self):
        for i in range(self.ordre):
            print(self.tableau[i])

    def somme_ligne(self, i):
        somme = 0
        for j in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def somme_col(self, j):
        somme = 0
        for i in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def est_semimagique(self):
        s = self.somme_ligne(0)
        for i in range(...):
            if ... != s:
                return ...
        for j in range(...):
            if ... != s:
                return ...
        return ...

# ------------------------------ SUJET 36 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-36.pdf !

# Exercice 2 :

def propager(M, i, j, val):
    if M[i][j] == ...:
        M[i][j] = val
    if i - 1 >= 0 and M[i - 1][j] == ...:
        propager(M, i - 1, j, val)
    if ... < len(M) and M[i + 1][j] == 1:
        propager(M, ..., j, val)
    if ... and M[i][j - 1] == 1:
        propager(M, ..., ..., val)
    if ... and ...:
        propager(..., ..., ..., ...)

# ------------------------------ SUJET 37 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-37.pdf !

# Exercice 2 :

class AdresseIP:

    def __init__(self, adresse):
        self.adresse = ...
   
    def liste_octet(self):
        return [int(i) for i in self.adresse.split(".")] 
        
    def est_reservee(self):
        return ... or ...
             
    def adresse_suivante(self):
        if ... < 254:
            octet_nouveau = ... + ...
            return AdresseIP('192.168.0.' + ...)
        else:
            return False

# ------------------------------ SUJET 38 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-38.pdf !

# Exercice 2 :

def est_cyclique(plan):
    expediteur = 'A'
    destinataire = plan[...]
    nb_destinaires = 1
    while destinataire != ...:
        destinataire = plan[...]
        nb_destinaires += ...
    return nb_destinaires == ...

# ------------------------------ SUJET 39 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-39.pdf !

# Exercice 2 :

def pantheon(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = ...
    for i in range(...):
        if notes[i] == ...:
            meilleurs_eleves.append(...)
        elif notes[i] > note_maxi:
            note_maxi = ...
            meilleurs_eleves = [...]
    return (note_maxi,meilleurs_eleves)

eleves_nsi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]

# ------------------------------ SUJET 40 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-40.pdf !

# Exercice 2 :

class Noeud:

    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None

    def getValeur(self):
        return self.valeur

    def droitExiste(self):
        return (self.droit is not None)

    def gaucheExiste(self):
        return (self.gauche is not None)

    def inserer(self, cle):
        if cle < ...:
            if self.gaucheExiste():
                ...
            else:
                self.gauche = ...
        elif cle > ...:
            if ...:
                ...
            else:
                ... = Noeud(cle)

arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)

# ------------------------------ SUJET 41 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-41.pdf !

# Exercice 2 :

valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return ...
    v = valeurs[rang]
    if v <= ...:
        return ... + rendu_glouton(a_rendre - v, rang)
    else:
        return rendu_glouton(a_rendre, ...)

# ------------------------------ SUJET 42 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-42.pdf !

# Exercice 2 :

from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, ...)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = ...

    while nb_mystere != ... and compteur < ...:
        compteur = compteur + ...
        if nb_mystere ... nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))
    if nb_mystere == nb_test:
        print("Bravo ! Le nombre etait ", ...)
        print("Nombre d'essais: ", ...)
    else:
        print("Perdu ! Le nombre etait ", ...)

# ------------------------------ SUJET 43 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-43.pdf !

# Exercice 2 :

def tri_bulles(T):
    n = len(T)
    for i in range(..., ..., -1):
        for j in range(i):
            if T[j] > T[...]:
                ... = T[j]
                T[j] = T[...]
                T[j + 1] = temp
    return T

# ------------------------------ SUJET 44 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-44.pdf !

# Exercice 2 :

def crible(n):
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(..., n):
        if tab[i] == ...:
            premiers.append(...)
            for multiple in range(2 * i, n, ...):
                tab[multiple] = ...
    return premiers

assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

# ------------------------------ SUJET 45 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 23-NSI-45.pdf !

# Exercice 2 :

def dec_to_bin (nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == ...:
        return str(r)
    else:
        return dec_to_bin(...) + ...

def bin_to_dec(nb_bin):
    if nb_bin == '0':
        return 0
    elif ...:
        return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = ...
        return ... * bin_to_dec(nb_bin[:-1]) + ...