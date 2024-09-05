n = int(input("N:"))
lista = list(range(2,n+1))
i = 0

while i < len(lista):
    comparador = lista[i]
    j = i+1
    while j < len(lista):
        if lista[j] % comparador == 0:
            lista.remove(lista[j])
        else:
            j+=1
    i+=1

print(lista)