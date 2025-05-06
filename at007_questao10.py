from collections import Counter

ips = []
with open('sistema.log', 'r') as f:
    for linha in f:
        if "sshd" in linha and "from" in linha:
            ip = linha.split("from ")[1].split()[0]
            ips.append(ip)

contagem = Counter(ips)
for ip, qtd in contagem.most_common():
    print(f"{ip}: {qtd}")
