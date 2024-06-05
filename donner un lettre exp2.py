ch=input("Donner une lettre")
ch1=ch.upper()
if ch1<"A" or ch1>"Z" :
    print(ch1,"n'est pas une lettre")
elif (ch1 in ["A","O","E","I","U","Y"]):
    print("voyelle")
else:
    print("consonne")