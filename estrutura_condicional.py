# (if) , (if...else) , (elif)
# if aninhado (Estrutura Aninhada)
# if ternário (Estrutura Ternária)


maior_idade = 18
idade = int(input("Digite sua idade: "))

if idade >= 18 and idade < 65:
    print("Idade permitida para aulas de CNH")
elif idade >= 65:
    print("Idade muito alta para tirar CNH")
elif idade == 16 or 17:
    print("Insuficiente para tirar CNH, porém permitido aulas teóricas")
else:
    print("Idade insuficiente para tirar CNH")


conta_normal = 1
conta_junior = 2
conta_especial = 3

tipo_conta = int(input("Escolha o tipo de conta: 1 (Normal), 2 (Junior), 3 (Especial): "))

if tipo_conta == conta_normal:
    print("Conta Normal selecionada.")
elif tipo_conta == conta_junior:
    print("Você escolheu a conta Junior para prosseguir.")
elif tipo_conta == conta_especial:
    print("Você escolheu a conta Especial para prosseguir.")
else:
    print("Tipo de conta inválido.")

saldo = 2000
cheque_especial = 500

# Estrutura Aninhada
if tipo_conta == conta_normal: # Exemplo Estrutura Aninhada
    
    saque = int(input("Digite o saque solicitado: "))

    if saque <= saldo:                                             # Exemplo Estrutura Aninhada                
        print("Saque disponível.")
    elif saque <= saldo + cheque_especial:                         # Exemplo Estrutura Aninhada                                
        print("Saque disponível com auxílio de Cheque Especial.")
    else:                                                          # Exemplo Estrutura Aninhada
        print("Saque indisponível.")
    print("Sessão encerrada, obrigado por usar!")

elif tipo_conta == conta_especial:
   print("Conta Especial selecionada.\nEntre em contato com o banco para mais detalhes.\nSessão finalizada.\nObrigado por usar!")

elif tipo_conta == conta_junior:
    print("Conta Junior selecionada.\nEntre em contato com o banco para mais detalhes.\nSessão finalilzada.\nObrigado por usar!")
else:
    print("Nenhuma conta selecionada.\nSessão finalizada.\nObrigado por usar!")


# Estrutura Ternária
saldo2 = 2000
saque2 = 1000 # Alterar valor.

status = "Sucesso" if saldo2 >= saque2 else "Falhou" # Exemplo Estrutura Ternária
print(f"{status} ao realizar o saque!") # Exemplo Estrutura Ternária