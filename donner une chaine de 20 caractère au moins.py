ch=input("donner une chaine de 20 caractère au moins")
while len(ch)<20:
    ch=input("donner une chaine de 20 caractère au moins")

c=input("donner un caractère")
while len(c)!=1:
    c=input("donner un caractère")

if(ch.find(c)==-1):
    print("le caractère n'existe pas dans la chaine")
else:
    nb=0
    for i in range(len(ch)):
        if ch[i]==c:
            nb=nb+1
    print("le nombre d'occurence de c dans ch est",nb)