p = int(input("Digite a posição da portinha P: "))
r = int(input("Digite a posição da portinha R: "))

if(p==0):
    caminho = "Caminho C"
elif(r == 0):
    caminho = "Caminho B"
else:
    caminho = "Caminho A"

print(f"A bolinha foi pelo caminho {caminho}")