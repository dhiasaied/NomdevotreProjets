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

def afficher(x, y):
    print(f"Les nombres premiers jumeaux entre {x} et {y} sont:")
    for i in range(x, y):
        if premier(i) and premier(i+2):
            print(f"({i}, {i+2})")


x, y = saisie()
afficher(x, y)
