# Depósito, Saque e Extrato

# Depósito: 
# - depositar valores positivos para minha conta
# - apenas um usuário (não precisa ter tipo de conta, agência, etc..)
# - valor inteiro e positivo (mais de 100,00)
# - Depositos devem ser armazanados em variaveis (para constar futuramente no extrato)

# Saque:
# -3 saques diários com limite de 500,00 por saque
# -caso nao tenha saldo, exibir mensagem de falha
# -saques devem ser armazanados para constar no extrato)

# Extrato:
# - listar todos depositos e saques
# - no fim da listagem deve exibir o valor atual da conta
# - valores exibidos no formato R$ xxx.xx

# INICIO


menu = '''
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair    
    
    '''
saldo = 0
limite = 500
extrato = ""
num_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! Por favor tente novamente com um valor válido...")
    
    elif opcao == "2":
        valor = float(input("Por favor informe o valor para saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor >  limite
        excedeu_saques = num_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("Limite de valor excedido!")
        elif excedeu_saques:
            print("Limite diário de saque excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            num_saque += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação inválida, por favor tente novamente!")
    
    elif opcao == "3":
        print("\n==========EXTRATO==========")
        print("Não foram relizadas movimentações." if not extrato else extrato) # expressão condicional ou expressão ternária - (valor_se_verdadeiro if condicao else valor_se_falso)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================")

    elif opcao == "0":
        print("Saída com sucesso!")
        break
    else:
        print("Operação inválida, por favor selecione uma opção novamente.")
    