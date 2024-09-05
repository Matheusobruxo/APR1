nota_p1 = float(input("Digite a nota da P1: "))
nota_p2 = float(input("Digite a nota da P2: "))
nota_l1 = float(input("Digite a nota da Lista 1: "))
nota_l2 = float(input("Digite a nota da Lista 2: "))
media_listas= (nota_l1+nota_l2)/ 2
media_final= (nota_p1*0.4) + (nota_p2*0.4) + (media_listas * 0.2)

if(media_final<4):
    print(f"Reprovado, lanço um {media_final:.2f}, tranca ae irmão!")
elif(media_final<6):
    print(f"Ta de IFA irmão :/, lanço um {media_final:.2f}! ")
else:
    print(f"Aprovadão meu parceiro, lanço um {media_final:.2f}! ")