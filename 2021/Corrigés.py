# BACCALAURÉAT GÉNÉRAL NSI TERMINALE - ÉPREUVE PRATIQUE - CORRIGÉS - SESSION 2021

# ------------------------------ SUJET 1 ------------------------------ #

# Exercice 1 :

def recherche(tab : list, n : int) -> int:
    for i in range(len(tab) - 1, -1, -1):
        if tab[i] == n:
            return i
    return len(tab)

assert recherche([5, 3], 1) == 2
assert recherche([2, 4], 2) == 0
assert recherche([2, 3, 5, 2, 4], 2) == 3
assert recherche([], 2) == 0

# Exercice 2 :

from math import sqrt

def distance(point1 : tuple, point2 : tuple ) -> float:
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

assert distance((0, 0), (0, 0)) == 0
assert distance((0, 0), (1, 1)) == sqrt(2)
assert distance((0, 0), (1, -1)) == sqrt(2)
assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"

def plus_courte_distance(tab : list, depart : tuple) -> tuple:
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(point, depart)
    return point

assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5)
assert plus_courte_distance([(7, 9), (2, 5), (5, 2), (-1, -1)], (0, 0)) == (-1, -1)

# ------------------------------ SUJET 2 ------------------------------ #

# Exercice 1 :

def moyenne(tab : list) -> float:
    total = 0
    for i in tab:
        total += i
    return total / len(tab) if len(tab) else None

assert moyenne([5,3,8]) == 5.333333333333333
assert moyenne([1,2,3,4,5,6,7,8,9,10]) == 5.5
assert moyenne([]) == None

# Exercice 2 :

def tri(tab : list) -> list:
    i = 0
    j = len(tab) - 1
    while i != j:
        if tab[i] == 0:
            i = i + 1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j = j - 1
    return tab

assert tri([0,1,0,1,0,1,0,1,0]) == [0, 0, 0, 0, 0, 1, 1, 1, 1]
assert tri([0,0,0]) == [0, 0, 0]
assert tri([1,1]) == [1, 1]
assert tri([1]) == [1]

# ------------------------------ SUJET 3 ------------------------------ #

# Exercice 1 :

def multiplication(n1 : int, n2 : int) -> int:
    total = 0
    for i in range(abs(n1)):
        total += abs(n2)
    if (n1 < 0 and n2 < 0) or (n1 > 0 and n2 > 0):
        return total
    else:
        return -total

assert multiplication(3,5) == 15
assert multiplication(-4,-8) == 32
assert multiplication(-2,6) == -12
assert multiplication(-2,0) == 0

# Exercice 2 :

def dichotomie(tab : list, x : int) -> bool:
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

assert dichotomie([], 1) == False
assert dichotomie([1, 3], 1) == True
assert dichotomie([1, 3], 3) == True
assert dichotomie([1, 2, 3], 2) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27) == False

# ------------------------------ SUJET 4 ------------------------------ #

# Exercice 1 :

def moyenne(tab : list) -> float:
    total = 0
    for i in tab:
        total += i
    return total / len(tab) if len(tab) else None

assert moyenne([]) == None
assert moyenne([1]) == 1
assert moyenne([1,2,3,4,5,6,7]) == 4
assert moyenne([1,2]) == 1.5

# Exercice 2 :

def dichotomie(tab : list, x : int):
    if len(tab) == 0:
        return False, 1
    if (x < tab[0]) or (x > tab[len(tab) - 1]):
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

assert dichotomie([], 1) == (False, 1)
assert dichotomie([1, 3], 1) == True
assert dichotomie([1, 3], 3) == True
assert dichotomie([1, 2, 3], 2) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27) == (False, 3)
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1) == (False, 2)

# ------------------------------ SUJET 5 ------------------------------ #

# Exercice 1 :

def convertir(T : list) -> int:
    total = 0
    pow = 0
    for i in T[::-1]:
        total += i * 2**pow
        pow += 1
    return total

assert convertir([0]) == 0
assert convertir([1, 0, 1, 0, 0, 1, 1]) == 83
assert convertir([1, 0, 0, 0, 0, 0, 1, 0]) == 130

# Exercice 2 :

def tri_insertion(L : list) -> list:
    n = len(L)
    if n == 0:
        return L
    for j in range(1, n):
        e = L[j]
        i = j
        while  i > 0 and L[i - 1] > L[j]:
            i = i - 1
        if i != j:
            for k in range(j, i, -1):
                L[k] = L[k - 1]
            L[i] = e
    return L

