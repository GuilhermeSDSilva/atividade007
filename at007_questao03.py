with open('sistema.log', 'r') as f:
    ips = set()
    for linha in f:
        if "sshd" in linha and "from" in linha:
            ip = linha.split("from ")[1].split()[0]
            ips.add(ip)
    print("IPs de conexões SSH:")
    print(ips)
