def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

# Exemplo --------------------------------------------------------------

def soma (*valioso):
    s = 0
    for num in valioso:
        s += num
    print(f'Somando os valiosos {valioso} temos {s}')


soma(5, 2)
soma(2, 9, 4)

# Exemplo --------------------------------------------------------------

def for_area(larg, comp):
    print(f"A largura é {larg}m e o comprimento é {comp}m")
    area = larg * comp
    print(f"A Área do terreno de {larg}m x {comp}m é de: {area}m².")


print("""
CONTROLE DE TERRENOS
--------------------""")

for_area(
larg = float(input("Digite a largura em metros: ")), 
comp = float(input("Digite o comprimento em metros: ")))
#   Alternativa correta!?
#   l = float(input("Digite a largura em metros: "))
#   c = float(input("Digite o comprimento em metros: "))
#   for_area(l, c)

# Exemplo --------------------------------------------------------------

def escreva(texto):
    tam = len(texto)
    print("~" * tam)
    print(texto)
    print("~" * tam)


escreva("Um Grande Sábio disse uma vez, e continua dizendo...")
escreva("Penis buceta xoxota xoxota buceta cu lingua pinto")
escreva("muita sabedoria desbalanceada...")

# Exemplo --------------------------------------------------------------

def contador(i, f, p):
    print(f"Contagem de {i} até {f} de {p} em {p}")
    
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont}", end=" ")
            cont += p
        print()
        print("FEIN! FEIN! FEIN! FEIN! FEIN! FEIN!")
    else:
        cont = i
        while cont>= f:
            print(f"{cont}", end=" ")
            cont -= p
        print()
        print("FEIN! FEIN! FEIN! FEIN! FEIN! FEIN!")
    print("-=" * 20)


contador(1, 10, 1)
contador(10, 0, 2)
print("Agora ua vez de personalizar a contagem!")
ini = int(input("Início: "))
fim = int(input("Fim: "))
pas = int(input("Passo: "))
contador(ini, fim, pas)