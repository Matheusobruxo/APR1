peso = float(input("peso: "))
altura = float(input("altura: "))
imc = peso / (altura **2)
print(imc)

if(imc < 18.5):
    print("Abaixo do peso")
elif(imc< 24.9):
    print("Peso normal")
elif(imc< 29.9):
    print("Acima do peso")
elif(imc< 34.9):
    print("Obesidade I")
elif(imc< 39.9):
    print("Obesidade II")
else:
    print("Obesidade III")
