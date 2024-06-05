e1=int(input("Donner un entier"))
e2=int(input("Donner un deuxième entier"))
e3=int(input("Donner un troisième entier"))
if e1>=e2 and e1>=e3:
    print(e1,"est le maximum")
elif e2>=e3 and e2>=e1:
    print(e2,"estle le maximum")
else:
    print(e3,"estle le maximum")
