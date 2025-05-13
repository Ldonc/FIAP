print("Bem Vindo à Vinheira Agnello!!!")
ano = int(input("Diga seu ano de nascimento: \n->"))
endereco = input("Diga seu endereço: \n->")
idade = 2025 - ano 
if idade < 18:
    print("QUE FEIO!!!!VOU CONTAR PARA SUA MÃE!!!")
else:
    vinho1 = "Pérgola"
    vinho2 = "Sangue de Boi"
    vinho3 = "Cantinho do Vale"
    preco1 = 50
    preco2 = 30
    preco3 = 10
    escolha = input(f"Esses são nossos vinhos:\n{vinho1} - {preco1}"f"\n{vinho2} - {preco2}\n{vinho3} - {preco3}"f"Qual você quer?\n->")
    qtd = int(input(f"Quantas garrafas de {escolha} você quer?\n->"))
    if escolha == vinho1:
        preco = preco1
    elif escolha == vinho2:
        preco = preco2
    else:
        preco = preco3 
    total = qtd*preco
    frete = 10
    if total > 100:
        frete = 0
        print("Frete GRÁTIS!!!")
        total = total + frete
        print(f"Obrigado por comprar conosco, você gastou R${total} e será entregue em"f"{endereco}")