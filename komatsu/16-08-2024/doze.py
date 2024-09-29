print("Segue tabela com uma pequena ajuda...")
# Definir o tamanho da tabela
tamanho = 10

# Imprimir o cabeçalho da tabela
print("    ", end="")  # Espaço inicial para alinhar os números das colunas
for i in range(1, tamanho + 1):
    print(f"{i:4}", end="")  # Imprimir os números das colunas com largura de 4 caracteres
print()

# Imprimir a linha separadora
print("    " + "----" * tamanho)

# Imprimir as linhas da tabela
for i in range(1, tamanho + 1):
    print(f"{i:2} |", end="")  # Imprimir o número da linha com largura de 2 caracteres e um separador
    for j in range(1, tamanho + 1):
        print(f"{i * j:4}", end="")  # Imprimir o produto com largura de 4 caracteres
    print()  # Quebra de linha após cada linha da tabela
