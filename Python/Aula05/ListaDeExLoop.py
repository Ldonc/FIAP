#Ex 1
# while True:
#     nota = input("Digite sua nota:\n->")
#     if nota.isnumeric():
#         nota = int(nota)
#         if nota < 0 or nota > 10:
#             break
# print(f"Sua nota foi {nota}")


#Ex 2
# nome = input("Digite seu nome: \n->")
# while len(nome) < 3:
#     nome = input("Digite seu nome: \n->")
    
# while True:
#     idade = input("Diga sua idade:\n->")
#     if idade.isnumeric():
#         idade = int(idade)
#         if idade > 0 and idade > 150:
#             break
#         print(f"{idade} está fora do intervalo 0 a 150")
#     else:
#         print("Deve ser digitado um número!")
        
# salario = input("Diga seu salário:\n->")
# while not salario.isnumeric():
#     salario = input("Diga seu salário:\n->")
# salario = int(salario)

# sexo = input("Diga seu sexo:\n->")
# while sexo != "f" and sexo != "m":
#     sexo = input("Diga seu sexo:\n->")
    
# estado_civil = input("Diga seu estado civil:\n->")
# while not (estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d"):
#     estado_civil = input("Diga seu estado civil:\n->")


#Ex 3
# populacao_A = 80000
# populacao_B = 200000
# taxa_A = 0.03
# taxa_B = 0.015
# anos = 0
# while populacao_A <= populacao_B:
#     populacao_A = populacao_A + (populacao_A * taxa_A)
#     pupulacao_b = populacao_B + (populacao_B * taxa_B)
#     anos += 1
# print(f"Para a população_A alcançar a população_B serão necessários {anos} anos.")

#Ex 3 outra resolução
# a = 80
# b = 200
# t = 0
# while a < b:
#     a *= 1.03
#     b *= 1.015
#     t += 1
#     print(t)


#Ex 4
# num_1 = int(input("Informe um número:\n->"))
# num_2 = int(input("Informe um número:\n->"))
# num_3 = int(input("Informe um número:\n->"))
# num_4 = int(input("Informe um número:\n->"))
# num_5 = int(input("Informe um número:\n->"))
# print(f"A soma dos números é {num_1 + num_2 + num_3 + num_4 + num_5} e sua média é {(num_1 + num_2 + num_3 + num_4 + num_5) / 2} .")

#Ex 4 outra resolução
# i = 0
# soma = 0
# while i < 5:
#     nota = input(f"Diga sua {i+1}º nota: ")
#     while not nota.isnumeric():
#         nota = input(f"Diga sua {i+1}º nota: ")
#         soma += nota
#         i += 1
#     media = soma/i
# print(media)
        

#Ex 5
# num_1 = input("Digite um número inteiro:\n->")
# num_2 = input("Digite um número inteiro:\n->")
# while not (num_1.isnumeric() == True and num_2.isnumeric() == True):
#     num_1 = input("Digite um número inteiro:\n->")
#     num_2 = input("Digite um número inteiro:\n->")
# num_1 = int(num_1)
# num_2 = int(num_2)
# if num_1 < num_2:
#     inicio = num_1 + 1
#     fim = num_2
# else:
#     inicio = num_2 + 1
#     fim = num_1
# print("Números no intervalo entre", inicio - 1, "e", fim, ":")
# while inicio < fim:
#     print(inicio)
#     inicio += 1

#Ex 05 outra resolução
# a = input("Diga um número")
# while not a.isnumeric()
#     a = input("Diga um número")
# a = int(a)
# b = input("Diga um número")
# while not b.isnumeric()
#     b = input("Diga um número")
# b = int(b)

# if b < a:
#     aux = a
#     a = b 
#     b = aux 

# while a <= b:
#     print(a, end="")
#     a += 1     

#Ex 6
# nome = input("Digite seu nome:\n-> ")
# senha = input("Digite sua senha:\n-> ")
# while nome == senha:
#     print(f"ERRO SENHA INVÁLIDA! ")
#     nome = input("Digite seu nome:\n-> ")
#     senha = input("Digite sua senha:\n-> ") 
# print("SENHA VÁLIDA!")


#Ex 7
# numero = int(input("Digite o número que gostaria de saber a tabuada:\n->"))
# if 1 <= numero <= 10:
#     print(f"Tabuada do {numero}:")
#     multiplicador = 1
#     while multiplicador <= 10:
#         resultado = numero * multiplicador
#         print(f"{numero} x {multiplicador} = {resultado}")
#         multiplicador += 1
# else:
#     print("Este número é inválido")


#Ex 7.1
# numero = 1
# while numero <= 10 :
#     print(f"Tabuada do {num}:")
#     mult = 1
#     while mult <= 10:
#         print(f"{num}*{mult} = {num*mult}")
#         mult += 1
#     print()
#     numero += 1
    
    
#Ex 8
# a = 0
# b = 1
# contador = 2

