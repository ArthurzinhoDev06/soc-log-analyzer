contagem ={}


with open("sample_auth.log") as arquivo:
    for linha in arquivo:
        if "Failed password" in linha:
            pedacos = linha.split()
            posicao = pedacos.index("from") + 1
            ip = pedacos [posicao]

            if ip in contagem:
                contagem[ip] = contagem[ip] + 1
            else:
                    contagem[ip] = 1

print(contagem)

LIMITE = 5

for ip, falhas in contagem.items():
        if falhas >= LIMITE:
            print("ALERTA", ip, "teve", falhas, "falhas")