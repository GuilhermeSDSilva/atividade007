with open('sistema.log', 'r') as f:
    for linha in f:
        if "Accepted password" in linha:
            print(linha.strip())
