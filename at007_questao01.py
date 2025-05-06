with open('sistema.log', 'r') as f:
    linhas = [linha for linha in f if linha.strip()]
print(f"Total de linhas no log: {len(linhas)}")
