i = 0
pares = 0

num = int(input(f"Diga o {i+1}° número: "))
if num%2 == 0:
    pares = pares + 1
i = i + 1

num = int(input(f"Diga o {i+1}° número: "))
if num%2 == 0:
    pares = pares + 1
i = i + 1

num = int(input(f"Diga o {i+1}° número: "))
if num%2 == 0:
    pares = pares + 1
i = i + 1

num = int(input(f"Diga o {i+1}° número: "))
if num%2 == 0:
    pares = pares + 1
i = i + 1

num = int(input(f"Diga o {i+1}° número: "))
if num%2 == 0:
    pares = pares + 1
i = i + 1

print(f"Você digitou {pares} números pares e {i - pares } números impares")





i = 0
pares = 0

while i < 5:
    num = int(input(f"Diga o {i + 1}° número: "))
    if num%2 == 0:
     pares = pares + 1 # pares += 1
     print(i)
     i = i + 1 # i +=  1
print(f"Você digitou {pares} números pares e {i - pares} números impares")

senha = "1234"
codigo = input("Digite sua senha:\n->")
while codigo != senha:
    print("Acesso negado🤔")
    codigo = input("Digite sua senha:\n->")
print("Acesso liberado")




senha = "1234"
senha_fornecida = input("Digite sua senha:\n->")
tentativa = 1
while tentativa < 3 and senha_fornecida != "1234":
    print("Acesso negado🤔")
    senha_fornecida = input("Digite sua senha:\n->")
    tentativa = tentativa + 1
if senha_fornecida == "1234":
    print("Acesso liberado😁")
if tentativa == 3:
    print("Seu acesso foi bloqueado😘")





pokemon = "Não é o pikachu"
pergunta = input("Qual seu pokemon favorito??\n->")
tentativa = 1
while tentativa < 5 and pergunta != "Não é o pikachu":
    print("Fala a verdade MANO!!!")
    pergunta = input("Qual seu pokemon favorito??\n->")
    tentativa = tentativa + 1
if pergunta == "Não é o pikachu":
    print("Parabéns você realmete entende de pokemon!!!!👌")
else:
    print("Deixa pra lá 😒")




#and
genero = input("Diga masculino ou feminino:\n->")
while genero != 'mansculino' and genero != "feminino":
    genero = input("Diga masculino ou feminino:\n->")




#or
genero = input("Diga masculino ou feminino:\n->")
while not (genero == 'mansculino' or genero == "feminino"):
    genero = input("Diga masculino ou feminino:\n->")





numero = input("Digite um número\n->")
while not (numero.isnumeric()):
    numero = input("Digite um número\n->")
numero = int(numero)