assert tri_insertion([]) == []
assert tri_insertion([0]) == [0]
assert tri_insertion([0,1,2,3]) == [0,1,2,3]
assert tri_insertion([3,2,1,0]) == [0,1,2,3]
assert tri_insertion([2,5,-1,7,0,28]) == [-1, 0, 2, 5, 7, 28]
assert tri_insertion([10,9,8,7,6,5,4,3,2,1,0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ------------------------------ SUJET 6 ------------------------------ #

# Exercice 1 :

def rendu(somme_a_rendre : int) -> list:
    n = [0, 0, 0]
    i = 0
    billets = [5, 2, 1]
    for b in billets:
        while somme_a_rendre >= b:
            somme_a_rendre -= b
            n[i] += 1
        i += 1
    return n

assert rendu(0) == [0,0,0]
assert rendu(3) == [0,1,1]
assert rendu(13) == [2,1,1]
assert rendu(64) == [12,2,0]
assert rendu(89) == [17,2,0]
assert rendu(88) == [17,1,1]

# Exercice 2 :

class Maillon :

    def __init__(self, v):
        self.valeur = v
        self.suivant = None

class File :

    def __init__(self):
        self.dernier_file = None

    def enfile(self, element):
        nouveau_maillon = Maillon(element)
        if self.dernier_file != None:
            nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = nouveau_maillon

    def est_vide(self):
        return self.dernier_file == None

    def affiche(self):
        file = []
        maillon = self.dernier_file
        while maillon != None:
            file.append(maillon.valeur)
            maillon = maillon.suivant
        return file

    def defile(self):
        if not self.est_vide():
            if self.dernier_file.suivant == None:
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.dernier_file
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = maillon.suivant.valeur
            maillon.suivant = None
            return resultat
        return None

F = File()
assert F.est_vide() == True
F.enfile(2)
assert F.affiche() == [2]
assert F.est_vide() == False
F.enfile(5)
F.enfile(7)
assert F.affiche() == [7, 5, 2]
assert F.defile() == 2
assert F.defile() == 5
assert F.affiche() == [7]
assert F.defile() == 7
assert F.defile() == None
assert F.affiche() == []

# ------------------------------ SUJET 7 ------------------------------ #

# Exercice 1 :

def fibonnaci_dynamique_desc(n : int) -> int:
    if type(n) is not int or n < 0:
        return None

    def fibonacci(n : int, table : list) -> int:
        if table[n] == None:
            if n < 2:
                table[n] = n
            else:
                table[n] = fibonacci(n - 1, table) + fibonacci(n - 2, table)
        return table[n]
    table = [None] * (n + 1)
    return fibonacci(n, table)

# OU

def fibonnaci_dynamique_asc(n : int) -> int:
    if type(n) is not int or n < 0:
        return None
    f = [0, 1]
    for i in range(1, n):
        f.append(f[i] + f[i - 1])
    return f[n]

assert fibonnaci_dynamique_desc(1) == 1
assert fibonnaci_dynamique_desc(2) == 1
assert fibonnaci_dynamique_desc(25) == 75025
assert fibonnaci_dynamique_desc(45) == 1134903170

assert fibonnaci_dynamique_asc(1) == 1
assert fibonnaci_dynamique_asc(2) == 1
assert fibonnaci_dynamique_asc(25) == 75025
assert fibonnaci_dynamique_asc(45) == 1134903170

# Exercice 2 :

def meilleures_notes(liste_eleves : list, liste_notes : list) -> tuple:
    note_maxi = 0
    nb_eleves_note_maxi = 0
    liste_maxi = []
    for compteur in range(len(liste_notes)):
        if liste_notes[compteur] == note_maxi:
            nb_eleves_note_maxi = nb_eleves_note_maxi + 1
            liste_maxi.append(liste_eleves[compteur])
        if liste_notes[compteur] > note_maxi:
            note_maxi = liste_notes[compteur]
            nb_eleves_note_maxi = 1
            liste_maxi = [liste_eleves[compteur]]
    return (note_maxi, nb_eleves_note_maxi, liste_maxi)

liste_eleves = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
liste_notes = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24]

assert meilleures_notes(liste_eleves, liste_notes) == (80, 3, ['c', 'f', 'h'])

# ------------------------------ SUJET 8 ------------------------------ #

# Exercice 1 :

def recherche(caractere : str, mot : str) -> int:
    total = 0
    for lettre in mot:
        if lettre == caractere:
            total += 1
    return total

assert recherche('e', "sciences") == 2
assert recherche('i', "mississippi") == 4
assert recherche('a', "mississippi") == 0

# Exercice 2 :

Pieces = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(pieces : list, arendre : int, solution : list = [], i : int = 0) -> list:
    if arendre == 0:
        return solution
    p = pieces[i]
    if p <= arendre:
        solution.append(p)
        return rendu_glouton(pieces, arendre - p, solution, i)
    else :
        return rendu_glouton(pieces, arendre, solution, i + 1)

assert rendu_glouton(Pieces, 68) == [50, 10, 5, 2, 1]
assert rendu_glouton(Pieces, 291, []) == [100, 100, 50, 20, 20, 1]

# ------------------------------ SUJET 9 ------------------------------ #

# Exercice 1 :

def moyenne(couple : list) -> float:
    total, nb_coeff = 0, 0
    for note, coeff in couple:
        total += note * coeff
        nb_coeff += coeff
    return total / nb_coeff if nb_coeff else None

assert moyenne([]) == None
assert moyenne([(0,2)]) == 0
assert moyenne([(15,2)]) == 15
assert moyenne([(15,2), (9,1), (12,3)]) == 12.5

# Exercice 2 :

def pascal(n : int) -> list:
    C = [[1]]
    for k in range(1, n):
        Ck = [1]
        for i in range(1, k):
            Ck.append(C[k - 1][i - 1] + C[k - 1][i])
        Ck.append(1)
        C.append(Ck)
    return C

assert pascal(1) == [[1]]
assert pascal(2) == [[1], [1, 1]]
assert pascal(3) == [[1], [1, 1], [1, 2, 1]]
assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert pascal(6) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

# ------------------------------ SUJET 10 ------------------------------ #

# Exercice 1 :

def maxi(tab : list) -> tuple:
    idx = 0
    max = tab[idx]
    for i in range(1, len(tab)):
        if tab[i] > max:
            idx = i
            max = tab[idx]
    return (max, idx)

assert maxi([1,5,6,9,1,2,3,7,9,8]) == (9,3)
assert maxi([8]) == (8,0)

# Exercice 2 :

def positif(T :  list) -> list:
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        T2.append(T3.pop())
    return T2

assert positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]) == [0, 5, 4, 10, 9]
assert positif([-1]) == []
assert positif([0]) == [0]

