usuarios = set()
with open('sistema.log', 'r') as f:
    for linha in f:
        if "sudo" in linha:
            partes = linha.split()
            for p in partes:
                if p.endswith(':'):
                    usuarios.add(p[:-1])
print("Usuários que usaram sudo:")
print(usuarios)
