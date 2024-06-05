A=int(input("donner un entier"))
u= A % 10
if u==0 :
     print("impossible de divisible par zéro")
elif A % u == 0:
    print(A,"est divisible par",u)
else :
    print(A,"est n'est divisible par",u)