# BACCALAURÉAT GÉNÉRAL NSI TERMINALE - ÉPREUVE PRATIQUE - SUJETS - SESSION 2022

# ------------------------------ SUJET 1 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-01.pdf !

# Exercice 2 :

Pieces = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(arendre, solution = [], i = 0):
    if arendre == 0:
        return ...
    p = Pieces[i]
    if p <= ... :
        solution.append(...)
        return rendu_glouton(arendre - p, solution, i)
    else :
        return rendu_glouton(arendre, solution, ...)
    
# ------------------------------ SUJET 2 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-02.pdf !

# Exercice 2 :

def pascal(n):
    C = [[1]]
    for k in range(1, ...):
        Ck = [...]
        for i in range(1, k):
            Ck.append(C[...][i - 1] + C[...][...])
        Ck.append(...)
        C.append(Ck)
    return C

# ------------------------------ SUJET 3 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-03.pdf !

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
    s = ...
    if e.gauche is not None:
        s = '(' + s + expression_infixe(...)
    s = s + ...
    if ... is not None:
        s = s + ... + ...
    if ... :
        return s
    
# ------------------------------ SUJET 4 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-04.pdf !

# Exercice 2 :

def propager(M, i, j, val):
    if M[i][j] == ...:
        return
    M[i][j] = val
    if ((i - 1) >= 0 and M[i - 1][j] == ...):
        propager(M, i - 1, j, val)
    if ((...) < len(M) and M[i + 1][j] == 1):
        propager(M, ..., j, val)
    if ((...) >= 0 and M[i][j - 1] == 1):
        propager(M, i, ..., val)
    if ((...) < len(M) and M[i][j + 1] == 1):
        propager(M, i, ..., val)

# ------------------------------ SUJET 5 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-05.pdf !

# Exercice 2 :

class Carte:

    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v

    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
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
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

class PaquetDeCarte:

    def __init__(self):
        self.contenu = []

    def remplir(self):
	    ... = [... for couleur in range(1, ...) for valeur in range(1, ...)]

    def getCarteAt(self, pos):
        if 0 <= pos < ...:
            return ...

# ------------------------------ SUJET 6 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-06.pdf !

# Exercice 2 :

def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = ...
    trouve = False
    while i < ... and trouve == ... :
        j = 0
        while j < g and gene[j] == seq_adn[i + j]:
            ...
        if j == g:
            trouve = True
        ...
    return trouve

# ------------------------------ SUJET 7 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-07.pdf !

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

# ------------------------------ SUJET 8 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-08.pdf !

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

# ------------------------------ SUJET 9 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-09.pdf !

# Exercice 2 :

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21,"V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

def est_parfait(mot) :
    code_c = ""
    code_a = ...
    for c in mot :
        code_c = code_c + ...
        code_a = ...
    code_c = int(code_c)
    if ... :
        mot_est_parfait = True
    else :
        mot_est_parfait = False
    return [code_a, code_c, mot_est_parfait]

# ------------------------------ SUJET 10 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-10.pdf !

# Exercice 2 :

