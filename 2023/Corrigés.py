# BACCALAURÉAT GÉNÉRAL NSI TERMINALE - ÉPREUVE PRATIQUE - CORRIGÉS - SESSION 2023

# ------------------------------ SUJET 1 ------------------------------ #

# Exercice 1 :

def verifie(tab : list) -> bool:
    a = tab[0]
    for b in tab[1:]:
        if a > b:
            return False
        a = b
    return True

verifie([0, 5, 8, 8])
assert verifie([0, 5, 8, 8, 9]) == True
assert verifie([8, 12, 4]) == False
assert verifie([-1, 4]) == True
assert verifie([5]) == True

# Exercice 2 :

urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax:
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale

election = depouille(urne)
assert election == {'B': 4, 'A': 3, 'C': 3}
assert vainqueur(election) == ['B']
assert vainqueur({'B': 4, 'A': 4, 'C': 3}) in [['B', 'A'], ['A', 'B']]
assert vainqueur({'B': 3}) == ['B']
assert vainqueur({}) == []

# ------------------------------ SUJET 2 ------------------------------ #

# Exercice 1 :

def indices_maxi(tab : list) -> tuple:
    max = tab[0]
    indices = [0]
    for index in range(1, len(tab)):
        if max < tab[index]:
            max = tab[index]
            indices = [index]
        elif max == tab[index]:
            indices.append(index)
    return max, indices

assert indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, [3, 8])
assert indices_maxi([7]) == (7, [0])

# Exercice 2 :

def positif(pile):
    pile_1 = list(pile)
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1

assert positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]) == [0, 5, 4, 10, 9]
assert positif([-2]) == []

# ------------------------------ SUJET 3 ------------------------------ #

# Exercice 1 :

def moyenne(l : list) -> float:
    total, sum = 0, 0
    for value, coef in l:
        if value < 0 or coef < 0:
            return None
        sum += coef
        total += value * coef

    if sum:
        return total / sum
    else:
        return None

assert moyenne([(8, 1)]) == 8
assert moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]) == 9.142857142857142
assert moyenne([(3, 0), (5, 0)]) == None
assert moyenne([]) == None
assert moyenne([(-3, 2), (5, 2)]) == None

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
    liste_zoom = []
    for elt in liste_depart :
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom

def zoomDessin(grille, k):
    grille_zoom = []
    for elt in grille:
        liste_zoom = zoomListe(elt, k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom

affiche(coeur)
affiche(zoomDessin(coeur, 3))

# ------------------------------ SUJET 4 ------------------------------ #

# Exercice 1 :

def a_doublon(l : list):
    if len(l) > 1:
        n = l[0]
        for i in range(1, len(l)):
            if n == l[i]:
                return True
            else:
                n = l[i]
    return False

assert a_doublon([]) == False
assert a_doublon([1]) == False
assert a_doublon([1, 2, 4, 6, 6]) == True
assert a_doublon([2, 5, 7, 7, 7, 9]) == True
assert a_doublon([0, 2, 3]) == False

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
    voisins = voisinage(len(grille), ligne, colonne)
    for l, c in voisins:
        if grille[l][c] != -1:
            grille[l][c] += 1 

def génère_grille(bombes):
    n = len(bombes)
    grille = [[0 for colonne in range(n)] for ligne in range(n)]
    for ligne, colonne in bombes:
        grille[ligne][colonne] = -1 
        incrémente_voisins(grille, ligne, colonne)
    return grille

assert génère_grille([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]) == [[1, 1, 1, 0, 0], [1, -1, 1, 1, 1], [2, 2, 3, 2, -1], [1, -1, 2, -1, 3], [1, 1, 2, 2, -1]]

# ------------------------------ SUJET 5 ------------------------------ #

# Exercice 1 :

from random import randint

def lancer(n : int) -> list:
    l = []
    for i in range(n):
        l.append(randint(1, 6))
    return l

def paire_6(tab : list) -> bool:
    count = 0
    for item in tab:
        if item == 6:
            count += 1
    return count > 1

assert len(lancer(5)) == 5
assert len(lancer(3)) == 3
assert len(lancer(0)) == 0
assert paire_6([5, 6, 6, 2, 2]) == True
assert paire_6([6, 5, 1, 6, 6]) == True
assert paire_6([2, 2, 6]) == False
assert paire_6([]) == False

# Exercice 2 :

def nbLig(image):
    return len([x for x in image])

def nbCol(image):
    return len([x for x in image[0]])

def negatif(image):
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            L[i][j] = 255 - image[i][j]
    return L

def binaire(image, seuil):
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            if image[i][j] < seuil:
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L

img = [[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]

assert nbLig(img) == 4
assert nbCol(img) == 5
assert negatif(img) == [[235, 221, 1, 110, 249], [232, 131, 18, 30, 186], [58, 81, 48, 230, 168], [0, 255, 231, 58, 66]]
assert binaire(img,120) == [[0, 0, 1, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 0, 0, 1, 1]]

# ------------------------------ SUJET 6 ------------------------------ #

# Exercice 1 :

def recherche(tab : list, n : int) -> int:
    indice = -1
    for i in range(len(tab)):
        if tab[i] == n:
            indice = i
    if indice == -1:
        return len(tab)
    else:
        return indice

assert recherche([], 1) == 0
assert recherche([5, 3], 1) == 2
assert recherche([2, 4], 2) == 0
assert recherche([2, 3, 5, 2, 4], 2) == 3

# Exercice 2 :

from math import sqrt

def distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def plus_courte_distance(tab, depart):
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart) < distance(tab[i], point):
            point = tab[i]
            min_dist = distance(point, depart)
    return point

assert distance((1, 0), (1, 0)) == 0
assert distance((1, 0), (5, 3)) == 5.0
assert distance((1, 0), (0, 1)) == 1.4142135623730951
assert plus_courte_distance([(0, 0)], (0, 0)) == (0, 0)
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5)
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (5, 2)) == (5, 2)

# ------------------------------ SUJET 7 ------------------------------ #

# Exercice 1 :

