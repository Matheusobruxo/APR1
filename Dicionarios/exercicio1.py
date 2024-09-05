n = int(input("Qtde alunos: "))
dicionario = {}
for i in range(n):
    aluno = input("Digite o nome do aluno: ")
    notas = []
    for j in range(3):
        notas.append(float(input(f"Digite a nota {j+1}: ")))
    dicionario[aluno]= notas

for k in dicionario.keys():
    print(f"Aluno: {k}")

for v in dicionario.values():
    print(f"Notas: {v}")

for k, v in dicionario.items():
    print(f"chave: {k} / valor: {v}")