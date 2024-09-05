soma_idades = 0
cont_pessoas = 0
menor_altura = 10
pessoas_peso_altura = 0
pessoas_altas=0
pessoas_idade_1030=0
while True:
    idade = int(input("Digite a idade do cidadão: "))
    # Se idade < 0 Para o laço
    if idade < 0:
        break
    # soma as idades
    soma_idades += idade

    altura = float(input("Digite a altura do cidadão: "))
    # Verifica a menor altura
    if menor_altura > altura:
        menor_altura = altura
    
    peso = float(input("Digite o peso do cidadão: "))
    # Verifica e conta pessoas com peso > 90kg ou altura < 1.5m
    if peso > 90 or altura < 1.5:
        pessoas_peso_altura += 1

    # Verifica altura > 1.90
    if altura > 1.90:
        pessoas_altas += 1
        # Verifica entre as pessoas com 1.90 com idade > 10 e < 30
        if idade >= 10 and idade <=30:
            pessoas_idade_1030 += 1
    
    #conta pessoas com idade > 0
    cont_pessoas+=1

if pessoas_altas > 0:
    porcentagem_pessoas_pessoas_altas = (pessoas_idade_1030/pessoas_altas)*100
else:
    porcentagem_pessoas_pessoas_altas = 0

print(f"A média das idades: {soma_idades/cont_pessoas}")
print(f"A menor altura: {menor_altura}")
print(f"Pessoas com peso > 90 ou altura < 1.5: {pessoas_peso_altura} ")
print(f"Percentual de pessoas com idade entre 10 e 30 anos entre as pessoas com > 1.90: {porcentagem_pessoas_pessoas_altas}% ")