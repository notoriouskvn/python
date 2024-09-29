# EXEMPLO 1
#a= 2
#b= 1
#equacao= input("Digite a fórmula geral da equação linear (a * x + b): ")
#print(f"\nA entrada do usuário {equacao} é do tipo {type(equacao)}")

#for x in range(5):
#    y = eval(equacao)
#    print(f"\Resultado da equação para x = {x} é {y}")

# EXEMPLO 2
#def nome_funcao():
    #bloco de comandos

# EXEMPLO 3
#def imprimir_mensagem(disciplina, curso):
#    print(f"Primeira função em Python disciplina: {disciplina}, do curso: {curso}.")

#imprimir_mensagem("Python", "ADS")

# EXEMPLO 4
#def imprimir_mensagem(disciplina, curso):
#    print(f"Primeira função em Python disciplina: {disciplina}, do curso: {curso}")

#resultado = imprimir_mensagem("Python", "ADS")
#print(f"Resultado = {resultado}")

# EXEMPLO 5
#def imprimir_mensagem(disciplina, curso):
#    return(f"Primeira função em Python disciplina: {disciplina}, do curso: {curso}")

#resultado = imprimir_mensagem("Python", "ADS")
#print(f"Resultado = {resultado}")

# EXEMPLO 6
#def converter_mes_para_extenso(data):
#    mes = '''janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'''.split()
#    d, m, a = data.split('/')
#    mes_extenso = mes[int(m) - 1]
#    return f'{d} de {mes_extenso} de {a}'

#print(converter_mes_para_extenso('10/05/2021'))

# EXEMPLO 7
#def somar (a, b):
#    return a + b
#r=somar?

# EXEMPLO 8
#def calcular_desconto(valor, desconto=0):
#    valor_com_desconto = valor - (valor * desconto)
#    return valor_com_desconto
#valor1 = calcular_desconto(100)
#valor2 = calcular_desconto(100, 0.25)

#print(f"\nPrimeiro valor a ser pago = {valor1}")
#print(f"\nSegundo valor a ser pago = {valor2}")

# EXEMPLO 9
#def cadstrar_pessoa(nome, idade, cidade):
#   print("\nDados a serem cadastrados")
#    print(f"Nome : {nome}")
#    print(f"Nome: {nome}")
#    print(f"Cidade: {cidade}")

# EXEMPLO 10
#def converter_maiuscula(texto, flag_maiuscula):
#    if flag_maiuscula:
#        return texto.upper()
#    else:
#        return texto.lower()
#texto = converter_maiuscula(flag_maiuscula=False, texto="João")
#print(texto)

# EXEMPLO 11
#def converter_minuscula(texto, flag_minuscula=True):
#    if flag_minuscula:
#        return texto.lower()
#    else:
#        return texto.upper()
#texto1 = converter_minuscula(flag_minuscula=False, texto="LINGUAGEM de Programação")
#texto2 = converter_minuscula(texto="LINGUAGEM de Programação")
#print(f"\nTexto 1 = {texto1}")
#print(f"\nTexto 2 = {texto2}")

# EXEMPLO 12
#def imprimir_parametros(*args):
#    qtde_parametros = len(args)
#    print(f"Quantidade de parâmetros = {qtde_parametros}")

#    for i, valor in enumerate(args):
#        print (f"Posição = {i}, valor = {valor}")
#print("\nChamada 1")
#imprimir_parametros("São Paulo", 10, 23.78, "João")
#print("\nChamada 2")
#imprimir_parametros(10, "São Paulo")

# EXEMPLO 13
#def imprimir_parametros(**kwargs):
#    print(f"Tipo de objeto recebido = {type(kwargs)}\n")
#    qtde_parametros = len(kwargs)
#    print(f"Quantidade de parâmetros = {qtde_parametros}")

#    for chave, valor in kwargs.items():
#        print(f"variável = {chave}, valor = {valor}")
#print("\nChamada 1")
#imprimir_parametros(cidade="São Paulo", idade= 33, nome= "Lord Quasi")
#print("\nChamada 2")
#imprimir_parametros(desconto=10, valor=100)

# EXEMPLO 14
#(lambda x: x + 1)(x=3)

# EXEMPLO 15
#(lambda x, y: x + y)(x=3, y=2)

# EXEMPLO 16
#somar = lambda x, y:x + y
#somar(x=5, y=3)
print("Feito no PyCharm")