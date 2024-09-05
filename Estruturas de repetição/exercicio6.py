qtde_alunos = 0
maior_nota = 0
menor_nota=10
while True:
    nota= int(input("Digite a nota do pião: "))
    if(nota<0):
        break
    if(nota> maior_nota):
        maior_nota= nota
    if(nota<menor_nota):
        menor_nota= nota
    qtde_alunos+=1
    

print("Maior nota {}, menor nota {}, quantidade de alunos {}". format(maior_nota, menor_nota, qtde_alunos))
