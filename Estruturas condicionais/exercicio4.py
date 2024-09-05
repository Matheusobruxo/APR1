x = int(input("Digite o limite da km v1: "))
v1 = float(input("Digite a bandeira v1: "))
v2 = float(input("Digite a bandeira v2: "))
p = int(input("Digite a quantidade de km percorridos: "))

if(p >x):
    total = p *v2
else:
    total = p* v1

print("O valor total é de {}".format(total))