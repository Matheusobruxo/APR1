pessoas={ '11111111111' : ['Maria','maria@maria.com'],
 '22222222222' : ['Joaquim','joaquim@joaquim.com'],
 '33333333333' : ['João','joão@joão.com']
 }

# pessoas= {}
# veiculos={}
# while True:
#     cpf = input("Digite o cpf do cidadão: ")
#     if cpf == "x":
#         break
#     nome = input("Digite o nome do cidadão: ")
#     email = input("Digite o email do cidadão: ")
    # pessoas[cpf]=[nome, email]

veiculos={'ABC1234' : ['VW/GOL',2012,'22222222222'],
 'ZAP9898' : ['GM/Astra',2010,'33333333333'],
 'XYZ1010' : ['Fiat/Argo',2022,'11111111111'],
 'AAA5678' : ['Ford/Ranger',2024,'11111111111']
 }


# while True:
#     placa = input("Digite a placa: ")
#     if placa.lower() == "x":
#         break
#     marca = input("Digite a marca do veiculo: ")
#     ano = int(input("Digite o ano do veiculo: "))
#     cpf_proprietario = int(input("Digite o cpf do proprietario: "))
#     veiculos[placa]= [marca, ano, cpf_proprietario]


search_placa = input("Digite uma placa: ")
for k,v in veiculos.items():
    if k==search_placa:
        print(f"O proprietario é o {pessoas[v[2]][0]}")

for k,v in pessoas.items():
    print(f"Carros da pessoas {v[0]}:")
    for chave, valor in veiculos.items():
        if k ==valor[2]:
            print(f"Veiculo placa: {chave}, marca: {valor[0]}, ano: {valor[1]}")


        