#Ex 1
n1 = input("Diga um número \n->")
n2 = input("Diga outro número \n->")
if n1 > n2 :
    print(n1)
else :
    print(n2)

#Ex 2
ano = int(input("Diga em que ano você nasceu.\n->"))
if ano >= 2009 :
    print("Não pode votar!!!")
else:
    print("Você já pode votar, vote com responsabilidade!!!")

#Ex 3
senha = input("Digite sua senha.\n->")
if senha == "1234" :
    print("ACESSO PERMITIDO")
else :
    print("ACESSO NEGADO")

#Ex 4
quantidade = int(input("Quantas maçãs você gostaria de comprar?\n->"))
if quantidade < 12 :
    print(f"Sua compra ficou no valor de R${0.30 * quantidade}")
else :
    print(f"Sua compra ficou no valor de R${0.25 * quantidade}")

#Ex 5
#Ex 5
n1 = int(input("Diga um número.\n->"))
n2 = int(input("Diga outro número.\n->"))
n3 = int(input("Diga mais um número.\n->"))

if n1 > n2 and n1 > n3:
    aux = n1
    n1 = n3
    n3 = aux
elif n2 > n3:
    aux = n2
    n2 = n3
    n3 = aux
if n2 < n1:
    aux = n1 
    n1 = n2
    n2 = aux
print(n1,n2,n3)

#Outra forma de resolver
n1 = int(input("Diga um número.\n->"))
n2 = int(input("Diga outro número.\n->"))
n3 = int(input("Diga mais um número.\n->"))
maior = n1
if n2 > maior:
    maior = n2
if n3 < maior:
    maior = n3
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
meio = n1 + n2 + n3 - menor - maior
print(n1,n2,n3)


#Ex 6
masculino = "2"
feminino = "1"
print("mulher ---> 1")
print("homem ---> 2")
sexo = input("Qual seu sexo?\n->")
altura = float(input("Qual sua altura\n->"))
if sexo == "2" :
    print(f"Seu peso ideal é {(72.7 * altura)- 58}")
if sexo == "1" :
    print(f"Seu peso ideal é {(62.1 * altura)- 44.7}")
    
    
#Ex 7
lados = input("Qual o número de lados do seu polígono?\n->")
medida = int(input("Qual a medida dos lados?\n->"))
perimetro = lados*medida
if lados == "3":
    print(f"Seu polígono é o triângulo e seu perímetro é igual a {perimetro}cm")
elif lados == "4":
    print(f"Seu polígono é o quadrado e seu perímetro é igual a {perimetro}cm")
else:
    print(f"Seu polígono é o pentágono e seu perímetro é igual a {perimetro}cm")


#Ex 8
lados = int(input("Qual o número de lados do seu polígono?\n->"))
if lados > 5:
    print("POLÍGONO NÃO IDENTIFICADO")
elif lados < 3:
    print("NÃO É POLÍGONO")
else:
    medida = float(input("Qual a medida dos lados?\n->"))
    perimetro = lados*medida
    if lados == 3:
        forma = "triângulo"
    elif lados == 4:
       forma = "quadrado"
    else:
        forma = pentágono"
        print(f"Seu polígono é o {forma} e seu perímetro é igual a {perimetro}cm")


#Ex 9
n1 = int(input("Diga um número!"))
n2 = int(input("Diga outro número!!"))
n3 = int(input("Diga mais um número!!!"))
if n1 > n2 and n1 > n3:
    print(f"O {n1} é o maior")
elif n2 > n3:
    print(f"O {n2} é o maior")
else:
    print(f"O {n3} é o maior")

#Outra forma de resolver
maior = n1
if n2 > maior:
    maior: n2
if n3 > maior:
    maior = n3
print(f"O maior número é {maior}")


#Ex 10
lado1 = int(input("Digite o tamanho de um dos lados do seu triângulo!\n->"))
lado2 = int(input("Digite o tamanho de um dos lados do seu triângulo!!\n->"))
lado3 = int(input("Digite o tamanho de um dos lados do seu triângulo!!!\n->"))
if lado1 == lado2 and lado2 == lado3:
    print("Seu triângulo é equilátero!!!")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Seu triângulo é isóceles!!!")
else:
    print("Seu triângulo é escaleno!!!")


#Ex11
angulo1 = int(input("Digite um ângulo do seu triângulo!\n->"))
angulo2 = int(input("Digite outro ângulo do seu triângulo!!\n->"))
angulo3 = int(input("Digite mais um ângulo do seu triângulo!!!\n->"))
if angulo1 + angulo2 + angulo3 == 180:
    if angulo1== 90 or angulo2 == 90 or angulo3 == 90:
        print("Seu triângulo é rêtangulo!!!")
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        print("Seu triângulo é obtusângulo!!!")
    else:
        print("Seu triângulo é escaleno!!!")
else:
    print("Esses ângulos não formam um triângulo!!!!!")