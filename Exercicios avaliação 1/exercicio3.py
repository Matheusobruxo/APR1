cont_xnum = 0
cont_maior = 0
cont_menor = 0
lista_x = []
n = int(input("N: "))
lista = [0]*n

for i in range(len(lista)):
    lista[i] = int(input(f"Digite um numero {i+1}: "))

# Solicita o número X
x = int(input("X:"))
for i in range (len(lista)):
    if lista[i] == x:
        cont_xnum += 1
    if lista[i] > x:
        cont_maior += 1
    if lista[i] < x:
        cont_menor += 1
    lista_x.append(lista[i]*x)

print(f"Há: {cont_xnum} números == x")
print(f"Há {cont_maior} números > x")
print(f"Há {cont_menor} números > x")
print(f"Lista antiga: {lista}")
print(f"Nova lista: {lista_x}")