# ------------------------------ SUJET 11 ------------------------------ #

# Exercice 1 :

def conv_bin(n : int) -> tuple:
    if n < 0:
        return None
    nb_bit = 1
    bin = [n % 2]
    n = n // 2
    while n:
        nb_bit += 1
        bin = [n % 2] + bin
        n = n // 2
    return (bin, nb_bit)

assert conv_bin(-1) == None
assert conv_bin(0) == ([0], 1)
assert conv_bin(9) == ([1,0,0,1], 4)
assert conv_bin(14) == ([1,1,1,0], 4)

# Exercice 2 :

def tri_bulles(T : list) -> list:
    n = len(T)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if T[j] > T[j + 1]:
                temp = T[j]
                T[j] = T[j + 1]
                T[j + 1] = temp
    return T

assert tri_bulles([0, 1, 6, 5, 4, 3]) == [0, 1, 3, 4, 5, 6]
assert tri_bulles([0, 1, 2]) == [0, 1, 2]
assert tri_bulles([2, 1, 0]) == [0, 1, 2]
assert tri_bulles([0]) == [0]
assert tri_bulles([]) == []

# ------------------------------ SUJET 12 ------------------------------ #

# Exercice 1 :

def maxi(tab : list) -> tuple:
    idx = 0
    max = tab[idx]
    for i in range(len(tab)):
        if max < tab[i]:
            idx = i
            max = tab[idx]
    return max, idx

assert maxi([1,5,6,9,1,2,3,7,9,8]) == (9,3)
assert maxi([9,1,2,3,7,9,8]) == (9,0)
assert maxi([0]) == (0,0)

# Exercice 2 :

def recherche(gene : str, seq_adn : str) -> bool:
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n and trouve == False:
        j = 0
        while j < g and gene[j] == seq_adn[i + j]:
            j += 1
        if j == g:
            trouve = True
        i += 1
    return trouve

