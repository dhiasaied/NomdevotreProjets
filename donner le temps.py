ch=input("Donner le temps S.V.P")
h=int(ch[0:2])
m=int(ch[3:5])
if(0>m or m>59 or h<0 or h>23):
   print("temps invalide")
else:
    m=m+5
    if m>59 :
        h=h+1
        m=m-60
        if h>23 :
            h=0
h1=str(h)
if h<10 :
    h1="0"+str(h)
m1=str(m)
if m<10 :
    m1="0"+str(m)
print("le temps aprés 5 min =",h1,":",m1)