ch=input("Donner un date sous la forme jj/mm/aaaa S.V.P")
j=int(ch[0:2])+1
m=int(ch[3:5])
a=int(ch[6:])
if(m in [1,3,5,7,8,10,12])and(j==32):
   j=1
   m=m+1
elif(m in [4,6,9,11])and(j==31):
    j=1
    m=m+1
elif(m==2)and(a%4==0)and(j==30):
     j=1
     m=m+1
elif(m==2)and(a%4!=0)and(j==29):
     j=1
     m=m+1
if(m==13):
     m=1
     a=a+1
print("demain sera le  " ,j,"\\",m,"\\",a) 