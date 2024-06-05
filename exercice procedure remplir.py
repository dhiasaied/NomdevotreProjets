from numpy import array
#Création de la procédure
def remplir(T,n):
    for i in range(n):
        T[i]=int(input("donner un entier"))
        
def saisir():
    n=int(input("Donner la taille du tableau"))
    while(n>30)or(n<10):
        n=int(input("la taille entre 10 et 30"))
    return n

def  afficher(T,n):
    for i in range(n):
        if T[i]>0:
            print(T[i])
#Programme principal
T=array([int()]*20)
n=saisir()
remplir(T,n)
afficher(T,n)