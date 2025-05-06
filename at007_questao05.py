with open('sistema.log', 'r') as f:
    sucesso = falha = 0
    for linha in f:
        if "Accepted password" in linha:
            sucesso += 1
        elif "Failed password" in linha:
            falha += 1
print(f"Logins bem-sucedidos: {sucesso}")
print(f"Logins falhos: {falha}")
