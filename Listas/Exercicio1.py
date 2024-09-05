temperaturas_semana = [0] * 7
media = 0
t_acima = 0
for i in range(len(temperaturas_semana)):
    temperaturas_semana[i] = float(input("Digite a temperatura do dia {}: ".format(i)))

for t in temperaturas_semana:
    media = media + t
media = media/len(temperaturas_semana)

for t in temperaturas_semana:
    if t > media:
        t_acima = t_acima+1
print("Media de temperaturas: {:.2f}".format(media))
print("Quantidade acima da média: {}".format(t_acima))