def fusion(tab1 : list, tab2 : list) -> list:
    tab = []
    i1, i2 = 0, 0
    n1, n2 = len(tab1), len(tab2)
    while (i1 < n1) and (i2 < n2):
        if tab1[i1] <= tab2[i2]:
            tab.append(tab1[i1])
            i1 += 1
        else:
            tab.append(tab2[i2])
            i2 += 1
    for i in range(i1, n1):
        tab.append(tab1[i])
    for i in range(i2, n2):
        tab.append(tab2[i])
    return tab

assert fusion([], []) == []
assert fusion([3, 5], [2, 5]) == [2, 3, 5, 5]
assert fusion([-2, 4], [-3, 5, 10]) == [-3, -2, 4, 5, 10]
assert fusion([4], [2, 6]) == [2, 4, 6]

# Exercice 2 :

romains = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def traduire_romain(nombre):
    if len(nombre) == 1:
        return romains[nombre]
    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return -romains[nombre[0]] + traduire_romain(nombre[1:])

assert traduire_romain("XIV") == 14
assert traduire_romain("CXLII") == 142
assert traduire_romain("MMXXIII") == 2023

# ------------------------------ SUJET 8 ------------------------------ #

# Exercice 1 :

def max_dico(dico : dict) -> tuple:
    name, max = None, -1
    for key, value in dico.items():
        if max < value:
            name, max = key, value
    return name, max

assert max_dico({}) == (None, -1)
assert max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}) == ('Ada', 201)
assert max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}) == ('Alan', 222)
assert max_dico({'Alan': 222, 'Ada': 201, 'Eve': 222, 'Tim': 50}) in [('Eve', 222), ('Alan', 222)]

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
    for element in tab:
        if element != '+' and element != '*':
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return p.depiler()

assert eval_expression([2, 3, '+', 5, '*']) == 25
assert eval_expression([2, 3, '*', 5, '*']) == 30
assert eval_expression([2, 3, '+', 5, '+']) == 10
assert eval_expression([2, 3, '+', 5, '*', 5, '+', 6, '*']) == 180
assert eval_expression([]) == None

# ------------------------------ SUJET 9 ------------------------------ #

# Exercice 1 :

def multiplication(n1 : int, n2 : int) -> int:
    resultat = 0
    positif  = (n1 < 0 and n2 < 0) or (n1 >= 0 and n2 >= 0)
    if n1 < 0:
        n1 = -n1
    if n2 < 0:
        n2 = -n2
    for _ in range(n1):
        resultat += n2
    return resultat if positif else -resultat

assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(6, -2) == -12
assert multiplication(-2, 0) == 0
assert multiplication(0, -2) == 0

# Exercice 2 :

def chercher(tab, n, i, j):
    if i < 0 or j > len(tab):
        return None
    elif i > j:
        return None
    m = (i + j) // 2
    if tab[m] < n:
        return chercher(tab, n, m + 1, j)
    elif tab[m] > n:
        return chercher(tab, n, i, m - 1)
    else:
        return m

assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 10) == None
assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 5) == None
assert chercher([1, 5, 6, 6, 9, 12], 9, 0, 5) == 4
assert chercher([1, 5, 6, 6, 9, 12], 6, 0, 5) == 2

# ------------------------------ SUJET 10 ------------------------------ #

# Exercice 1 :

def maxliste(tab : list) -> int:
    max = tab[0]
    for t in tab:
        if t > max:
            max = t
    return max

assert maxliste([98, 12, 104, 23, 131, 9]) == 131
assert maxliste([-27, 24, -3, 15]) == 24

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
        if c == '(':
            p.empiler(c)
        elif c == ')':
            if p.est_vide():
                return False
            else:
                p.depiler()
    return p.est_vide()

assert parenthesage("") == True
assert parenthesage("((()())(()))") == True
assert parenthesage("())(()") == False
assert parenthesage("(())(()") == False

# ------------------------------ SUJET 11 ------------------------------ #

# Exercice 1 :

def convertir(tab):
    decimal = 0
    power = len(tab) - 1
    for t in tab:
        decimal += t * 2**power
        power -= 1
    return decimal

assert convertir([0]) == 0
assert convertir([1]) == 1
assert convertir([1, 1]) == 3
assert convertir([1, 0, 1, 0, 0, 1, 1]) == 83
assert convertir([1, 0, 0, 0, 0, 0, 1, 0]) == 130

# Exercice 2 :

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        j = i
        while j > 0 and valeur_insertion < tab[j - 1]:
            tab[j] = tab[j - 1]
            j = j - 1
        tab[j] = valeur_insertion
    return tab

assert tri_insertion([]) == []
assert tri_insertion([9]) == [9]
assert tri_insertion([9, 9]) == [9, 9]
assert tri_insertion([9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ------------------------------ SUJET 12 ------------------------------ #

# Exercice 1 :

class ABR:

    def __init__(self, g0, v0, d0):
        self.gauche = g0
        self.cle = v0
        self.droit = d0

    def __repr__(self):
        if self is None:
            return ''
        else:
            return '(' + (self.gauche).__repr__() + ',' + str(self.cle) + ',' +(self.droit).__repr__() + ')'

abr = ABR(ABR(None, 0, None), 1, ABR(None, 2, ABR(None, 3, None)))

def ajoute(cle, a):
    if a.cle > cle:
        if a.gauche is None:
            a.gauche = ABR(None, cle, None)
            return abr
        else:
            return ajoute(cle, a.gauche)
    elif a.cle < cle:
        if a.droit is None:
            a.droit = ABR(None, cle, None)
            return abr
        else:
            return ajoute(cle, a.droit)
    else:
        return abr

print(ajoute(4,abr))
print(ajoute(-5, abr))
print(ajoute(2, abr))

# Exercice 2 :

def empaqueter(liste_masses, c):
    n = len(liste_masses)
    nb_boites = 0
    boites = [0] * n
    for masse in liste_masses:
        i = 0
        while i <= nb_boites and boites[i] + masse > c:
            i = i + 1
        if i == nb_boites + 1:
            nb_boites += 1
        boites[i] = boites[i] + masse
    return nb_boites + 1

assert empaqueter([1, 5, 2], 5) == 2
assert empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11) == 5

# ------------------------------ SUJET 13 ------------------------------ #

# Exercice 1 :

from typing import Union

def recherche(a : Union[float, int], tab : list) -> int:
    occurrence = 0
    for t in tab:
        if t == a:
            occurrence += 1
    return occurrence

assert recherche(5, []) == 0
assert recherche(5, [-2, 3, 4, 8]) == 0
assert recherche(5, [-2, 3, 1, 5, 3, 7, 4]) == 1
assert recherche(5, [-2, 5, 3, 5, 4, 5]) == 3

# Exercice 2 :

pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):
    rendu = []
    a_rendre = somme_versee - somme_due
    i = len(pieces) - 1
    while a_rendre > 0 :
        if pieces[i] <= a_rendre:
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else :
            i = i - 1
    return rendu

