print("Seja bem vindo")
endereco = input("Digite seu enderço. \n->")
ano = int(input("Informe seu ano de nascimento\n->"))
if ano > 2007 :
    print("Não é permitida a venda de bebidas alcoolicas para menores de idade!!!")
else :
    print("Em nossa vinheria estão disponíveis 3 tipos de vinhos!")
    print("DaCasa R$50 \nMedieval R$60 \nCerteiro R$70")
    vinho = input("Qual vinho gostaria de comprar?\n->")
    quantidade = int(input("De quantas garrafas gostaria?\n->"))
    preco = int
    frete = 25
    if vinho == "DaCasa":
        preco = 50
    elif vinho == "Medieval":
        preco = 60
    elif vinho == "Certeiro":
        preco = 70
    total = preco * quantidade
    if preco * quantidade < 100:
            print(f"O valor total de sua compra foi de R${total} + frete, dando um total de R${total + frete}")
    else :
            print(f"O valor total de sua compra foi de R${total} e você ganhou frete GRÁTIS!!!!")
    print("Muito obrigado pela preferência e volte sempre!!!!")
