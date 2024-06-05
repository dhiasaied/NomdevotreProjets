from numpy import *

def Valide(ch):
    c = True
    if len(ch) == 0:
        c = False
    elif not ch[0].isalpha() or not ch[0].isupper():
        return False
    for i in range(1, len(ch)):
        if not ch[i].isalpha():
            c = False
    return c
    
def Chercher(Pers, P, C):
    exist = False
    for element in P[:C]:
        if element == Pers:
            exist = True
            break
    return exist

p = [""] * 10
C = 1
i = 0
while not Valide(p[0]):
    p[0] = input("donnez le nom du personnage du paquet num 1 : ")
    C = 1
    i = 1
while C != 5 and i != 10:
    i += 1
    pers = ""
    while not Valide(pers):
        pers = input(f"donnez le nom du personnage du paquet num {i}: ")
    if not Chercher(pers, p, C):
        C += 1
        p[C] = pers

if C == 5:
    print("vous avez gagné")
else:
    print("vous avez perdu")