assert rendu_monnaie(700, 700) == []
assert rendu_monnaie(102, 500) == [200, 100, 50, 20, 20, 5, 2, 1]
assert rendu_monnaie(0, 1) == [1]

# ------------------------------ SUJET 14 ------------------------------ #

# Exercice 1 :

def recherche(elt : int, tab : list) -> int:
    indice = 0
    for t in tab:
        if t == elt:
            return indice
        indice += 1
    return -1

assert recherche(1, [2, 3, 4]) == -1
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(50, [1, 50, 1]) == 1
assert recherche(15, [8, 9, 10, 15]) == 3
assert recherche(50, []) == -1
assert recherche(4, [2, 4, 4, 3, 4]) == 1

# Exercice 2 :

def insere(a, tab):
    l = list(tab)
    l.append(a)
    i = len(tab) - 1
    while a < l[i] and i >= 0:
      l[i + 1] = l[i]
      l[i] = a
      i = i - 1
    return l

assert insere(3, [1, 2, 4, 5]) == [1, 2, 3, 4, 5]
assert insere(30, [1, 2, 7, 12, 14, 25]) == [1, 2, 7, 12, 14, 25, 30]
assert insere(1, [2, 3, 4]) == [1, 2, 3, 4]
assert insere(1, []) == [1]

# ------------------------------ SUJET 15 ------------------------------ #

# Exercice 1 :

t_moy  = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def mini(releve : list, date : list) -> tuple:
    if len(releve) == 0 or len(releve) != len(date):
        return None
    indice = 0
    mini = t_moy[0]
    for i in range(1, len(releve)):
        if mini > releve[i]:
            mini = releve[i]
            indice = i
    return releve[indice], date[indice]

assert mini(t_moy, annees) == (12.5, 2016)

# Exercice 2 :

def inverse_chaine(chaine):
    result = ""
    for caractere in chaine:
       result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse == chaine

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)

assert inverse_chaine('bac') == 'cab'
assert inverse_chaine('baac') == 'caab'
assert inverse_chaine('a') == 'a'
assert inverse_chaine('') == ''

assert est_palindrome('NSI') == False
assert est_palindrome('ISN-NSI') == True

assert est_nbre_palindrome(214312) == False
assert est_nbre_palindrome(213312) == True

# ------------------------------ SUJET 16 ------------------------------ #

# Exercice 1 :

def recherche_indices_classement(elt : int, tab : list) -> tuple:
    tab1, tab2, tab3 = [], [], []
    for i in range(len(tab)):
        if tab[i] < elt:
            tab1.append(i)
        elif tab[i] == elt:
            tab2.append(i)
        else:
            tab3.append(i)
    return tab1, tab2, tab3

assert recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]) == ([0, 3, 7], [1, 6], [2, 4, 5])
assert recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]) == ([0, 2, 5], [], [1, 3, 4])
assert recherche_indices_classement(3, [1, 1, 1, 1]) == ([0, 1, 2, 3], [], [])
assert recherche_indices_classement(3, []) == ([], [], [])

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
                           'DS4':[15, 4]
                       }
            }

def moyenne(nom, dico_result):
    if nom in dico_result:
        notes = dico_result[nom]
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note, coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round(total_points / total_coefficients, 1)
    else:
        return -1

assert moyenne('Dupond', resultats) == -1
assert moyenne('Dupont', resultats) == 14.5
assert moyenne('Durand', resultats) == 9.2

# ------------------------------ SUJET 17 ------------------------------ #

# Exercice 1 :

def moyenne(liste_notes : list) -> float:
    total_note = 0
    total_coef = 0
    for note, coef in liste_notes:
        total_note += note * coef
        total_coef += coef
    return round(total_note / total_coef, 1) if total_coef else -1

assert moyenne([(15, 2)]) == 15
assert moyenne([(15, 2), (9, 1), (12, 3)]) == 12.5
assert moyenne([(15, 0), (9, 0), (12, 0)]) == -1
assert moyenne([]) == -1

# Exercice 2 :

def pascal(n):
    triangle = [[1]]
    for k in range(1, n + 1):
        ligne_k = [1]
        for i in range(1, k):
            ligne_k.append(triangle[k - 1][i - 1] + triangle[k - 1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle

assert pascal(0) == [[1]]
assert pascal(1) == [[1], [1, 1]]
assert pascal(2) == [[1], [1, 1], [1, 2, 1]]
assert pascal(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

# ------------------------------ SUJET 18 ------------------------------ #

# Exercice 1 :

def max_et_indice(tab : list) -> tuple:
    if len(tab) == 0:
        return None, -1
    indice = 0
    maxi = tab[indice]
    for i in range(len(tab)):
        if maxi < tab[i]:
            indice = i
            maxi = tab[indice]
    return maxi, indice

assert max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
assert max_et_indice([-2]) == (-2, 0)
assert max_et_indice([]) == (None, -1)
assert max_et_indice([-1, -1, 3, 3, 3]) == (3, 2)
assert max_et_indice([1, 1, 1, 1]) == (1, 0)

# Exercice 2 :

def est_un_ordre(tab):
    for i in range(1, len(tab) + 1):
        if i not in tab:
            return False
    return True

def nombre_points_rupture(ordre):
    assert est_un_ordre(ordre) == True
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: 
        nb = nb + 1
    i = 0
    while i < n - 1:
        if ordre[i] - ordre[i + 1] not in [-1, 1]:
            nb = nb + 1
        i = i + 1
    if ordre[n - 1] != n: 
        nb = nb + 1
    return nb

assert est_un_ordre([1, 6, 2, 8, 3, 7]) == False
assert est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]) == True

assert nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]) == 4
assert nombre_points_rupture([1, 2, 3, 4, 5]) == 0
assert nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5]) == 7
assert nombre_points_rupture([2, 1, 3, 4]) == 2

