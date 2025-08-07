with open("arquivo.txt", "r", encoding="utf-8") as repositorio:
    conteudo = repositorio.read()

# Separa texto e número
texto = conteudo[:-2]      # "repositorio"
numero = conteudo[-2:]     # "01", "02", etc.

# Converte o número e incrementa
numero_atual = int(numero)
proximo_numero = numero_atual + 1

# Reinicia para 1 se passar de 5
if proximo_numero > 5:
    proximo_numero = 1

# Remonta o texto com o novo número formatado com 2 dígitos
novo_conteudo = texto + f"{proximo_numero:02d}"

# Salva o novo conteúdo no arquivo
with open("arquivo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(novo_conteudo)

print(f"Arquivo atualizado: {novo_conteudo}")
