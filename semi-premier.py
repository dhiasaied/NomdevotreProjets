def saisie():
    x, y = 0, 0
    while not (1 <= x < y <= 100):
        x = int(input("Entrez la valeur de x (1 < x < y < 100) : "))
        y = int(input("Entrez la valeur de y (1 < x < y < 100) : "))
    return x, y

def premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def semi_premier(n):
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            y = i
            x = n // i
            if premier(x) and premier(y):
                return True
    return False

def afficher(x, y):
    print("Les nombres semi-premiers entre", x, "et", y, "sont :")
    for n in range(x, y+1):
        if semi_premier(n):
            print(n)

x, y = saisie()
afficher(x, y)
