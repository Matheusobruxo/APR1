qtd_divisores = 0
n= int(input("Digite um numero inteiro: "))
for i in range(1, n+1):
    if(n%i==0):
        qtd_divisores+=1
if(qtd_divisores==2):
    print("Primo")
else:
    print("Primo não")
