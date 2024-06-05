m=float(input("Donner le moyenne"))
if(m<7) and (m>=0):
    print(m,"réfusé")
elif(m>=7) and (m<10):
    print(m,"controle")    
elif(m>=10) and (m<=20):
    print(m,"admis")
else:
    print(m,"incorrecte")
