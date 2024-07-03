def saisir():
    x = int(input("Entrez un entier (x) : "))
    y = int(input("Entrez un entier (y) : "))
    return x, y

def is_sp(n):
    if n % 4 != 0:
        return False
    
    for c in str(n):
        if int(c) % 2 != 0:
            return False
    
    d = [d for d in range(2, int(n**0.5) + 1) if n % d == 0]
    for div in d:
        if div % 2 != 0 and n // div % 2 != 0:
            return False
    
    return True

def afficher(x, y):
    sp = [n for n in range(x, y + 1) if is_sp(n)]
    if sp:
        print(f"Les nombres super-pairs entre {x} et {y} sont : {sp}")
    else:
        print(f"Aucun nombre super-pair trouvé entre {x} et {y}")

x, y = saisir()
afficher(x, y)