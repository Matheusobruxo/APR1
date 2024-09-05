def ler_dados_aluno():
    prontuario = input("Digite o prontuário do aluno: ")
    nome = input("Digite o nome do aluno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Digite a nota {i+1} do aluno: "))
        while nota < 0 or nota > 10:
            print("Nota inválida. Digite um número entre 0 e 10.")
            nota = float(input(f"Digite a nota {i+1} do aluno: "))
        notas.append(nota)
    return (prontuario, nome, notas)

def inserir_dados_no_dicionario(tupla):
    prontuario, nome, notas = tupla
    return {prontuario: [nome] + notas}

def gravar_dados_no_arquivo(tupla):
    prontuario, nome, notas = tupla
    notas_str = ''
    for nota in notas:
        notas_str += '\t' + str(nota)
    with open("notas_apr1.txt", "a") as arquivo:
        arquivo.write(f"{prontuario}\t{nome}{notas_str}\n")

def calcular_media(notas):
    total = 0
    for nota in notas:
        total += nota
    return total / len(notas)

def situacao_aluno(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "IFA"
    else:
        return "Reprovado"

def mostrar_alunos_e_notas():
    with open("notas_apr1.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split('\t')
            if len(dados) > 0:
                prontuario = dados[0]
                nome = dados[1]
                notas = {}
                for i in range(2, len(dados)):
                    nota = float(dados[i])
                    notas.append(nota)
                media = calcular_media(notas)
                situacao = situacao_aluno(media)
                print(f"Prontuário: {prontuario}, Nome: {nome}, Notas: {notas}, Média: {media:.2f}, Situação: {situacao}")
        return

def pesquisar_aluno(prontuario):
    with open("notas_apr1.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split('\t')
            if dados[0] == prontuario:
                nome, notas = dados[1], list(map(float, dados[2:]))
                media = calcular_media(notas)
                situacao = situacao_aluno(media)
                print(f"Prontuário: {prontuario}, Nome: {nome}, Notas: {notas}, Média: {media:.2f}, Situação: {situacao}")
                return
        print("Aluno não cadastrado")

def exibir_menu():
    print("1 - Cadastrar aluno e notas")
    print("2 - Mostrar alunos e notas")
    print("3 - Pesquisar aluno")

def main():
    dicionario = {}
    while True:
        exibir_menu()
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            tupla = ler_dados_aluno()
            dicionario.update(inserir_dados_no_dicionario(tupla))
            gravar_dados_no_arquivo(tupla)
        elif opcao == 2:
            mostrar_alunos_e_notas(dicionario)
        elif opcao == 3:
            prontuario = input("Digite o prontuário do aluno a ser pesquisado: ")
            pesquisar_aluno(prontuario)
        else:
            print("Opção inválida. Tente novamente.")

main()