# ------------------------------ SUJET 19 ------------------------------ #

# Exercice 1 :

def recherche(tab : list, n : int) -> int:
    a, b = 0, len(tab) - 1
    while a <= b:
        m = (a + b) // 2
        if tab[m] < n:
            a = m + 1
        elif tab[m] > n:
            b = m - 1
        else:
            return m
    return -1

assert recherche([], 5) == -1
assert recherche([5], 5) == 0
assert recherche([2, 3, 4, 5, 6], 2) == 0
assert recherche([2, 3, 4, 5, 6], 6) == 4
assert recherche([2, 3, 4, 5, 6], 5) == 3
assert recherche([2, 3, 4, 6, 7], 5) == -1
assert recherche([2, 3, 4, 6], 4) == 2

# Exercice 2 :

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c) + decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + c
    return resultat

assert cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4) == 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
assert cesar(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4), -4)== 'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
assert cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5) == 'BONJOUR A TOUS. VIVE LA MATIERE NSI !'

# ------------------------------ SUJET 20 ------------------------------ #

# Exercice 1 :

def ajoute_dictionnaires(d1 : dict, d2 : dict) -> dict:
    d = d1
    for k, v in d2.items():
        if k in d:
            d[k] += v
        else:
            d[k] = v
    return d

assert ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}) == {1: 5, 2: 16, 3: 11}
assert ajoute_dictionnaires({}, {2: 9, 3: 11}) == {2: 9, 3: 11}
assert ajoute_dictionnaires({1: 5, 2: 7}, {}) == {1: 5, 2: 7}
assert ajoute_dictionnaires({1: 5, 2: 7}, {}) == {1: 5, 2: 7}
assert ajoute_dictionnaires({}, {}) == {}

# Exercice 2 :

from random import randint

def nbre_coups():
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < 12:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % 12
        if case_en_cours not in cases_vues:
            cases_vues.append(case_en_cours)
        n = n + 1
    return n

assert nbre_coups() >= 12

# ------------------------------ SUJET 21 ------------------------------ #

# Exercice 1 :

def delta(liste : list) -> list:
    if len(liste) == 0:
        return []
    l = [liste[0]]
    for i in range(0, len(liste) - 1):
        l += [liste[i + 1] - liste[i]]
    return l

assert delta([1000, 800, 802, 1000, 1003]) == [1000, -200, 2, 198, 3]
assert delta([1000, 1000, 1000, 1000]) == [1000, 0, 0, 0]
assert delta([42]) == [42]
assert delta([]) == []

# Exercice 2 :

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
    s = ''
    if e.gauche is not None:
        s = '(' + s + expression_infixe(e.gauche)
    s = s + str(e.valeur)
    if e.droit is not None:
        s = s + expression_infixe(e.droit) + ')'
    return s

