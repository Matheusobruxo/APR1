def criar_matriz(N, M):
    matriz = []
    for i in range(N):
        linha = []
        for j in range(M):
            valor = int(input(f"Digite o valor para a posição [{i+1},{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def somar_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma

def mostrar_matriz(matriz):
    for linha in matriz:
        print(linha)

def calcular_media(matriz):
    medias = []
    for linha in matriz:
        total = 0
        for valor in linha:
            total += valor
        media = total / len(linha)
        medias.append(media)
    return medias

def main():
    N = 2
    M = 3
    matriz = criar_matriz(N, M)
    print("Matriz:")
    mostrar_matriz(matriz)
    print("Soma da diagonal principal:", somar_diagonal(matriz))
    print("Média de cada linha:", calcular_media(matriz))

main()