assert recherche("AATC", "GTACAAATCTTGCC") == True
assert recherche("AGTC", "GTACAAATCTTGCC") == False
assert recherche("AGTC", "GTAC") == False
assert recherche("AGTC", "AGTC") == True
assert recherche("A", "TA") == True
assert recherche("TA", "A") == False

# ------------------------------ SUJET 13 ------------------------------ #

# Exercice 1 :

def tri_selection(tab : list) -> list:
    n = len(tab)
    for i in range(n):
        j = i
        min = tab[j]
        for idx in range(i + 1, n):
            if tab[idx] < min:
                j = idx
                min = tab[j]
        if i != j:
            tab[i], tab[j] = tab[j], tab[i]
    return tab

assert tri_selection([]) == []
assert tri_selection([1]) == [1]
assert tri_selection([1, 52, 6, -9, 12]) == [-9, 1, 6, 12, 52]

# Exercice 2 :

from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1
    while nb_mystere != nb_test and compteur < 11 :
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))
    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print ("Perdu ! Le nombre était ", nb_mystere)

plus_ou_moins()

# ------------------------------ SUJET 14 ------------------------------ #

# Exercice 1 :

def recherche(elt : int, tab : list) -> list:
    idx = []
    for i in range(len(tab)):
        if tab[i] == elt:
            idx.append(i)
    return idx

assert recherche(3, [3, 2, 1, 3, 2, 1]) == [0, 3]
assert recherche(4, [1, 2, 3]) == []
assert recherche(4, []) == []

# Exercice 2 :

def moyenne(nom : str, resultats : dict) -> float:
    if nom in resultats:
        notes = resultats[nom]
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note, coefficient = valeurs
            total_points += note * coefficient
            total_coefficients += coefficient
        return round(total_points / total_coefficients, 1)
    else:
        return -1

resultats = {'Dupont':{'DS1': [15.5, 4],
                       'DM1': [14.5, 1],
                       'DS2': [13, 4],
                       'PROJET1': [16, 3],
                       'DS3': [14, 4]},
             'Dupond':{'DS1': [1, 4]},
             'Durand':{'DS1': [6, 4],
                       'DM1': [14.5, 1],
                       'DS2': [8, 4],
                       'PROJET1': [9, 3],
                       'IE1': [7, 2],
                       'DS3': [8, 4],
                       'DS4':[15, 4]},
             'Durant':{'DS1': [1, 4],
                       'DS2': [6, 1]}}

assert moyenne('toto', resultats) == -1
assert moyenne('Dupont', resultats) == 14.5
assert moyenne('Dupond', resultats) == 1
assert moyenne('Durand', resultats) == 9.2
assert moyenne('Durant', resultats) == 2

# ------------------------------ SUJET 15 ------------------------------ #

# Exercice 1 :

def RechercheMinMax(tab : list) -> dict:
    if len(tab) == 0:
        return {'min': None, 'max': None}
    min, max = tab[0], tab[0]
    for i in tab:
        if i < min:
            min = i
        if i > max:
            max = i
    return {'min': min, 'max': max}

