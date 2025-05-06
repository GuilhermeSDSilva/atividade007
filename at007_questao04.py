with open('sistema.log', 'r') as f:
    for linha in f:
        if "Failed password" in linha:
            print(linha.strip())

