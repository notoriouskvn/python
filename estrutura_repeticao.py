# Exemplo sem repetição
# Receba um número e exiba 2 números seguintes:
n = int(input("Digite um número: "))

n += 1
print(n)

n += 1
print(n)


# For-In:
texto = input("Informe um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
print()


#For / Else:
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
else:
    print()
    print("Executa ao final do laço.")


# Built-in Range
# 3 Argumentos: stop(obrigatório), start(opcional) e step (opcional)
# Exemplo:
list(range(5))
[0, 1, 2, 3, 4, 5, 6]