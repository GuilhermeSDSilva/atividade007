from datetime import datetime

def extrair_data(l):
    partes = l.split()
    data = f"{partes[0]} {partes[1]} {partes[2]}"
    return datetime.strptime(data, "%b %d %H:%M:%S")

with open('sistema.log', 'r') as f:
    linhas = [linha.strip() for linha in f if linha.strip()]

ordenado = sorted(linhas, key=extrair_data)
for linha in ordenado:
    print(linha)
