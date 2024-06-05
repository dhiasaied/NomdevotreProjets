
def saisir():
    msg = input("Entrez le message à crypter : ")
    return msg

def crypter(msg):
    nb_mots = len(msg.split())
    decalage = nb_mots % 26

    def Détermine(c):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            return chr((ord(c) - base + decalage) % 26 + base)
        return c

    return ''.join(Détermine(c) for c in msg)

def afficher(msg_crypte):
    print("Message crypté : ", msg_crypte)

msg = saisir()
msg_crypte = crypter(msg)
afficher(msg_crypte)
