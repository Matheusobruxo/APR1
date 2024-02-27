lado_a = 5
lado_b = 5
lado_c = 5

if((lado_a + lado_b) > lado_c and (lado_a + lado_c) > lado_b and (lado_c + lado_b) > lado_a):
    if(lado_a == lado_b or lado_a == lado_c or lado_b == lado_c):
        if(lado_a == lado_b and lado_b == lado_c):
            print("Triangulo equilátero! ")
        else:
            print("Triângulo isóceles! ")
    else:
        print("Triângulo escaleno! ")
          
else:
     print("não é uym triangulo! ")