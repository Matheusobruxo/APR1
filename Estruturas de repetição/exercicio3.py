chico = 1.5
ze = 1.1
i=0 

while True:
    chico += 0.02
    ze += 0.03
    i+=1
    if(ze > chico):
        print("Demoraram {} anos!".format(i))
        break