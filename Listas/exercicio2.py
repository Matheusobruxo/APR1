salarios = []
media = 0

while True:
    salario = float(input("Digite o valor do salario: R$ "))
    if salario < 0:
        break
    else:
        media += salario
        salarios.append(salario)

media = media / len(salarios)

for i in range(len(salarios)):
    salario = salarios[i]
    print("Salario atual do funcionario {}: R$ {}.".format(i+1,salarios[i]))
    if salario > media:
        salarios[i]= salario * 1.05
        print("Novo salario R$ {}.".format(salarios[i]))
    else:
        salarios[i]= salario * 1.10
        print("Novo salario R$ {}.".format(salarios[i]))
