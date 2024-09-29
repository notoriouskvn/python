import itertools

# Função para solicitar as 12 opções ao usuário
def obter_opcoes():
    opcoes = []
    for i in range(12):
        opcao = input(f"Digite o nome da opção {i + 1}: ")
        opcoes.append(opcao)
    return opcoes

# Função para realizar um duelo entre duas opções, com o usuário escolhendo o vencedor
def duelo(opcao1, opcao2):
    print(f"\nDuelo: {opcao1} vs {opcao2}")
    while True:
        escolha = input(f"Digite 1 para {opcao1} ou 2 para {opcao2}: ")
        if escolha == '1':
            return opcao1
        elif escolha == '2':
            return opcao2
        else:
            print("Escolha inválida. Tente novamente.")

# Função para realizar todos os duelos e contar vitórias
def realizar_duelos(opcoes):
    placar = {opcao: 0 for opcao in opcoes}  # Inicializa o placar com 0 vitórias para cada opção
    duelos = list(itertools.combinations(opcoes, 2))  # Cria todas as combinações possíveis (duelos)

    for duelo_atual in duelos:
        opcao1, opcao2 = duelo_atual
        vencedor = duelo(opcao1, opcao2)
        print(f"Vencedor: {vencedor}")
        placar[vencedor] += 1

    return placar

# Função para exibir a classificação final
def exibir_classificacao(placar):
    classificacao = sorted(placar.items(), key=lambda x: x[1], reverse=True)
    print("\nClassificação final:")
    for i, (opcao, vitorias) in enumerate(classificacao, start=1):
        print(f"{i}. {opcao} - {vitorias} vitórias")

# Programa principal
def main():
    print("Bem-vindo ao torneio de opções!")
    opcoes = obter_opcoes()
    placar = realizar_duelos(opcoes)
    exibir_classificacao(placar)

if __name__ == "__main__":
    main()
