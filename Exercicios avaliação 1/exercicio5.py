m = int(input("Digite m: "))
n = int(input("Digite n: "))
lista = []
lista_transposta = []

for i in range(m):
    #adiciona as linhas de n
    lista.append([])
    for j in range(n):
        lista[i].append(int(input("numero: ")))


for i in range(len(lista[0])):
    linha= []
    for sublista in lista:
        linha.append(sublista[i])
    lista_transposta.append(linha)

print(lista)
print(lista_transposta)
