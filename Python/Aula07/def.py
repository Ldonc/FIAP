# for char in "danilo":
#     print(char)

#contando vogais do nome danilo
# vogais = 0
# for char in "danilo":
#     if char in ["a","e","i","o","u"]:
#         vogais += 1
# print(vogais)


# lista = [3,True,7.2,"nome",[]]
# for elem in lista:
#     print(elem)
# print()
# for i in range(len(lista)):
#     print(lista[i])


# lista = [3,True,7.2,"nome",[]]
# for elem in lista:
#     elem = 1
# print(lista)
# for i in range(len(lista)):
#     lista = [1]
# print(lista)


# lista = [3,True,7.2,"nome",[]]
# for i in range(len(lista)):
#     print(f"{lista[i]} = {lista[i]}")

#somando números da lista
# numeros = [5,1,7,9,0,2]
# soma = 0
# for num in numeros:
#     soma += num
# print(soma)

# outra forma de somar os números
# soma = 0
# for i in range(len(numeros)):
#     soma += numeros[i]
# print(soma)


# alunos = ['Lucas','Samuel','Victor','João','Cristian','Rodrigo','Rafael']
# notas = [8,6,4,8,9,2,3]
# for i in range(len(notas)):
#     if notas[i] >= 6:
#         print(f"O {alunos[i]} passou com {notas[i]}")
#     else:
#         print(f"O {alunos[i]} não passou {notas[i]}")


# def verifica_numero(msg):
#     numero = input("msg")
#     while not numero.isnumeric():
#         numero = input("msg")
#     numero = int(numero)
#     return numero
#
# qtd = verifica_numero("Quantos números você vai colocar na lista")
# #ano = verifica_numero("Diga seu ano de nascimento")
# lista = []
# while len(lista) < qtd:
#     num = verifica_numero(f"Diga o {len(lista)+1}º número: ")
#     lista.append(num)
#     print(lista)


# opcoes = ['Pérgola','Sangue de Boi','Salton']
# escolha = input("Qual vinho você quer?\n->")
# while not escolha in opcoes:
#     escolha = input("Qual vinho você quer?\n->")

# opcoes = ['Pérgola','Sangue de Boi','Salton']
# def forca_opcao(msg,lista_opcoes):
#     escolha = input(msg)
#     while not escolha in lista_opcoes:
#         escolha = input(msg)
#     return escolha

# def forca_opcao(msg,lista_opcoes):
#     opcoes = "," .join(lista_opcoes)
#     escolha = input(f"{msg}\n{opcoes}\n->")
#     while not escolha in lista_opcoes:
#         escolha = input(f"{msg}\n{opcoes}\n->")
#     return escolha
# vinhos = ['Pérgola','Sangue de Boi','Salton']
# vinho = forca_opcao("Qual vinho você quer?",vinhos)
# print(f"Você escolheu o {vinho}")
# opcoes = ["s","n"]
# continuar = forca_opcao("Você quer continuar?(s/n)",opcoes)
# print(f"Você disse {continuar}")


# calculando uma média usando função
# def acha_media(lista_numeros):
#     soma = 0
#     for num in lista_numeros:
#         soma += num
#     media = soma/len(lista_numeros)
#     return media
#
# lista = [3,4,7,9,8,2]
# media = acha_media(lista)
# print(media)
# lista2 =[1,2,3]
# media = acha_media(lista2)
# print(media)


#achando números pares usando função
# def conta_pares(lista):
#     pares = 0
#     for num in lista:
#         if num%2 == 0:
#             pares += 1
#     return pares
# lista = [5,1,8,7,2,3]
# print(conta_pares(lista))


#achando maior número da lista usando função e seu respectivo valor
# def acha_maior(lista):
#     indice_maior = 0
#     maior = lista[indice_maior]
#     for i in range(len(lista)):
#         if lista[i] > maior:
#             maior = lista[i]
#             indice_maior = i
#     return indice_maior
# carros = ['up','fox','polo','gol']
# precos = [10,1000,30,50]
# local_maior = acha_maior(precos)
# print(carros[local_maior],precos[local_maior])


def forca_opcao(msg,lista_opcoes):
    opcoes = "," .join(lista_opcoes)
    escolha = input(f"{msg}\n{lista_opcoes}\n->")
    while not escolha in lista_opcoes:
        escolha = input(f"{msg}\n{lista_opcoes}\n->")
    return escolha
carros = ["BMW M3","Porche Panamera","Lamborguini Urus","La Ferrari"]
precos = [750.000,1000.000,3000.000,40000.000]
escolha = forca_opcao("Qual carro te interessa?",carros)
def acha_index(lista,elem):
    for i in range(len(carros)):
        if lista [i] == elem:
            return i
indice_escolha = acha_index(carros,escolha)
print(f"O {escolha} custa {precos[indice_escolha]}")


#.join em função
def join(lista_str,sep):
    ajuntado = lista_str[0]
    for i in range(len(lista_str)):
        ajuntado += sep + lista_str[i]
    return ajuntado