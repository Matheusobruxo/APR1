def num_pares(lista):
    if lista == []:
        return 0
    else:
        sublista= lista[0]
        contador = 0
        for num in sublista:
            if num %2 == 0:
                contador+=1
        return contador + num_pares(lista[1:])

def main():
    print(num_pares([[4,6,5,1],[5,3,9],[],[4,0,10]]))

main()    