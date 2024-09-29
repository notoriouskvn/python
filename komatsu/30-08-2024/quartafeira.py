
notas_alunos = {
    "Fernando Collor": {"Matemática": 85, "Física": 90, "Química": 70},
    "Maria Betânia": {"Matemática": 55, "Física": 65, "Química": 95},
    "Arnaldo César Coelho": {"Matemática": 75, "Física": 100, "Química": 80}}


def media(aluno):
    if aluno in notas_alunos:
        disciplinas = notas_alunos[aluno]
        media = sum(disciplinas.values()) / len(disciplinas)
        return media
    else:
        return print("Erro crítico, ferrou...")

notas_alunos["Regina Cazé"] = {"Matemática": 85, "Física": 30, "Química": 45} # Adicionando um aluno
print("Após adicionar Regina Cazé:")
print(notas_alunos)

notas_alunos["Fernando Collor"]["Física"] = 75 # Atualizando nota
print("\nApós atualizar a nota do Fernando Collor:")
print(notas_alunos)

notas_alunos.pop("Maria Betânia") # Removendo um aluno
print("\nApós remover Maria Betânia:")
print(notas_alunos)

print("\nIterando sobre os estudantes e suas notas:")
for aluno, disciplinas in notas_alunos.items(): #chaves e valores;
    print(f"Estudante: {aluno}")
    for disciplina, nota in disciplinas.items(): #chaves e valores;
        print(f"  {disciplina}: {nota}")

media_collor = media("Fernando Collor")
if media_collor is not None:
    print(f"\nA média das notas do Fernando Collor é: {media_collor}")
else:
    print("\nEstudante não encontrado.")
