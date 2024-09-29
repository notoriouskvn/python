def soma_lista(numeros):
    return sum(numeros)

numeros_usuario = input("Digite uma lista de números separados por espaço para somar: ")

lista_numeros = list(map(int, numeros_usuario.split()))
soma = soma_lista(lista_numeros)

print(f"A soma dos números {lista_numeros} é {soma}.")
