from numpy import *

n=int
def saisir():
    n=int(input("donnez la taille du tableau:"))
    while not (n>=2) and (n<= 10):
        n=int(input("donnez la taille du tableau entre 2 et 10:"))
    return n

def remplir(t , n):
    t=[0]*n
    for i in range (1, n):
        while not (t[i]>=100 ) and (t[i]<=999):
            t[i] = int(input(f"t[{i}]   : "))
    return t

def pronique(n):
    for i in range(9 , n):
        if i* (i+1)==n :
            return True
    return False

def afficher(t):
    print ("les nombres proniques sont :")
    for i in t :
        if pronique(i):
            print(i)
            
n= saisir()
t=[0]*n
t= remplir(t ,n)
afficher (t) 
    

            
        
        
        
