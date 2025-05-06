from collections import Counter

usuarios = []
with open('sistema.log', 'r') as f:
    for linha in f:
        if "Failed password" in linha:
            usuario = linha.split("for ")[1].split()[0]
            usuarios.append(usuario)

contagem = Counter(usuarios)
for user, qtd in contagem.items():
    if qtd > 1:
        print(f"{user}: {qtd} falhas")