e = Noeud(Noeud(Noeud(None, 3, None),
    '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))),
    '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))

assert expression_infixe(e) == '((3*(8+7))-(2+1))'

# ------------------------------ SUJET 22 ------------------------------ #

# Exercice 1 :

def liste_puissances(a : int, n : int) -> list:
    if n < 1:
        return []
    l = [a] * n
    for i in range(1, n):
        for j in range(i):
            l[i] *= a
    return l

def liste_puissances_borne(a : int, borne : int) -> list:
    l = []
    if a >= 2:
        i = 0
        puissances = liste_puissances(a, borne)
        while puissances[i] < borne:
            l.append(puissances[i])
            i += 1
    return l

assert liste_puissances(3, 0) == []
assert liste_puissances(3, 5) == [3, 9, 27, 81, 243]
assert liste_puissances(-2, 4) == [-2, 4, -8, 16]

assert liste_puissances_borne(2, 3) == [2]
assert liste_puissances_borne(1, 2) == []
assert liste_puissances_borne(2, 16) == [2, 4, 8]
assert liste_puissances_borne(2, 17) == [2, 4, 8, 16]
assert liste_puissances_borne(5, 5) == []

# Exercice 2 :

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

def est_parfait(mot):
    code_concatene = ""
    code_additionne = 0
    for c in mot:
        code_concatene = code_concatene + str(dico[c])
        code_additionne = code_additionne + dico[c]
    code_concatene = int(code_concatene)
    if code_concatene % code_additionne == 0:
        mot_est_parfait = True
    else:
        mot_est_parfait = False
    return code_additionne, code_concatene, mot_est_parfait

assert est_parfait("PAUL") == (50, 1612112, False)
assert est_parfait("ALAIN") == (37, 1121914, True)

# ------------------------------ SUJET 23 ------------------------------ #

# Exercice 1 :

animaux = [{'nom': 'Medor', 'espece': 'chien', 'age': 5, 'enclos': 2}, {'nom': 'Titine', 'espece': 'chat', 'age': 2, 'enclos': 5}, {'nom': 'Tom', 'espece': 'chat', 'age': 7, 'enclos': 4}, {'nom': 'Belle', 'espece': 'chien', 'age': 6, 'enclos': 3}, {'nom': 'Mirza', 'espece': 'chat', 'age': 6, 'enclos': 5}]

def selection_enclos(table_animaux : list, num_enclos : int) -> list:
    l = []
    for animal in animaux:
        if animal['enclos'] == num_enclos:
            l.append(animal)
    return l

assert selection_enclos(animaux, 5) == [{'nom': 'Titine', 'espece': 'chat', 'age': 2, 'enclos': 5}, {'nom': 'Mirza', 'espece': 'chat', 'age': 6, 'enclos': 5}]
assert selection_enclos(animaux, 2) == [{'nom': 'Medor', 'espece': 'chien', 'age': 5, 'enclos': 2}]
assert selection_enclos(animaux, 7) == []

# Exercice 2 :

tab_a = [3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8, 8, 5, 5, 5]
tab_b = [8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3]
tab_c = [5, 5, 5, 1, 1, 1, 0, 0, 0, 6, 6, 6, 3, 8, 8, 8]

def trouver_intrus(tab, g, d):
    if g == d:
        return tab[g]
    else:
        nombre_de_triplets = (d - g) // 3
        indice = g + 3 * (nombre_de_triplets // 2)
        if tab[indice] == tab[indice + 1]:
            return trouver_intrus(tab, g + 3, d)
        else:
            return trouver_intrus(tab, g, d - 3)

assert trouver_intrus([3, 3, 3, 1], 0, 3) == 1
assert trouver_intrus([1, 3, 3, 3], 0, 3) == 1
assert trouver_intrus([3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8, 8, 5, 5, 5], 0, 21) == 7
assert trouver_intrus([8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3], 0, 12) == 8
assert trouver_intrus([5, 5, 5, 1, 1, 1, 0, 0, 0, 6, 6, 6, 3, 8, 8, 8], 0, 15) == 3

# ------------------------------ SUJET 24 ------------------------------ #

# Exercice 1 :

def nbr_occurrences(chaîne : str) -> dict:
    dico = {}
    for c in chaîne:
        if c in dico:
            dico[c] += 1
        else:
            dico[c] = 1
    return dico

assert nbr_occurrences('') == {}
assert nbr_occurrences('Hello world !') == {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'w': 1, 'r': 1, 'd': 1, '!': 1}

# Exercice 2 :

def fusion(lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    lst12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:
            lst12[i] = lst1[i1]
            i1 = i1 + 1
        else:
            lst12[i] = lst2[i2]
            i2 = i2 + 1
        i += 1
    while i1 < n1:
        lst12[i] = lst1[i1]
        i1 = i1 + 1
        i = i + 1
    while i2 < n2:
        lst12[i] = lst2[i2]
        i2 = i2 + 1
        i = i + 1
    return lst12

assert fusion([], []) == []
assert fusion([1], []) == [1]
assert fusion([], [1]) == [1]
assert fusion([1], [2]) == [1, 2]
assert fusion([2], [1]) == [1, 2]
assert fusion([1, 6, 10], [0, 7, 8, 9]) == [0, 1, 6, 7, 8, 9, 10]

# ------------------------------ SUJET 25 ------------------------------ #

# Exercice 1 :

def enumere(L : list) -> dict:
    d = {}
    i = 0
    for l in L:
        if l in d:
            d[l] = d[l] + [i]
        else:
            d[l] = [i]
        i += 1
    return d

assert enumere([]) == {}
assert enumere([1]) == {1: [0]}
assert enumere([1, 1, 2, 3, 2, 1]) == {1: [0, 1, 5], 2: [2, 4], 3: [3]}

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
    if cle < arbre.v:
        if arbre.fg is not None:
            insere(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if arbre.fd is not None:
            insere(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)

a = Arbre(5)
insere(a, 2)
insere(a, 3)
insere(a, 7)
l = []
assert parcours(a, l) == [2, 3, 5, 7]

# ------------------------------ SUJET 26 ------------------------------ #

# Exercice 1 :

def multiplication(n1 : int, n2 : int) -> int:
    resultat = 0
    positif = (n1 < 0 and n2 < 0) or (n1 >= 0 and n2 >= 0)
    if n1 < 0:
        n1 = -n1
    if n2 < 0:
        n2 = -n2
    for _ in range(n1):
        resultat += n2
    return resultat if positif else -resultat

assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(6, -2) == -12
assert multiplication(-2, 0) == 0
assert multiplication(0, -2) == 0

# Exercice 2 :

def dichotomie(tab, x):
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
             fin = m - 1
    return False

assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) == True
assert dichotomie([15], 15) == True
assert dichotomie([15, 16], 15) == True
assert dichotomie([15, 16], 16) == True
assert dichotomie([], 15) == False
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27) == False

# ------------------------------ SUJET 27 ------------------------------ #

# Exercice 1 :

def recherche_min(tab : list) -> int:
    indice = 0
    mini = tab[indice]
    for i in range(1, len(tab)):
        if mini > tab[i]:
            indice = i
            mini = tab[indice]
    return indice

assert recherche_min([5]) == 0
assert recherche_min([2, 4, 1]) == 2
assert recherche_min([5, 3, 2, 2, 4]) == 2

# Exercice 2 :

def separe(tab):
    gauche = 0
    droite = len(tab) - 1
    while gauche < droite:
        if tab[gauche] == 0:
            gauche = gauche + 1
        else:
            tab[gauche], tab[droite] = tab[droite], tab[gauche]
            droite = droite - 1
    return tab

assert separe([0]) == [0]
assert separe([1]) == [1]
assert separe([1, 0]) == [0, 1]
assert separe([0, 1]) == [0, 1]
assert separe([1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]
assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# ------------------------------ SUJET 28 ------------------------------ #

# Exercice 1 :

def moyenne(tab):
    return sum(tab) / len(tab)

assert moyenne([1]) == 1
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4
assert moyenne([1, 2]) == 1.5

# Exercice 2 :

def dichotomie(tab, x):
    if len(tab) == 0:
        return False, 1
    if (x < tab[0]) or (x < tab[0]):
        return False, 2
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False, 3

assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27) == (False, 3)
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1) == (False, 2)
assert dichotomie([], 28) == (False, 1)
assert dichotomie([1], 0) == (False, 2)
assert dichotomie([1], 2) == (False, 3)

# ------------------------------ SUJET 29 ------------------------------ #

# Exercice 1 :

class Arbre:

    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def taille(a : Arbre) -> int:
    if a is None:
        return 0
    if (a.fg is None) and (a.fd is None):
        return 1
    else:
        return 1 + taille(a.fg) + taille(a.fd)

a = Arbre(1)
a.fg = Arbre(4)
a.fd = Arbre(0)
a.fd.fd = Arbre(7)

assert taille(None) == 0
assert taille(Arbre(1)) == 1
assert taille(a) == 4

def hauteur(a : Arbre) -> int:
    if a is None:
        return 0
    if (a.fg is None) and (a.fd is None):
        return 1
    else:
        return 1 + max(hauteur(a.fg), hauteur(a.fd))

assert hauteur(None) == 0
assert hauteur(Arbre(1)) == 1
assert hauteur(a) == 3

a = Arbre(0)
a.fg = Arbre(1)
a.fg.fg = Arbre(3)
a.fd = Arbre(2)
a.fd.fg = Arbre(4)
a.fd.fg.fd = Arbre(6)
a.fd.fd = Arbre(5)

assert taille(a) == 7
assert hauteur(a) == 4

# Exercice 2 :

def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if indice < nbre_elts:
        for i in range(indice):
            L[i] = liste[i]
        L[indice] = element
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = liste[i - 1]
    else:
        for i in range(nbre_elts):
            L[i] = liste[i]
        L[nbre_elts] = element
    return L

assert ajoute(1, 4, [7, 8, 9]) == [7, 4, 8, 9]
assert ajoute(3, 4, [7, 8, 9]) == [7, 8, 9, 4]
assert ajoute(4, 4, [7, 8, 9]) == [7, 8, 9, 4]

# ------------------------------ SUJET 30 ------------------------------ #

# Exercice 1 :

def moyenne(tab : list) -> float:
    return sum(tab) / len(tab)

assert moyenne([1.0]) == 1.0
assert moyenne([1.0, 2.0, 4.0]) == 2.3333333333333335

# Exercice 2 :

def binaire(a):
    bin_a = str(a % 2)
    a = a // 2
    while a != 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a

assert binaire(83) == '1010011'
assert binaire(127) == '1111111'
assert binaire(0) == '0'
assert binaire(1) == '1'
assert binaire(2) == '10'

# ------------------------------ SUJET 31 ------------------------------ #

# Exercice 1 :

def nb_repetitions(elt : int, tab : list):
    occurrence = 0
    for t in tab:
        if t == elt:
            occurrence += 1
    return occurrence

assert nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]) == 3
assert nb_repetitions('A', [ 'B', 'A', 'B', 'A', 'R']) == 2
assert nb_repetitions(12, [1, '! ', 7, 21, 36, 44]) == 0

