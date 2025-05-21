// Recupera o tempo salvo ao recarregar a página
// Ou inicia a contagem do zero
let tempoDecorrido = parseInt(sessionStorage.getItem('tempoDecorrido'));
if (isNaN(tempoDecorrido)) {
    tempoDecorrido = 0;
};

const contador1 = document.getElementById('contador');
const mensagem1 = document.getElementById('mensagem');

// Atualiza a tela
function atualizarTela(){
    contador1.textContent = tempoDecorrido;

    if (tempoDecorrido > 10){
        mensagem1.textContent = '👍😁Você está parado há um tempo nesta sessão. Interaja com o sistema😁👍';
    } else {
        mensagem1.textContent = '';
    }
}
// Atualização a cada segundo
const contando = setInterval(() => {
    tempoDecorrido++;
    sessionStorage.setItem('tempoDecorrido', tempoDecorrido);
    atualizarTela();
}, 1000);

// Atualizar a tela imediatamente a carregar a página
atualizarTela();