# print("Termo 1:", a)
# print("Termo 2:", b)

# while contador <= 90:
#     c = a + b
#     print(f"Termo {contador + 1}: {c}")
#     a = b
#     b = c
#     contador += 1


#Ex 8 outra ressolução
# a = 1
# b = 1
# print(a,b,end=" ")
# i = 2
# while i < 10:
#     c = a + b
#     print(c,end=" ")
#     a = b 
#     b = c
#     i += 1


#Ex 9
# pares = ""
# impares = ""

# contador = 0
# while contador < 10:
#     num = int(input(f"Digite o {contador + 1}º número: "))
    
#     if num % 2 == 0:
#         pares += str(num) + " "
#     else:
#         impares += str(num) + " "
    
#     contador += 1

# print("\nNúmeros pares:", pares)
# print("Números ímpares:", impares)


#Ex 10
# num = int(input("Digite um número inteiro para calcular o fatorial:\n-> "))

# if num < 0:
#     print("Fatorial não é definido para números negativos.")
# else:
#     fatorial = 1
#     contador = 1

#     while contador <= num:
#         fatorial *= contador
#         contador += 1

#     print(f"O fatorial de {num} é {fatorial}")


#Ex 11
# num = int(input("Digite um número inteiro:\n-> "))
# divisores = 0
# contador = 1

# while contador <= num:
#     if num % contador == 0:
#       divisores += 1
#     contador += 1

# if divisores == 2:
#     print(f"{num} é um número primo.")
# else:
#     print(f"{num} não é um número primo.")


#Ex 12
# n = int(input("Quantas notas você quer informar?\n-> "))
# soma = 0
# contador = 0

# while contador < n:
#     nota = float(input(f"Digite a {contador + 1}ª nota:\n-> "))
#     soma += nota
#     contador += 1

# media = soma / n
# print(f"\nA média aritmética das {n} notas é: {media:2f}")


# Ex 13
# salario = 1000
# ano = 1995
# taxa = 0.015
# while ano < 2000 :
#     aumento = 1 + taxa
#     salario *= aumento
#     taxa *= 2
#     ano += 1
#     print(salario)


#Ex 13 parte 2
# i = 0
# while i < 10:
#     if i %2 == 1:
#         i += 1
#         continue
#     print(i)
#     i += 1


#Ex 14
# intervalo_1 = 0
# intervalo_2 = 0
# intervalo_3 = 0
# intervalo_4 = 0
#
# while True:
#     num = input("Diga um número:\n->")
#     while not num.isnumeric():
#         print("Inválido")
#         num = input("Diga um número:\n->")
#     num = int(num)
#     if num < 25:
#         intervalo_1 += 1
#     elif num < 50:
#         intervalo_2 += 1
#     elif num < 75:
#         intervalo_3 += 1
#     elif num < 100:
#         intervalo_4 += 1
#     else:
#         print("Número deve ser até 100")
#         continue
#     proxima = input("Quer continuar? (s/n)\n->")
#     while not (proxima == "s" or proxima == "n"):
#         proxima = input("Quer continuar? (s/n)\n->")
#     if proxima == "n" :
#         break


#Ex 15
# candidato_1 = 0
# candidato_2 = 0
# candidato_3 = 0
# candidato_4 = 0
# nulo = 0
# branco = 0
# votos_totais = 0
# print("1 ------ Roberto\n2 ------ Dagmar\n3 ------ Claudio\n4 ------ Paulo\n5 ------ Nulo\n6 ------ Branco")
# while True:
#     voto = input("Em quem você gostaria de votar?\n->")
#     if not (voto == '1' or voto == '2' or voto == '3' or voto == '4' or voto == '5' or voto == '6'):
#         print("Candidato não identificado!!!")
#         continue
#     if voto == "1":
#         candidato_1 += 1
#     elif voto == "2":
#         candidato_2 += 1
#     elif voto == "3":
#         candidato_3 += 1
#     elif voto == "4":
#         candidato_4 += 1
#     elif voto == "5":
#         nulo += 1
#     else:
#         branco += 1
#     votos_totais += 1
#     proxima = input("Quer continuar? (s/n)\n->")
#     while not (proxima == "s" or proxima == "n"):
#         proxima = input("Quer continuar? (s/n)\n->")
#     if proxima == "n":
#         break

# print(f"Roberto teve {candidato_1} votos.")
# print(f"Dagmar teve {candidato_2} votos.")
# print(f"Claudio teve {candidato_3} votos.")
# print(f"Paulo teve {candidato_4} votos.")
# print(f"A votação teve {nulo} votos nulos")
# print(f"A votação teve {branco} votos brancos")
# print(f"A votação teve {nulo*100/votos_totais:.2f}% de votos nulos")
# print(f"A votação teve {branco*100/votos_totais:.2f}% de votos brancos")