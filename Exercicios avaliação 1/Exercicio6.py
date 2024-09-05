M = int(input("Digite o número de escolas de samba: "))
N = int(input("Digite o número de categorias: "))
K = int(input("Digite o número de jurados: "))
notas = [] 


for i in range(M):
    escola = []  
    for j in range(N):
        categoria = []  
        for k in range(K):
            nota = float(input(f"Digite a nota do jurado {k+1} para a categoria {j+1} da escola {i+1}: "))
            categoria.append(nota)
        escola.append(categoria)
    notas.append(escola)
    
for i in range(M):
    soma = 0
    for j in range(N):
        for k in range(K):
            soma += notas[i][j][k]
    print(f"A escola de samba {i+1} obteve o total de {soma} pontos")

for i in range(M):
    print(f"Escola de samba {i+1}:")
    for j in range(N):
        soma = 0
        for k in range(K):
            soma += notas[i][j][k]
        media = soma / K
        print(f"Média na categoria {j+1}: {media}")
