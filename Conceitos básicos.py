'''frase = "Hello World"
print(frase)

palavra_1 = "Olá "
palavra_2 = "Mundo"
print(palavra_1 + palavra_2)
frase = palavra_1 + palavra_2
print(frase)

frase = "Eu"
print(frase)
frase = frase + " " + "sou"
print(frase)
frase = frase + " " + "o"
print(frase)
frase = frase + " " + "Danilo"
print(frase)

frase = input("Diga a primeira palavra: ")
print(frase)
frase = frase + " " + input("Diga a segunda palavra: ")
print(frase)
frase = frase + " " + input("Diga a terceira palavra: ")
print(frase)
frase = frase + " " + input("Diga a quarta palavra: ")
print(frase)
frase = frase + " " + input("Diga a quinta palavra: ")
print(frase)

a = 2
b = 3
print(type(a))
soma = a + b
print(soma)
subtração = a - b
print(subtração)
multipicação = a * b
print(multipicação)
divisão = a / b
print(divisão)
potencia = a ** b
print(potencia)

print(f"A soma entre {a} e {b} é {soma}")

nome = input("Diga seu nome: ")
print(f"Olá , {nome}! Bem Vindo à calculadora!")

valor1 = int(input("Diga um valor: "))
valor2 = int(input("Diga outro valor: "))
print(valor1 + valor2)

a = 2
b = 3
print(a>b)
print(a!=b) (!= significa diferente) (== significa comparação)
a = 2
b = 4
print(f"O resultado de {a} > {b} é {a>b}")
print(f"O resultado de {a} < {b} é {a<b}")
print(f"O resultado de {a} >= {b} é {a>=b}")
print(f"O resultado de {a} <= {b} é {a<=b}")
print(f"O resultado de {a} == {b} é {a==b}")
print(f"O resultado de {a} != {b} é {a!=b}")

print(True and False)
print(False and False) (com and ambos precisam ser verdadeiros)
print(True and True)
print(2>3 and 3>2)
print(2<3 and 3>2)

print("Teste com and: ")
a = 2
b = 3
print(f"{a} > {b} and {a} < {b}, ou seja, {2 > 3} and {3 < 2} dá {2 > 3 and 3 > 2}")
print(f"{a} < {b} and {a} < {b}, ou seja, {2 < 3} and {3 < 2} dá {2 < 3 and 3 < 2}")
print(f"{a} > {b} and {a} < {b}, ou seja, {2 > 3} and {3 > 2} dá {2 > 3 and 3 < 2}")
print(f"{a} < {b} and {a} < {b}, ou seja, {2 < 3} and {3 > 2} dá {2 < 3 and 3 > 2}")

print("Teste com or: ")
a = 2
b = 3
print(f"{a} > {b} or {a} > {b}, ou seja, {2 > 3} or {3 < 2} dá {2 > 3 or 3 < 2}")
print(f"{a} > {b} or {a} > {b}, ou seja, {2 < 3} or {3 < 2} dá {2 < 3 or 3 > 2}")   (com or apenas um dos elementos precisa ser verdadeiro)
print(f"{a} > {b} or {a} > {b}, ou seja, {2 > 3} or {3 > 2} dá {2 > 3 or 3 > 2}")
print(f"{a} > {b} or {a} > {b}, ou seja, {2 < 3} or {3 > 2} dá {2 < 3 or 3 > 2}")

idade = int(input("Diga sua idade: "))
if idade >= 18:
    print("aôba🍻")
else:      ou     if idade <= 18:
    print("QUE FEIO😡")

print("Teste com or")
idoso = input("Você é idoso ?\n")
deficiente = input("Você é deficiente ?\n")      (\n faz com que a resposta vá para próxima linha)
if idoso == "sim" or deficiente == "sim":
    print("Estaciona fio🚗")
else:
    print("NÃO PODE ESTACIONAR!!!Vou contar pra sua mãe😡😡")

print("Teste com and")
idoso = input("Você é idoso ?\n")
carteirinha = input("Você tem a carteirinha ?\n")
if idoso == "sim" and carteirinha == "sim":
    print("Pode estacionar👍👍👍!!!")
else:
    print("Não será autorizado que você estacione aqui🤚🤚🤚!!!")'''

