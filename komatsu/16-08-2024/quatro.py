print("Verificando se ambos são positivos...")
num1 = int(input("Digite um número: "))
num2 = int(input("Digite mais um número: "))

if num1 > 0 and num2 > 0:
    print("Os números digitados são Positivos")
elif num1 > 0 or num2 > 0:
    print("Um dos números digitados é Negativo")
else:
    print("Os dois números digitados são Negativos")

