with open('sistema.log', 'r') as f:
    for linha in f:
        if "sudo" in linha and "COMMAND=" in linha:
            comando = linha.split("COMMAND=")[1]
            print(comando)
