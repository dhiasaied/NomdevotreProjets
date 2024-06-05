from numpy import *

def saisie():
    p, q = 0, 0
    while not (2 <= p <= q):
        p = int(input("Donnez le premier nombre p : "))
        q = int(input("Donnez le deuxieme nombre q : "))
    return p, q

def fact(x):
    f = 1
    for i in range(2, x+1):
        f *= i
    return f

def afficher(p, q):
    for i in range(p, q+1):
        s = 0
        ch = str(i)
        for j in range(len(ch)):
            s += fact(int(ch[j]))
        if s == i:
            print("Nombre fort:", i)
        else:
            print("Pas un nombre fort:", i)

p, q = saisie()
afficher(p, q)

