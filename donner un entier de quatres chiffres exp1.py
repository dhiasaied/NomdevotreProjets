n=int(input("donner un entier de quatres chiffres S.V.P"))
u=n % 10
d=(n % 100)//10
c=(n%1000)//100
m=n//1000
n1=u*10+d*100+c*1000+m
print(n1)