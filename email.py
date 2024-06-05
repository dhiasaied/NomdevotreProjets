def saisir():
    adresse_email = input("Veuillez saisir une adresse email : ")
    return adresse_email


def verif1(adresse_email):
    if "@" in adresse_email:
        return True
    else:
        return False


def verif2(adresse_email):
    nom_utilisateur, reste = adresse_email.split("@")
    domaine, suffixe = reste.split(".")

    premiere_lettre_domaine = domaine[0]
    derniere_lettre_suffixe = suffixe[-1]

    mot_de_passe = nom_utilisateur + premiere_lettre_domaine + derniere_lettre_suffixe

    return mot_de_passe


adresse_email = saisir()

if verif1(adresse_email):
    mot_de_passe = verif2(adresse_email)
    print("Le mot de passe correspondant est :", mot_de_passe)
else:
    print("Adresse email invalide.")