assert RechercheMinMax([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
assert RechercheMinMax([0]) == {'min': 0, 'max': 0}
assert RechercheMinMax([]) == {'min': None, 'max': None}

# Exercice 2 :

class Carte:

    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur  = v

    def getNom(self):
        if (self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle'][self.Couleur]

class PaquetDeCarte:

    def __init__(self):
        self.contenu = []

    def remplir(self):
        for c in ['pique', 'coeur', 'carreau', 'trefle']:
            for v in range(1, 15):
                self.contenu.append(Carte(c, v))

    def getCarteAt(self, pos):
        try:
            return self.contenu[pos-1]
        except IndexError:
            pass

unPaquet = PaquetDeCarte()
unPaquet.remplir()

try:
    assert unPaquet.getCarteAt(20).getNom() == '6'
    assert unPaquet.getCarteAt(20).getCouleur() == 'coeur'
    assert unPaquet.getCarteAt(1).getNom() == 'As'
    assert unPaquet.getCarteAt(1).getCouleur() == 'pique'
    assert unPaquet.getCarteAt(111).getNom() == '1'
    assert unPaquet.getCarteAt(-1).getCouleur() == 'pique'
except AttributeError:
    print("La carte n'existe pas")

# ------------------------------ SUJET 16 ------------------------------ #

# Exercice 1 :

def moyenne(tab : list) -> float:
    total = 0
    for i in tab:
        total += i
    return total / len(tab) if len(tab) else None

assert moyenne([]) == None
assert moyenne([1.0]) == 1.0
assert moyenne([1.0, 2.0, 4.0]) == 2.3333333333333335

# Exercice 2 :

def dec_to_bin(a : int) -> str:
    bin_a = str(a % 2)
    a = a // 2
    while a != 0 :
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a

assert dec_to_bin(0) == '0'
assert dec_to_bin(83) == '1010011'
assert dec_to_bin(127) == '1111111'

# ------------------------------ SUJET 17 ------------------------------ #

# Exercice 1 :

def RechercheMin(tab : list) -> int:
    if len(tab) == 0:
        return -1
    idx = 0
    min = tab[idx]
    for i in range(len(tab)):
        if tab[i] < min:
            idx = i
            min = tab[idx]
    return idx

assert RechercheMin([]) == -1
assert RechercheMin([5]) == 0
assert RechercheMin([2, 4, 1]) == 2
assert RechercheMin([5, 3, 2, 2, 4]) == 2

# Exercice 2 :

def separe(tab : list) -> list:
    i = 0
    j = len(tab) - 1
    while i < j :
        if tab[i] == 0 :
            i = i + 1
        else :
            tab[i], tab[j] = tab[j], tab[i]
            j = j - 1
    return tab

assert separe([]) == []
assert separe([1]) == [1]
assert separe([0, 0, 0]) == [0, 0, 0]
assert separe([1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]
assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# ------------------------------ SUJET 18 ------------------------------ #

# Exercice 1 :

def recherche(elt : int, tab : list) -> int:
    idx = 0
    for i in tab:
        if i == elt:
            return idx
        idx += 1
    return -1

assert recherche(1, []) == -1
assert recherche(1, [2, 3, 4]) == -1
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(50, [1, 50, 1]) == 1
assert recherche(15, [8, 9, 10, 15]) == 3

# Exercice 2 :

def insere(a : int, tab : list) -> list:
    l = list(tab)
    l.append(a)
    i = len(tab) - 1
    while a < l[i] and i > -1:
        l[i + 1] = l[i]
        l[i] = a
        i = i - 1
    return l

assert insere(3, []) == [3]
assert insere(3, [3]) == [3, 3]
assert insere(3, [1,2,4,5]) == [1, 2, 3, 4, 5]
assert insere(10, [1,2,7,12,14,25]) == [1, 2, 7, 10, 12, 14, 25]
assert insere(1, [2,3,4]) == [1, 2, 3, 4]
assert insere(5, [2,3,4]) == [2, 3, 4, 5]

# ------------------------------ SUJET 19 ------------------------------ #

# Exercice 1 :

def recherche(tab : list, n : int) -> int:
    inf = 0
    sup = len(tab) - 1
    while inf <= sup:
        m = (inf + sup) // 2
        if tab[m] == n:
            return m
        if tab[m] < n:
            inf = m + 1
        else:
            sup = m - 1
    return -1

assert recherche([], 2) == -1
assert recherche([2], 2) == 0
assert recherche([2, 3], 2) == 0
assert recherche([2, 3], 3) == 1
assert recherche([2, 3, 4, 5], 3) == 1
assert recherche([2, 3, 4, 5], 4) == 2
assert recherche([2, 3, 4, 5, 6], 4) == 2
assert recherche([2, 3, 4, 5, 6], 5) == 3
assert recherche([2, 3, 4, 6, 7], 5) == -1

# Exercice 2 :

ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre : str) -> int:
    return ALPHABET.find(lettre)

def cesar(message : str, decalage : int) -> str:
    resultat = ''
    for lettre in message:
        if lettre in ALPHABET:
            indice   = (position_alphabet(lettre) + decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + lettre
    return resultat

assert cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4) == 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
assert cesar(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4), -4) == 'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
assert cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5) == 'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
assert cesar(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5), 5) == 'GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !'

# ------------------------------ SUJET 20 ------------------------------ #

# Exercice 1 :

t_moy  = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def mini(releve : list, date : list) -> tuple:
    if len(releve) != len(date):
        return None
    if len(releve) == 0 or len(date) == 0:
        return None
    idx = 0
    min = releve[idx]
    for i in range(len(releve)):
        if releve[i] < min:
            idx = i
            min = releve[idx]
    return (releve[idx], date[idx])

assert mini(t_moy, annees) == (12.5, 2016)

# Exercice 2 :

def inverse_chaine(chaine):
    result = ''
    for caractere in chaine:
       result = caractere + result
    return result

