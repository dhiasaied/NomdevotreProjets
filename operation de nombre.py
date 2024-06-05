n1=float(input("Donner le premier réel"))
n2=float(input("Donner le deuxième réel"))
op=input("choisir l'operation {+,-,/,*}")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="/":
    if (n2==0):
       print("impossible de diviser par zéro")
    else:
       print(n1/n2)
elif op=="*":
    print(n1*n2)
else:
    print("choix de l'operation incorrecte")
