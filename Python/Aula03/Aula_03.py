cachorro = input("sentar\n->")
if cachorro == "sim" :
    print("bom garoto🐶🐶")
else :
    print("menino mal😡😡")

vogal = input("Coloque uma letra\n->")
if vogal == "a" or vogal == "e" or vogal == "i" or vogal == "o" or vogal == "u" :
    print(f"Sim {vogal} é uma vogal😁😁😁")
else :
    print(f"{vogal} não é uma vogal😥😥😥")

time = input("Diga para que time você torce:\n-> ")
if time == "São Paulo" :
    print("Maior do Brasil, trimundial, triliberta, o mais foda né")
elif time == "Palmeiras" :
    print("Sem mundial, parbéns pelo bi da serie B, tia Leila faz o pix")
elif time == "Corinthians" :
    print("Por favor não me roube😭😭")
else :
    print("Parabéns pela serie B, Pelé futebol clube")

salario = int(input("Diga seu salário:\n-> "))
if salario < 1903.98 :
    print("Parabéns você não pagará imposto🤑🤑")
elif salario >= 1903.99 or salario <= 2826.65 :
    print(f"Você receberá R${salario - (salario * 0.075) } de salário com imposto descontado")
elif salario >= 2826.66 or salario <= 3751.05 :
    print(f"Você receberá R${salario - (salario * 0.15) } de salário com imposto descontado")
elif salario >= 3751.06 or salario <= 4664.68 :
    print(f"Você receberá R${salario - (salario * 0.225) } de salário com imposto descontado")
else :
    print(f"Você receberá R${salario - (salario * 0.275) } de salário com imposto descontado")


entrar = input("Você quer fazer contas???\n->")
if entrar == "sim" :
    n1 = int(input("Diga um número\n->"))
    n2 = int(input("Diga outro número\n->"))
    operacao = (input("Qual operação você deseja realizar?\n->"))
    if operacao == "adição" :
         print(n1 + n2)
    elif operacao == "subtração" :
            print(n1 - n2)
    elif operacao == "multiplicação" :
        print(n1 * n2)
    else :
          print(n1 / n2)

else :
    print("Vai se lascar!!!!!")