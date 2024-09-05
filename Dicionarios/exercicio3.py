# vendas={}
vendas={'geladeira':[3000.00,2],
 'fogão':[900.00,2],
 'sofá':[2500.00,5]
 }
# qtde_produtos= int(input("qtde de produtos: "))
faturamento_geral=0
mais_vendido=0

# for i in range(qtde_produtos):
#     prod = input(f"Digite o nome do {i+1}º produto: ")
#     unidade = float(input("Digite o preço unitário do produto: "))
#     qtde_vendida = int(input("Digite q qtde de produtos vendidos: "))
#     vendas[prod] =[unidade, qtde_vendida]

print("Total por produto")

for k, v in vendas.items():
    total_produto_faturado = v[0] * v[1]
    faturamento_geral+= total_produto_faturado
    print(f"{k}: {total_produto_faturado}")

for k,v in vendas.items():
    qtde_vendas_K= v[1]
    if qtde_vendas_K> mais_vendido:
        mais_vendido= qtde_vendas_K
        nome_prod_mais_vendido= k
        
print(f"Faturamento total: {faturamento_geral}")
print(F"O produto mais vendido foi {nome_prod_mais_vendido}: {qtde_vendas_K} unidades")




    