def est_palindrome(chaine : str) -> bool:
    inverse = inverse_chaine(chaine)
    return inverse == chaine

def est_nbre_palindrome(nbre : int) -> bool:
    chaine = str(nbre)
    return est_palindrome(chaine)

assert inverse_chaine('x') == 'x'
assert est_palindrome('x') == True
assert inverse_chaine(inverse_chaine('abc')) == 'abc'
assert inverse_chaine('bac') == 'cab'
assert est_palindrome('NSI') == False
assert est_palindrome('ISN-NSI') == True
assert est_nbre_palindrome(214312) == False
assert est_nbre_palindrome(213312) == True

# ------------------------------ SUJET 21 ------------------------------ #

# Exercice 1 :

from typing import Union

def nb_repetitions(elt : Union[int, str], tab : list) -> int:
    total = 0
    for i in tab:
        if i == elt:
            total += 1
    return total

assert nb_repetitions(5, []) == 0
assert nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]) == 3
assert nb_repetitions('A',[ 'B', 'A', 'B', 'A', 'R']) == 2
assert nb_repetitions(12, [1, '! ', 7, 21, 36, 44]) == 0

# Exercice 2 :

def binaire(a : int) -> str:
    bin_a = str(a % 2)
    a = a // 2
    while a != 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a

assert binaire(0) == '0'
assert binaire(77) == '1001101'

# ------------------------------ SUJET 22 ------------------------------ #

# Exercice 1 :

def recherche(a : Union[int, float], t : list) -> int:
    total = 0
    for i in t:
        if i == a:
            total += 1
    return total

assert recherche(5, []) == 0
assert recherche(5, [-2, 3, 4, 8]) == 0
assert recherche(3.14, [-2, 3.14, 4, 8]) == 1
assert recherche(5, [-2, 3, 1, 5, 3, 7, 4]) == 1
assert recherche(5, [-2, 5, 3, 5, 4, 5]) == 3

# Exercice 2 :

def rendu_monnaie_centimes(s_due : int, s_versee : int) -> list:
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = []
    a_rendre = s_versee - s_due
    i = len(pieces) - 1
    while a_rendre > 0 :
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else :
            i = i - 1
    return rendu

assert rendu_monnaie_centimes(700, 700) == []
assert rendu_monnaie_centimes(0, 100) == [100]
assert rendu_monnaie_centimes(0, 251) == [200, 50, 1]
assert rendu_monnaie_centimes(112, 500) == [200, 100, 50, 20, 10, 5, 2, 1]

# ------------------------------ SUJET 23 ------------------------------ #

# Exercice 1 :

def occurence_lettres(phrase : str) -> dict:
    occ = {}
    for i in phrase:
        if i in occ:
            occ[i] += 1
        else:
            occ[i] = 1
    return occ

assert occurence_lettres('') == {}
assert occurence_lettres('H') == {'H': 1}
assert occurence_lettres('HHHHHHHHHH') == {'H': 10}
assert occurence_lettres('Hello world !') == {'H': 1,'e': 1,'l': 3,'o': 2,' ': 2,'w': 1,'r': 1,'d': 1,'!': 1}

# Exercice 2 :

