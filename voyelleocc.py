def main():
    string = input("Veuillez entrer une chaîne de caractère : ")
    voyelles = "aeiouy"

    letters = {char: string.lower().count(char) for char in voyelles}

    for char in voyelles:
        print(f"{char}: {letters[char]}")
        if char.isupper():
            print(f"{char} (majuscule): {letters[char.lower()]}")
        elif char.islower():
            print(f"{char} (minuscule): {letters[char]}")

    print("\nRatios:")
    for char in voyelles:
        ratio = (letters[char] / len(string)) * 100
        print(f"{char}: {ratio:.2f}%")

if __name__ =="__main__":
    main()
