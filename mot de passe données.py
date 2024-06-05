nb=1
mp=input("Donner le mot de passe")
while not(mp=="ABCD") and nb<3:
    mp=input("Donner le mot de passe")
    nb=nb+1
if mp=="ABCD":
    print("Bienvenue")
else:
    print("accès interdit") 