def fusion(L1, L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2:
        if L1[i1] < L2[i2]:
            L12[i] = L1[i1]
            i1 = i1 + 1
        else:
            L12[i] = L2[i2]
            i2 = i2 + 1
        i += 1
    while i1 < n1:
        L12[i] = L1[i1]
        i1 = i1 + 1
        i = i + 1
    while i2 < n2:
        L12[i] = L2[i2]
        i2 = i2 + 1
        i = i + 1
    return L12

assert fusion([], []) == []
assert fusion([1], []) == [1]
assert fusion([], [2]) == [2]
assert fusion([2], [1]) == [1, 2]
assert fusion([1,6,10], [0,7,8,9]) == [0, 1, 6, 7, 8, 9, 10]

# ------------------------------ SUJET 24 ------------------------------ #

# Exercice 1 :

def recherche(elt : int, tab : list) -> int:
    for i in range(len(tab) - 1, -1, -1):
        if tab[i] == elt:
            return i
    return -1

assert recherche(1, []) == -1
assert recherche(1, [2,3,4]) == -1
assert recherche(1, [10,12,1,56]) == 2
assert recherche(1, [1,50,1]) == 2
assert recherche(1, [8,1,10,1,7,1,8]) == 5

# Exercice 2 :

class AdresseIP:

    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octet(self):
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        return self.adresse == '192.168.0.0' or self.adresse == '192.168.0.255'

    def adresse_suivante(self):
        if self.liste_octet()[3] < 254:
            octet_nouveau = int(self.liste_octet()[3]) + 1
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False

assert AdresseIP('192.168.0.0').est_reservee() == True
assert AdresseIP('192.168.0.1').est_reservee() == False
assert AdresseIP('192.168.0.2').adresse_suivante().adresse == '192.168.0.3'
assert AdresseIP('192.168.0.255').adresse_suivante() == False

# ------------------------------ SUJET 25 ------------------------------ #

# Exercice 1 :

def recherche(tab : list) -> list:
    couples = []
    if len(tab) > 1:
        courant = 0
        while courant < len(tab) - 1:
            if tab[courant] == tab[courant + 1] - 1:
                couples.append((tab[courant], tab[courant + 1]))
            courant += 1
    return couples

assert recherche([1, 4, 3, 5]) == []
assert recherche([1, 4, 5, 3]) == [(4, 5)]
assert recherche([7, 1, 2, 5, 3, 4]) == [(1, 2), (3, 4)]
assert recherche([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)]

# Exercice 2 :

def propager(M : list, i : int, j : int, val : int) -> list:
    if M[i][j] == val:
        return
    M[i][j] = val
    if (i - 1) >= 0 and M[i - 1][j] == 1:
        propager(M, i - 1, j, val)
    if (i + 1) < len(M) and M[i + 1][j] == 1:
        propager(M, i + 1, j, val)
    if (j - 1) >= 0 and M[i][j - 1] == 1:
        propager(M, i, j - 1, val)
    if (j + 1) < len(M) and M[i][j + 1] == 1:
        propager(M, i, j + 1, val)
    return M

assert propager([[0,0,1,0], [0,1,0,1], [1,1,1,0], [0,1,1,0]], 2, 1, 3) == [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]

# ------------------------------ SUJET 26 ------------------------------ #

# Exercice 1 :

def occurrence_max(chaine : str):
    max = 0
    caractere = ''
    occurrence = {}
    for i in chaine:
        if i in occurrence:
            occurrence[i] += 1
        else:
            occurrence[i] = 1
        if max < occurrence[i]:
            max += 1
            caractere = i
    return caractere

assert occurrence_max('') == ''
assert occurrence_max('!!!!!!!!!!') == '!'
assert occurrence_max('+++****+++') == '+'
assert occurrence_max('je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique') == 'e'

# Exercice 2 :

def nbLig(image : list) -> int:
    return len(image)

def nbCol(image : list) -> int:
    return len(image[0])

def negatif(image : list) -> list:
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            L[i][j] = 255 - image[i][j]
    return L

def binaire(image : list, seuil : int) -> list:
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            if image[i][j] < seuil:
                L[i][j] = 1
            else:
                L[i][j] = 0
    return L

assert nbLig([[0, 2],[2, 0],[3, 3]]) == 3
assert nbCol([[0, 2],[2, 0],[3, 3]]) == 2
assert negatif([[0, 2],[2, 0],[3, 3]]) == [[255, 253],[253, 255],[252, 252]]
assert binaire([[0, 2],[2, 0],[3, 3]], 0) == [[0, 0],[0, 0],[0, 0]]
assert binaire([[0, 2],[2, 0],[3, 3]], 1) == [[1, 0],[0, 1],[0, 0]]
assert binaire([[0, 2],[2, 0],[3, 3]], 3) == [[1, 1],[1, 1],[0, 0]]
assert binaire([[0, 2],[2, 0],[3, 3]], 4) == [[1, 1],[1, 1],[1, 1]]

img = [[20, 34, 254, 145, 6], [23, 124, 287, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]

assert nbLig(img) == 4
assert nbCol(img) == 5
assert negatif(img) == [[235, 221, 1, 110, 249], [232, 131, -32, 30, 186], [58, 81, 48, 230, 168], [0, 255, 231, 58, 66]]
assert binaire(img, 120) == [[1, 1, 0, 0, 1], [1, 0, 0, 0, 1], [0, 0, 0, 1, 1], [0, 1, 1, 0, 0]]

# ------------------------------ SUJET 27 ------------------------------ #

# Exercice 1 :

def moyenne(tab : list) -> float:
    total = 0
    for i in tab:
        total += i
    return total / len(tab) if len(tab) else None

assert moyenne([]) == None
assert moyenne([3.14]) == 3.14
assert moyenne([1, 2]) == 1.5
assert moyenne([10,20,30,40,60,110]) == 45.0

# Exercice 2 :

coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], \
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0], \
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], \
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], \
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], \
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], \
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], \
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], \
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def affiche(dessin : list):
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *", end = "")
            else:
                print("  ", end = "")
        print()


