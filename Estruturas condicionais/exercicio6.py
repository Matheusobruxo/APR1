preco_gasolina= 6.00
preco_etanol= 3.00
tipo_combustivel= int(input("Digite o tipo do combustível (1- Gasolina | 2- Etanol): "))
qtde_abastecida = float(input("Digite a quantidade abastecida: "))

if(tipo_combustivel == 1):
    if(qtde_abastecida < 20):
        preco_final = 0.96 * (preco_gasolina * qtde_abastecida)
    else:
        preco_final = 0.94 * (preco_gasolina * qtde_abastecida)
else:
    if(qtde_abastecida < 20):
        preco_final = 0.97 * (preco_etanol * qtde_abastecida)
    else:
        preco_final = 0.95 * (preco_etanol * qtde_abastecida)
preco_final
print(f"O valor a ser pago é R${preco_final: .2f}")