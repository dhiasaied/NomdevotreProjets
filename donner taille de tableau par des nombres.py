from numpy import *
from random import randint

n=int(input("donner la taille du tableau"))
while not(5<=n<=20):
    n=int(input("donner la taille du tableau"))
    
T=array([int()]*n)
for i in range(n):
    T[i]=randint(100,999)
    
for i in range(n):
    if(T[i] % 2==0):
        print(T[i],"|",end="")