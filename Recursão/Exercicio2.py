def maior(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        if lista[0] > maior(lista[1:]):
            return lista[0]
        else:
            return maior(lista[1:])
        
def main():
    num = [1,2,3,4,5,6,7,8,9,10]
    print(maior(num))

main()