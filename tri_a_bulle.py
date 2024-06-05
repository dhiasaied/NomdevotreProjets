from numpy import *

t=random.randint(1, 101, size=10)
def tri_A_bulle(t):
    while ((permute == True) and (n ==len(T))) :
        for i in range(len(t)):
            if (T[i]> T[i+1]):
                a= T[i]
                T[i]=T[i+1]
                T[i+1]=a
                return t
print(t)
print("le tableau trie est:")
print(t)