# Exercice 2 :

def binaire(a):
    bin_a = str(a % 2)
    a = a // 2
    while a != 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a

assert binaire(83) == '1010011'
assert binaire(127) == '1111111'
assert binaire(0) == '0'
assert binaire(1) == '1'
assert binaire(2) == '10'

# ------------------------------ SUJET 32 ------------------------------ #

# Exercice 1 :

def min_et_max(tab : list) -> dict:
    min = tab[0]
    max = tab[0]
    for t in tab:
        if min > t:
            min = t
        elif max < t:
            max = t
    return {'min': min, 'max': max}

assert min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
assert min_et_max([0, 1, 2, 3]) == {'min': 0, 'max': 3}
assert min_et_max([3]) == {'min': 3, 'max': 3}
assert min_et_max([1, 3, 2, 1, 3]) == {'min': 1, 'max': 3}
assert min_et_max([-1, -1, -1, -1, -1]) == {'min': -1, 'max': -1}

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
        self.cartes = []
        for couleur in range(1, 5):
            for valeur in range(1, 14):
                self.cartes.append(Carte(couleur, valeur))

    def get_carte(self, pos):
        if 51 < pos or pos < 0:
            raise AssertionError('paramètre pos invalide')
        return self.cartes[pos]

jeu = Paquet_de_cartes()
assert jeu.get_carte(0).get_valeur() == 'As'
assert jeu.get_carte(10).get_valeur() == 'Valet'
assert jeu.get_carte(10).get_couleur() == 'pique'

carte1 = jeu.get_carte(20)
assert carte1.get_valeur() + " de " + carte1.get_couleur() == '8 de coeur'
carte2 = jeu.get_carte(0)
assert carte2.get_valeur() + " de " + carte2.get_couleur() == 'As de pique'
jeu.get_carte(52)

# ------------------------------ SUJET 33 ------------------------------ #

# Exercice 1 :

def taille(arbre : dict, lettre : str) -> int:
    if lettre == '':
        return 0
    if arbre[lettre][0] == '' and arbre[lettre][1] == '':
        return 1
    return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])

a = {'F': ['B','G'], 'B': ['A','D'], 'A': ['',''], 'D': ['C','E'], 'C': ['',''], 'E': ['',''], 'G': ['','I'], 'I': ['','H'], 'H': ['','']}

assert taille(a, 'F') == 9

# Exercice 2 :

def tri_selection(tab):
    N = len(tab)
    for k in range(N):
        imin = k
        for i in range(imin + 1, N):
            if tab[i] < tab[imin]:
                imin = i
        tab[k], tab[imin] = tab[imin], tab[k]
    return tab

liste = [41, 55, 21, 18, 12, 6, 25]
tri_selection(liste)
assert liste == [6, 12, 18, 21, 25, 41, 55]

# ------------------------------ SUJET 34 ------------------------------ #

# Exercice 1 :

def moyenne(tab : list) -> float:
    total = 0
    for t in tab:
        total += t
    return total / len(tab) if len(tab) else None

assert moyenne([5]) == 5
assert moyenne([0, 1]) == 0.5
assert moyenne([5, 3, 8]) == 5.333333333333333
assert moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5
assert moyenne([]) == None

# Exercice 2 :

def tri(tab):
    i = 0
    j = len(tab) - 1
    while i != j:
        if tab[i] == 0:
            i = i + 1
        else:
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j = j - 1
    return tab

