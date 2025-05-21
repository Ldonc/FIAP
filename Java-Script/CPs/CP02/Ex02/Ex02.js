function sequencia(){
    const n1 = document.getElementById('n1').value;
    const n2 = document.getElementById('n2').value;
    const n3 = document.getElementById('n3').value;
    const mensagem = document.getElementById('mensagem');

    if (n2 - n1 == n3 - n2){
        mensagem.textContent = "Esta sequência é uma Progressão Arimética";
    } else if (n2/n1 == n3/n2){
        mensagem.textContent = "Esta sequência é uma Progressão Geométrica";
    } else {
        mensagem.textContent = "Padrão Personalizado!"
    }
}