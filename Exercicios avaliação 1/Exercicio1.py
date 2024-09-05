start = int(input("Digite o numero inicial da PA: "))
razao = int(input("Digite a razão da PA: "))
qtde_termos = int(input("Digite a quantidade de termos: "))

for i in range(qtde_termos):
    print("Termo {}: {}".format(i+1,start))
    start+=razao