assert tri([0, 1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 0, 1, 1, 1, 1]
assert tri([0]) == [0]
assert tri([1]) == [1]
assert tri([0, 1]) == [0, 1]
assert tri([1, 0]) == [0, 1]

# ------------------------------ SUJET 35 ------------------------------ #

# Exercice 1 :

def ou_exclusif(tab1 : list, tab2 : list) -> list:
    if len(tab1) != len(tab2):
        return []
    for i in range(len(tab1)):
        if tab1[i] == tab2[i]:
            tab1[i] = 0
        else:
            tab1[i] += tab2[i]
    return tab1

a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]

assert ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]) == [1, 1, 0, 1, 1, 0, 0, 1]
assert ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1]) == [1, 1, 1, 0]
assert ou_exclusif([0, 0, 1, 1], [0, 1, 0, 1]) == [0, 1, 1, 0]
assert ou_exclusif([0, 1], [0]) == []

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
        for i in range(1, self.ordre):
            if self.somme_ligne(i) != s:
                return False
        for j in range(self.ordre):
            if self.somme_col(i) != s:
                return False
        return True

c2 = Carre((1, 7, 7, 1), 2)
assert c2.est_semimagique()
c3 = Carre((3, 4, 5, 4, 4, 4, 5, 4, 3), 3)
assert c3.est_semimagique()
c3.affiche()
c3bis = Carre((2, 9, 4, 7, 0, 3, 6, 1, 8), 3)
assert not c3bis.est_semimagique()

# ------------------------------ SUJET 36 ------------------------------ #

# Exercice 1 :

def couples_consecutifs(tab : list) -> list:
    if len(tab) < 2:
        return []
    l = []
    for i in range(len(tab) - 1):
        a, b = tab[i], tab[i + 1]
        if (a == b - 1) and (a < b):
            l.append((a, b))
    return l

assert couples_consecutifs([]) == []
assert couples_consecutifs([1]) == []
assert couples_consecutifs([1, 1]) == []
assert couples_consecutifs([1, 2]) == [(1,2)]
assert couples_consecutifs([1, 4, 3, 5]) == []
assert couples_consecutifs([1, 4, 5, 3]) == [(4, 5)]
assert couples_consecutifs([1, 1, 2, 4]) == [(1, 2)]
assert couples_consecutifs([7, 1, 2, 5, 3, 4]) == [(1, 2), (3, 4)]
assert couples_consecutifs ([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)]

# Exercice 2 :

def propager(M, i, j, val):
    if M[i][j] == 1:
        M[i][j] = val
    if i - 1 >= 0 and M[i - 1][j] == 1:
        propager(M, i - 1, j, val)
    if i + 1 < len(M) and M[i + 1][j] == 1:
        propager(M, i + 1, j, val)
    if j - 1 >= 0 and M[i][j - 1] == 1:
        propager(M, i, j - 1, val)
    if j + 1 < len(M[0]) and M[i][j + 1] == 1:
        propager(M, i, j + 1, val)
    return M

assert propager([[0, 0, 1], [0, 1, 0], [1, 1, 1], [0, 1, 1]], 2, 1, 3) == [[0, 0, 1], [0, 3, 0], [3, 3, 3], [0, 3, 3]]
assert propager([[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]], 2, 1, 3) == [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]

# ------------------------------ SUJET 37 ------------------------------ #

# Exercice 1 :

def recherche(elt : int, tab : list) -> int:
    indice = -1
    for i in range(len(tab)):
        if tab[i] == elt:
            indice = i
    return indice

assert recherche(1, [2, 3, 4]) == -1
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(1, [1, 0, 42, 7]) == 0
assert recherche(1, [1, 50, 1]) == 2
assert recherche(1, [8, 1, 10, 1, 7, 1, 8]) == 5

# Exercice 2 :

class AdresseIP:

    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octet(self):
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        return self.adresse == '192.168.0.255' or self.adresse == '192.168.0.0'

    def adresse_suivante(self):
        if int(self.adresse.split('.')[3]) < 254:
            octet_nouveau = int(self.adresse.split('.')[3]) + 1
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False

assert AdresseIP('192.168.0.1').est_reservee() == False
assert AdresseIP('192.168.0.0').est_reservee() == True
assert AdresseIP('192.168.0.255').est_reservee() == True
assert AdresseIP('192.168.0.2').adresse_suivante().adresse == '192.168.0.3'
assert AdresseIP('192.168.0.253').adresse_suivante().adresse == '192.168.0.254'
assert AdresseIP('192.168.0.254').adresse_suivante() == False

# ------------------------------ SUJET 38 ------------------------------ #

# Exercice 1 :

def correspond(mot : str, mot_a_trous : str) -> bool:
    if len(mot) != len(mot_a_trous):
        return False
    for i in range(len(mot)):
        if mot[i] != mot_a_trous[i] and mot_a_trous[i] != '*':
            return False
    return True

assert correspond('INFORMATIQUE', 'INFO*MA*IQUE') == True
assert correspond('AUTOMATIQUE', 'INFO*MA*IQUE') == False
assert correspond('STOP', 'S*') == False
assert correspond('AUTO', '*UT*') == True

# Exercice 2 :

def est_cyclique(plan):
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinaires = 1
    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinaires += 1
    return nb_destinaires == len(plan)

assert est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'}) == False
assert est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F', 'D':'A'}) == True
assert est_cyclique({'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F', 'D':'E'}) == True
assert est_cyclique({'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F', 'D':'E'}) == False

# ------------------------------ SUJET 39 ------------------------------ #

# Exercice 1 :

def fibonacci(n : int) -> int:
    if n < 1:
        return None
    suite = [0] * (n + 1)
    for i in range(1, n + 1):
        if i < 3:
            suite[i] = 1
        else:
            suite[i] = suite[i - 1] + suite[i - 2]
    return suite[n]

assert fibonacci(0) == None
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
assert fibonacci(7) == 13
assert fibonacci(8) == 21
assert fibonacci(25) == 75025
assert fibonacci(45) == 1134903170

# Exercice 2 :

def pantheon(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []
    for i in range(len(notes)):
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]
    return (note_maxi, meilleurs_eleves)