def fusion(L1, L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and ... :
        if L1[i1] < L2[i2]:
            L12[i] = ...
            i1 = ...
        else:
            L12[i] = L2[i2]
            i2 = ...
        i += 1
    while i1 < n1:
    	L12[i] = ...
    	i1 = i1 + 1
    	i = ...
    while i2 < n2:
    	L12[i] = ...
    	i2 = i2 + 1
    	i = ...
    return L12

# ------------------------------ SUJET 11 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-11.pdf !

# Exercice 2 :

ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    resultat = ''
    for ... in message:
        if lettre in ALPHABET:
            indice = ( ... ) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = ...
    return resultat

# ------------------------------ SUJET 12 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-12.pdf !

# Exercice 2 :

def tri(tab):
    i = ...
    j = ...
    while i != j :
        if tab[i] == 0:
            i= ...
        else :
            valeur = tab[j]
            tab[j] = ...
            ...
            j = ...
    ...

# ------------------------------ SUJET 13 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-13.pdf !

# Exercice 2 :

class Maillon :

    def __init__(self, v):
        self.valeur = v
        self.suivant = None

class File :

    def __init__(self):
        self.dernier_file = None

    def enfile(self, element):
        nouveau_maillon = Maillon(...) 
        nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = ...

    def est_vide(self):
        return self.dernier_file == None

    def affiche(self):
        maillon = self.dernier_file
        while maillon != ...:
            print(maillon.valeur)
            maillon = ...

    def defile(self):
        if not self.est_vide():
            if self.dernier_file.suivant == None:
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = ...
            while maillon.suivant.suivant != None:
                maillon = maillon.suivant
            resultat = ...
            maillon.suivant = None
            return resultat
        return None 

# ------------------------------ SUJET 14 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-14.pdf !

# Exercice 2 :

def est_cyclique(plan):
    personne = 'A'
    N = len(...)                          
    for i in range(...):
        if plan[...] == ...:
            return ...
        else:
            personne = ...
    return ...

# ------------------------------ SUJET 15 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-15.pdf !

# Exercice 2 :

def binaire(a):
    bin_a = str(...)
    a = a // 2
    while a ...:
        bin_a = ...(a % 2) + ...
        a = ...
    return bin_a

# ------------------------------ SUJET 16 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-16.pdf !

# Exercice 2 :

def positif(T):
    T2 = ...(T)
    T3 = ...
    while T2 != []:
        x = ...
        if ... >= 0:
            T3.append(...)
    T2 = []
    while T3 != ...:
        x = T3.pop()
        ...
    print('T = ', T)
    return T2

# ------------------------------ SUJET 17 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-17.pdf !

# Exercice 2 :

class Noeud:

    def __init__(self, v, g, d):
        self.valeur = v
        self.gauche = g
        self.droite = d
        
class ABR:
    
    def __init__(self):
        self.racine = None
        
    def est_vide(self):
        return self.racine is None
    
    def parcours(self, tab = []):
        if self.est_vide():
            return tab
        else:
            self.racine.gauche.parcours(tab)
            tab.append(...)
            ...
            return tab
        
    def insere(self, element):
        if self.est_vide():
            self.racine = Noeud(element, ABR(), ABR())
        else:
            if element < self.racine.valeur:
                self.racine.gauche.insere(element)
            else : 
                self.racine.droite.insere(element)
    
    def recherche(self, element):
        if self.est_vide():
            return ...
        else:
            if element < self.racine.valeur:
                return ...
            elif element > self.racine.valeur:
                return ...
            else:
                return ...

# ------------------------------ SUJET 18 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-18.pdf !

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

# ------------------------------ SUJET 19 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-19.pdf !

# Exercice 2 :

def chercher(T, n, i, j):
    if i < 0 or ...:
        print("Erreur")
        return None    
    if i > j:
        return None
    m = (i + j) // ...
    if T[m] < ...:
        return chercher(T, n, ... , ...)
    elif ...:
        return chercher(T, n, ..., ...)
    else :
        return ...
    
# ------------------------------ SUJET 20 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-20.pdf !

# Exercice 2 :

class Carre:

    def __init__(self, tableau = [[]]):
        self.ordre = len(tableau)
        self.valeurs = tableau
    
    def affiche(self):
        for i in range(self.ordre):
            print(self.valeurs[i])
    
    def somme_ligne(self, i):
        return sum(self.valeurs[i])
    
    def somme_col(self, j):
        return sum([self.valeurs[i][j] for i in range(self.ordre)])

def est_magique(carre):
    n = carre.ordre
    s = carre.somme_ligne(0) 
    for i in range(..., ...):
        if carre.somme_ligne(i) != s:
            return ...    
    for j in range(n):
        if ... != s:
            return False  
    if sum([carre.valeurs[...][...] for k in range(n)]) != s:
            return False
    if sum([carre.valeurs[k][n-1-k] for k in range(n)]) != s:
            return False
    return ...   

# ------------------------------ SUJET 21 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-21.pdf !

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

# ------------------------------ SUJET 22 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-22.pdf !

# Exercice 2 :

def crible(N):
    premiers = []
    tab = [True] * N
    tab[0], tab[1] = False, False
    for i in range(..., N):
        if tab[i] == ...:
            premiers.append(...)
            for multiple in range(2*i, N, ...):
                tab[multiple] = ...
    return premiers

assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

# ------------------------------ SUJET 23 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-23.pdf !

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

# ------------------------------ SUJET 24 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-24.pdf !

# Exercice 2 :

class Pile:

    def __init__(self, valeurs = []):
        self.valeurs = valeurs

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

assert parenthesage("((()())(()))") == True
assert parenthesage("())(()") == False
assert parenthesage("(())(()") == False

# ------------------------------ SUJET 25 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-25.pdf !

# Exercice 2 :

def trouver_intrus(tab, g, d):
    if g == d:
        return ...
    else:
        nombre_de_triplets = (d - g) // ...
        indice = g + 3 * (nombre_de_triplets // 2)
        if ... :
            return ...
        else:
            return ...

# ------------------------------ SUJET 26 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-26.pdf !

# Exercice 2 :

def separe(tab):
    i = 0
    j = ...
    while i < j:
        if tab[i] == 0:
            i = ...
        else :
            tab[i], tab[j] = ...
            j = ...
    return tab

# ------------------------------ SUJET 27 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-27.pdf !

# Exercice 2 :

def tri_iteratif(tab):
    for k in range( ... , 0, -1):
        imax = ...
        for i in range(0 , ...):
            if tab[i] > ...:
                imax = i
        if tab[imax] > ...:
            ..., tab[imax] = tab[imax], ...
    return tab

# ------------------------------ SUJET 28 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-28.pdf !

# Exercice 2 :

def dec_to_bin(a):
    bin_a = ...
    a = a // 2
    while a ...:
        bin_a = ... + bin_a
        a = ...
    return bin_a

# ------------------------------ SUJET 29 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-29.pdf !

# Exercice 2 :

liste_eleves = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
liste_notes = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24]

def meilleures_notes():
    note_maxi = 0
    nb_eleves_note_maxi = ...
    liste_maxi = ...
    for compteur in range(...):
        if liste_notes[compteur] == ...:
            nb_eleves_note_maxi = nb_eleves_note_maxi + 1
            liste_maxi.append(liste_eleves[...])
        if liste_notes[compteur] > note_maxi:
            note_maxi = liste_notes[compteur]
            nb_eleves_note_maxi = ...
            liste_maxi = [...]
    return (note_maxi,nb_eleves_note_maxi,liste_maxi)

# ------------------------------ SUJET 30 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-30.pdf !

# Exercice 2 :

def rom_to_dec (nombre):
    dico = {"I": 1, "V": 5, ...}
    if len(nombre) == 1:
        return ...
    else:
        nombre_droite = nombre[1:]
        if dico[nombre[0]] >= dico[nombre[1]]:
            return dico[nombre[0]] + ...
        else:
            return ...

assert rom_to_dec("CXLII") == 142

# ------------------------------ SUJET 31 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-31.pdf !

# Exercice 2 :

def rendu_monnaie_centimes(s_due, s_versee):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = ...
    a_rendre = ...
    i = len(pieces) - 1
    while a_rendre > ...:
        if pieces[i] <= a_rendre:
            rendu.append(...)
            a_rendre = ...
        else:
            i = ...
    return rendu

# ------------------------------ SUJET 32 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-32.pdf !

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

# ------------------------------ SUJET 33 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-33.pdf !

# Exercice 2 :

def tri_insertion(L):
    n = len(L)
    if ...:
        return L
    for j in range(1, n):
        e = L[j]
        i = j
        while i > 0 and L[i - 1] > ...:
            i = ...
        if i != j:
            for k in range(j, i, ...):
                L[k] = L[...]
            L[i] = ...
    return L

# ------------------------------ SUJET 34 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-34.pdf !

# Exercice 2 :

def nbLig(image):
    return ...

def nbCol(image):
    return ...

def negatif(image):
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(len(image)):
        for j in range(...):
            L[i][j] = ...
    return L

def binaire(image, seuil):
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))] 
    for i in range(len(image)):
        for j in range(...):
            if image[i][j] < ...:
                L[i][j] = ...
            else:
                L[i][j] = ...
    return L

