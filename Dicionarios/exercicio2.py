meses={1: 50,
    2: 51,
    3: 52,
    4: 53,
    5: 54,
    6: 55,
    7: 56,
    8: 57,
    9: 58,
    10: 59,
    11: 60,
    12: 61
}
qtde_meses=12
media=0
menos_grana= 9000000
mais_grana = 0
# for i in range (qtde_meses):
#     mes= input("Digite o mês: ")
#     gastos= int(input(f"Digite o gasto do mês {mes}: "))
#     meses[mes]=gastos

for mes in meses.values():
    media = media + mes

for mes in meses.values():
    if menos_grana > mes:
        menos_grana = mes
    if mais_grana < mes:
        mais_grana = mes
print(meses)
print(media/qtde_meses) 
print(menos_grana)
print(mais_grana)
