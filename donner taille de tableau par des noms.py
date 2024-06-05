from numpy import *
n=int(input("donner la taille du tableau"))
while not(5<=n<=20):
    n=int(input("donner la taille du tableau"))
    
T=array([str]*n)
for i in range(n):
    T[i]=input("donner un nom")
    while len(T[i])<=4:
        T[i]=input("donner un nom correcte")
ch=input("donner le nom à chercher")
while len(ch)<=4:
        ch=input("donner un nom correcte")
trouve=False
for i in range(n):
    if T[i]==ch:
        trouve=True
if trouve==True:
    print("le nom existe")
else:
    print("le nom n'existe pas")