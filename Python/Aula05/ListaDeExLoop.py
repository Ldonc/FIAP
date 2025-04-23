#Ex 1
# nota = int(input("Digite sua nota:\n->"))
# while not (nota >= 0 and nota <= 10):
#     nota = int(input("Digite sua nota:\n->")


#Ex 2
# nome = input("Digite seu nome: \n->")
# while len(nome) < 3:
#     nome = input("Digite seu nome: \n->")
# idade = int(input("Digite sua idade:\n->"))
# while not (idade > 0 and idade <= 150):
#     idade = int(input("Digite sua idade:\n->"))
# salario = float(input("Digite seu salario:\n->"))
# while salario < 0 :
#     salario = float(input("Digite seu salario:\n->"))
# sexo = input("Digite seu sexo:\n->")
# while not (sexo == "f" or sexo == "m"):
#     sexo = input("Digite seu sexo:\n->")
# estado_civil = input("Digite seu estado civil:\n->")
# while not (estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d"):
#     estado_civil = input("Digite seu estado civil:\n->")


#Ex 3
# populacao_A = 80000
# populacao_B = 200000
# taxa_A = 0.03
# taxa_B = 0.015
# anos = 0
# while populacao_A <= populacao_B:
#     populacao_A = populacao_A + (populacao_A * taxa_A)
#     pupulacao_b = populacao_B + (populacao_B * taxa_B)
#     anos = anos + 1
# print(f"Para a população_A alcançar a população_B serão necessários {anos} anos.")


#Ex 4
# num_1 = int(input("Informe um número:\n->"))
# num_2 = int(input("Informe um número:\n->"))
# num_3 = int(input("Informe um número:\n->"))
# num_4 = int(input("Informe um número:\n->"))
# num_5 = int(input("Informe um número:\n->"))
# print(f"A soma dos números é {num_1 + num_2 + num_3 + num_4 + num_5} e sua média é {(num_1 + num_2 + num_3 + num_4 + num_5) / 2} .")


#Ex 5
# num_1 = int(input("Digite um número inteiro:\n->"))
# num_2 = int(input("Digite um número inteiro:\n->"))
#
# if num_1 < num_2:
#     inicio = num_1 + 1
#     fim = num_2
# else:
#     inicio = num_2 + 1
#     fim = num_1
#
# print("Números no intervalo entre", inicio - 1, "e", fim, ":")
# while inicio < fim:
#     print(inicio)
#     inicio += 1


#Ex 6
# nome = input("Digite seu nome:\n-> ")
# senha = input("Digite sua senha:\n-> ")
# while nome == senha:
#     print("ERRO SENHA INVÁLIDA!")
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
