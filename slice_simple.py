def slice_simple():
    texto = "Awesome"
    texto = texto.lower()

    # Primeras 3 letras
    print(texto[0:3])

    # 3 letras del medio
    print(texto[2:5])

    # De la primera a la cuarta + de la antepenúltima a la última
    print(texto[0:4] + texto[-3:])
slice_simple()