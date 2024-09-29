def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

numero = int(input("Digite um número inteiro: "))
resultado = par_ou_impar(numero)

print(f"O número {numero} é {resultado}.")