def zoomListe(liste_depart : list, k : int) -> list:
    liste_zoom = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom

def zoomDessin(grille : int, k : int) -> list:
    grille_zoom = []
    for elt in grille:
        liste_zoom = zoomListe(elt, k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom

affiche(coeur)
affiche(zoomDessin(coeur, 3))

# ------------------------------ SUJET 28 ------------------------------ #

# Exercice 1 :

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}
b = {'A':['','']}
c = {'A':['B',''], 'B':['','']}
d = {}

def taille(arbre : dict, lettre : str) -> int:
    def recursif(arbre : dict, noeud : str, total : list = [0]) -> int:
        if noeud in arbre:
            total[0] += 1
            if arbre[noeud][0] != '':
                recursif(arbre, arbre[noeud][0], total)
            if arbre[noeud][1] != '':
                recursif(arbre, arbre[noeud][1], total)
        return total[0]
    return recursif(arbre, lettre) if len(arbre) else 0

assert taille(d, 'A') == 0
assert taille(b, 'A') == 1
assert taille(b, 'B') == 0
assert taille(c, 'A') == 2
assert taille(a, 'F') == 9

# Exercice 2 :

def tri_iteratif(tab : list) -> list:
    for k in range(len(tab), 0, -1):
        imax = k - 1
        for i in range(0, k - 1):
            if tab[i] > tab[imax]:
                imax = i
        if tab[imax] > tab[k - 1]:
            tab[k - 1], tab[imax] = tab[imax], tab[k - 1]
    return tab

assert tri_iteratif([]) == []
assert tri_iteratif([1]) == [1]
assert tri_iteratif([1, 2]) == [1, 2]
assert tri_iteratif([2, 1]) == [1, 2]
assert tri_iteratif([41, 55, 21, 18, 12, 6, 25]) == [6, 12, 18, 21, 25, 41, 55]

# ------------------------------ SUJET 29 ------------------------------ #

# Exercice 1 :

def calcul(n : int) -> list:
    suite = []
    if n >= 1:
        suite.append(n)
        while n != 1:
            if  n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            suite.append(n)
    return suite

assert calcul(0) == []
assert calcul(1) == [1]
assert calcul(2) == [2, 1]
assert calcul(7) == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

# Exercice 2 :

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21,"V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

def est_parfait(mot : str) -> list:
    code_c = ""
    code_a = 0
    for c in mot :
        code_c = code_c + str(dico[c])
        code_a = code_a + dico[c]
    code_c = int(code_c)
    if int(code_c) % code_a == 0:
        mot_est_parfait = True
    else :
        mot_est_parfait = False
    return [code_a, code_c, mot_est_parfait]

assert est_parfait("PAUL") == [50, 1612112, False]
assert est_parfait("ALAIN") == [37, 1121914, True]

# ------------------------------ SUJET 30 ------------------------------ #

# Exercice 1 :

def multiplication(n1 : int, n2 : int) -> int:
    total = 0
    for i in range(abs(n1)):
        total += abs(n2)
    if (n1 < 0 and n2 < 0) or (n1 > 0 and n2 > 0):
        return total
    else:
        return -total

assert multiplication(3,5) == 15
assert multiplication(-4,-8) == 32
assert multiplication(-2,6) == -12
assert multiplication(-2,0) == 0

# Exercice 2 :

def chercher(T : list, n : int, i : int, j : int) -> int:
    if i < 0 or j >= len(T):
        return None
    if i > j :
        return None
    m = (i + j) // 2
    if T[m] < n:
        return chercher(T, n, m + 1, j)
    elif T[m] > n:
        return chercher(T, n, i, m - 1)
    else :
        return m

assert chercher([], 7, 0, 10) == None
assert chercher([1,5,6,6,9,12], 7, 0, 10) == None
assert chercher([1,5,6,6,9,12], 7, 0, 5) == None
assert chercher([1,5,6,6,9,12], 9, 0, 5) == 4
assert chercher([1,5,6,6,9,12], 6, 0, 5) == 2
assert chercher([1,5,6,6,9,12], 6, 1, 3) == 2