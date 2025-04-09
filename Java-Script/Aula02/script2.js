console.log("Script externo rodando para o DOM");

const tituloElemento = document.getElementById("tituloDinamico")//seleciona o elemento <h2> pelo seu id.
tituloElemento.textContent = "Texto alterado pelo JavaScript";//altera o texto
tituloElemento.style.color = "green";//alterando a cor do texto

const botaoElemento = document.getElementById("meuBotao");//seleciona o botão pelo seu id 
botaoElemento.addEventListener("click", function () {
    alert("Botão foi clicado!!!");
})

let idade = 17;
if(idade >= 18){
    console.log("Você é maior de idade")}


let temperatura = 25;
if (temperatura > 30){
    console.log("Esta muito quente!!!")
}


let nota = 7
if (nota >= 7){
    console.log("Você foi aprovado!!!")
}else{
    console.log("Você foi reprovado!!!")
}


let estaChovendo = false;
if (estaChovendo){
    console.log("Leve o guarda-chuva")
}else{
    console.log("Não precisa de guarda-chuva")
}

const inputIdade = document.getElementById('idadeInput');
const botaoVerificar = document.getElementById('verificarIdade');
const resultadoTexto = document.getElementById('resultadoVerificacao');

botaoVerificar.addEventListener('click' , function(){
    let idadeDigitada = parseInt(inputIdade.value);
    if(!isNaN(idadeDigitada)){ 
    if(idadeDigitada >= 18){
        resultadoTexto.textContent = 'Você é maior de idade';
        resultadoTexto.style.color = 'green';
    }else{
        resultadoTexto.textContent = 'Você é menor de idade';
        resultadoTexto.style.color = 'red';
    }
}else{
    resultadoTexto.textContent = 'Digite uma idade válida';
    resultadoTexto.style.color = 'orange';
}

});


