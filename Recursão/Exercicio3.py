def contar(lista, item):
    if len(lista)==0:
        return 0
    if lista[0]== item:
        return 1 + contar(lista[1:], item)
    else:
        return 0+ contar(lista[1:], item)



def main():
    l = [3, 3, 3, 5, 10, 5]
    i = 3
    print(contar(l,i))

main()