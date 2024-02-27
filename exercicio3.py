for i in range(5):
    numero =int(input("Digite um número: "))
    if i == 0:
        maior_num = numero
    else:
        if maior_num < numero:
            maior_num = numero
print(maior_num)