# ------------------------------ SUJET 35 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-35.pdf !

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

# ------------------------------ SUJET 36 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-36.pdf !

# Exercice 2 :

from math import sqrt

def distance(point1, point2): 
    return sqrt((...)**2 + (...)**2)

assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"

def plus_courte_distance(tab, depart):
    point = tab[0]
    min_dist = ...
    for i in range (1, ...):
        if distance(tab[i], depart) ...:
            point = ...
            min_dist = ...
    return point

assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5), "erreur"

# ------------------------------ SUJET 37 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-37.pdf !

# Exercice 2 :

urne = ['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']

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

# ------------------------------ SUJET 38 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-38.pdf !

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
        print ("Bravo ! Le nombre etait ", ...)
        print("Nombre d'essais: ", ...)
    else:
        print ("Perdu ! Le nombre etait ", ...)

# ------------------------------ SUJET 39 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-39.pdf !

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
    for elt in ...:
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

# ------------------------------ SUJET 40 ------------------------------ #

# Exercice 1 : L'énoncé de l'exercice est disponible dans le fichier 22-NSI-40.pdf !

# Exercice 2 :

resultats = {'Dupont': {'DS1': [15.5, 4],
                        'DM1': [14.5, 1],
                        'DS2': [13, 4],
                        'PROJET1': [16, 3],
                        'DS3': [14, 4]},
             'Durand': {'DS1': [6, 4],
                        'DM1': [14.5, 1],
                        'DS2': [8, 4],
                        'PROJET1': [9, 3],
                        'IE1': [7, 2],
                        'DS3': [8, 4],
                        'DS4': [15, 4]}}

def moyenne(nom):
    if nom in ...:
        notes = resultats[nom]
        total_points = ...
        total_coefficients = ...
        for ... in notes.values():
            note, coefficient = valeurs
            total_points = total_points + ... * coefficient
            total_coefficients = ... + coefficient
        return round(... / total_coefficients, 1)
    else:
        return -1