def check_vowels():
    
    texto = input("Ingrese un nombre: ")
    texto = texto.lower()
    vocales = ["a", "e", "i", "o", "u"]

    for vocal in vocales:
        print(f"Contiene {vocal}: {vocal in texto}")
check_vowels()