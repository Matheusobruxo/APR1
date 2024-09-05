soma_idades = 0
qtde_maiores21 = 0
qtde_idosos=0
pessoas = 0
while True:
    idade= int(input("Digite a nota do pião: "))
    if(idade<0):
        break
    if(idade> 21):
        qtde_maiores21+=1
    if(idade>65):
        qtde_idosos+=1
    soma_idades+=idade
    pessoas+=1
    

print("Maiores de 21 {}, idosos {}, idade média {}". format(qtde_maiores21, qtde_idosos, soma_idades/pessoas))
