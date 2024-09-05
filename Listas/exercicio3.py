#n = int(input("Digite o tamanho de uma matriz quadradada de N x N: "))
n=3
numero = 1
matriz=[]
for i in range(n):
    matriz.append([0]*n)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = numero
        numero = numero+1

for i in range(n):
    for j in range(i,n):
        print(matriz[i][j])