assert pantheon(['a'], [24]) == (24, ['a'])
assert pantheon(['a','b','c','d','e','f','g','h','i','j'], [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]) == (80, ['c', 'f', 'h'])
assert pantheon([],[]) == (0, [])

# ------------------------------ SUJET 40 ------------------------------ #

# Exercice 1 :

def nombre_de_mots(phrase : str) -> int:
    nb_mots = 0
    for caractere in phrase:
        if caractere == ' ' or caractere == '.':
            nb_mots += 1
    return nb_mots

assert nombre_de_mots('') == 0
assert nombre_de_mots('Cet exercice est simple.') == 4
assert nombre_de_mots('Le point d exclamation est separe !') == 6
assert nombre_de_mots('Combien de mots y a t il dans cette phrase ?') == 10
assert nombre_de_mots('Fin.') == 1

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
        if cle < self.valeur:
            if self.gaucheExiste():
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        elif cle > self.valeur:
            if self.droitExiste():
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)

arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)

assert arbre.gauche.getValeur() == 3
assert arbre.droit.getValeur() == 9
assert arbre.gauche.gauche.getValeur() == 1
assert arbre.gauche.droit.getValeur() == 6

# ------------------------------ SUJET 41 ------------------------------ #

# Exercice 1 :

def recherche(caractere : str, chaine : str) -> int:
    occurrences = 0
    for c in chaine:
        if c == caractere:
            occurrences += 1
    return occurrences

assert recherche('e', "sciences") == 2
assert recherche('i', "mississippi") == 4
assert recherche('a', "mississippi") == 0
assert recherche('a', "") == 0
assert recherche('', "mississippi") == 0

# Exercice 2 :

valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre:
        return [valeurs[rang]] + rendu_glouton(a_rendre - v, rang)
    else :
        return rendu_glouton(a_rendre, rang + 1)

assert rendu_glouton(67, 0) == [50, 10, 5, 2]
assert rendu_glouton(291, 0) == [100, 100, 50, 20, 20, 1]
assert rendu_glouton(291, 1) == [50, 50, 50, 50, 50, 20, 20, 1]

# ------------------------------ SUJET 42 ------------------------------ #

# Exercice 1 :

def tri_selection(tab : list) -> list:
    if len(tab) == 0:
        return []
    for i in range(len(tab) - 1):
        indice = i
        mini = tab[indice]
        for k in range(indice + 1, len(tab)):
            if tab[k] < mini:
                indice = k
                mini = tab[indice]
        tab[i], tab[indice] = tab[indice], tab[i]
    return tab

assert tri_selection([1, 52, 6, -9, 12]) == [-9, 1, 6, 12, 52]
assert tri_selection([1]) == [1]
assert tri_selection([1, 2]) == [1, 2]
assert tri_selection([2, 1]) == [1, 2]
assert tri_selection([]) == []

# Exercice 2 :

from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1
    while nb_mystere != nb_test and compteur < 11:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))
    if nb_mystere == nb_test:
        print("Bravo ! Le nombre etait ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre etait ", nb_mystere)

plus_ou_moins()

# ------------------------------ SUJET 43 ------------------------------ #

# Exercice 1 :

def ecriture_binaire_entier_positif(n):
    if n == 0:
        return [0]
    b = []
    bits = 0
    while n != 0:
        b = [n % 2] + b
        bits += 1
        n = n // 2
    return b

assert ecriture_binaire_entier_positif(0) == [0]
assert ecriture_binaire_entier_positif(2) == [1, 0]
assert ecriture_binaire_entier_positif(105) == [1, 1, 0, 1, 0, 0, 1]

# Exercice 2 :

def tri_bulles(T):
    n = len(T)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if T[j] > T[j + 1]:
                temp = T[j]
                T[j] = T[j + 1]
                T[j + 1] = temp
    return T

assert tri_bulles([]) == []
assert tri_bulles([7]) == [7]
assert tri_bulles([9, 3, 7, 2, 3, 1, 6]) == [1, 2, 3, 3, 6, 7, 9]
assert tri_bulles([9, 7, 4, 3]) == [3, 4, 7, 9]

# ------------------------------ SUJET 44 ------------------------------ #

# Exercice 1 :

def renverse(mot : str) -> str:
    s = ""
    for i in range(len(mot) - 1, -1, -1):
        s += mot[i]
    return s

assert renverse("informatique") == "euqitamrofni"
assert renverse("i") == "i"
assert renverse("") == ""

# Exercice 2 :

def crible(n):
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(2, n):
        if tab[i] == True:
            premiers.append(i)
            for multiple in range(2 * i, n, i):
                tab[multiple] = False
    return premiers

assert crible(2) == []
assert crible(3) == [2]
assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

# ------------------------------ SUJET 45 ------------------------------ #

# Exercice 1 :

def rangement_valeurs(notes_eval : list) -> list:
    valeurs = []
    for i in range(11):
        total = 0
        for note in notes_eval:
            if i == note:
                total += 1
        valeurs.append(total)
    return valeurs

def notes_triees(effectifs : list) -> list:
    notes = []
    for i in range(len(effectifs)):
        for j in range(effectifs[i]):
            notes.append(i)
    return notes

notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]
assert rangement_valeurs(notes_eval) == [2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1]
assert notes_triees(rangement_valeurs(notes_eval)) == [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10]

# Exercice 2 :

def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)

def bin_to_dec(nb_bin):
    if nb_bin == '0':
        return 0
    elif nb_bin == '1':
        return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit

assert dec_to_bin(0) == '0'
assert dec_to_bin(1) == '1'
assert dec_to_bin(2) == '10'
assert dec_to_bin(25) == '11001'
assert bin_to_dec('0') == 0
assert bin_to_dec('1') == 1
assert bin_to_dec('10') == 2
assert bin_to_dec('101010') == 42
assert dec_to_bin(bin_to_dec('10101011010100011010')) == '10101011010100011010'
assert bin_to_dec(dec_to_bin(1266673211115978899834)) == 1266673211115978899834