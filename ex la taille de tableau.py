from numpy import array

n=int(input("donner la taille de tableau"))
while not(5<=n<=20):
    n=int(input(" taille entre 5 et 20 S.V.P"))

T=array([str]*n)

for i in range(n):
    T[i]=input("donner le nom n°"+str(i+1))
    while len(T[i])<=5:
        T[i]=input("donner le nom n°"+str(i+1))
for i in range(n):
    print(T[i],"|",end="")