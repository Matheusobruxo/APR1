numero = int(input("Digite um numero: "))
if(numero== 0):
    print("O numero {} é nulo".format(numero))
elif(numero<0):
    print("O número {} negativo!".format(numero))
elif(numero%2 == 0):
    print("O numero {} é par".format(numero))
else:
    print("O numero {} é impar".format(numero))
