n = 3
m= 3
numero = 1
matriz = []
soma_diagonal_principal = 0
pares = 0
impares= 0
media_colunas = [0]*m
for i in range(n):
    matriz.append([0]*m)

for i in range(n):
    for j in range(len(matriz[i])):
        matriz[i][j] = numero
        numero = numero+1
#        matriz[i][j]= int(input("Digite o numero que quer colocar na posição [{}] [{}]: ".format(i,j)))

for i in range(n):
    for j in range(len(matriz[i])):
        if i ==j:
            soma_diagonal_principal += matriz[i][j]

for i in range(n):
    for j in range(len(matriz[i])):
        numero = matriz[i][j]
        if numero %2 == 0:
            pares+=1
        else:
            impares+=1

for i in range(m):
    for j in range(len(matriz)):
        media_colunas[j] = media_colunas[j] + matriz[i][j] 


for i in range(len(media_colunas)):
    media_colunas[i] = media_colunas[i] /m


print(matriz)
print(soma_diagonal_principal)
print(pares)
print(media_colunas)