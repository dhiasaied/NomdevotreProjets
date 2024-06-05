m=float(input("Donner le moyenne"))
if(m<7) and (m>=0):
    print(m,"réfusé")
elif(m>=7) and (m<10):
    print(m,"controle")    
elif(10<=m) and (m<12) :
    print(m,"passable")
elif(12<=m) and (m<14) :
    print(m,"assez bien")
elif(14<=m) and (m<16) :
    print(m,"bien")
elif(16<=m) and (m<18) :
    print(m,"T.bien")
elif(18<=m) and (m<=20) :
    print(m,"excellent")
else:
    print(m,"incorrecte")