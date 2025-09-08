def check_vowels():
    vocal = input("Ingrese un nombre: ")
    for v in "aeiou":
        contiene = v in vocal.lower()
        print(f"Contiene {v}: {contiene}")
