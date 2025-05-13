const compra = parseInt(document.getElementById("valor").value);
const resposta = document.getElementById("resposta");


function desconto(){
    const compra = document.getElementById("valor").value;
    const resposta = document.getElementById("resposta");
    if(compra > 50 && compra <= 100) {
        const desconto = 0.05;
        resposta.textContent = `Sua compra foi de R$${compra - (compra*desconto)}`;
    }
    else if(compra > 100 && compra <= 200){
        const desconto = 0.1;
        resposta.textContent = `Sua compra foi de R$${compra - (compra*desconto)}`;
    }
    else if(compra > 200){
        const desconto = 0.15;
        resposta.textContent = `Sua compra foi de R$${compra - (compra*desconto)}`;
    }
    else {
        resposta.textContent = `Sua compra foi de R$${compra}`;;
    }
}