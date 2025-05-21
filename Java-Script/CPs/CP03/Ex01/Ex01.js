// Base de frases
const baseDeDados = [
    { frase: "A Terra é plana", status: "fake", explicacao: "A Terra tem forma esférica, comprovada por evidências científicas." },
    { frase: "Vacinas causam autismo", status: "fake", explicacao: "Não há evidências científicas que comprovem essa relação." },
    { frase: "A água ferve a 100 graus Celsius ao nível do mar", status: "fato", explicacao: "Essa é uma propriedade física confirmada." },
    { frase: "5G transmite COVID-19", status: "fake", explicacao: "COVID-19 é causado por um vírus, não por ondas de rádio." },
    { frase: "Usar máscara ajuda a prevenir a COVID-19", status: "fato", explicacao: "Máscaras reduzem a transmissão de gotículas respiratórias." },
    { frase: "Beber água com limão cura câncer", status: "fake", explicacao: "Não há comprovação científica de cura do câncer com limão." },
    { frase: "O aquecimento global é causado por atividades humanas", status: "fato", explicacao: "O IPCC aponta o impacto humano no clima global." },
    { frase: "Bill Gates implantou chips com vacinas", status: "fake", explicacao: "Essa é uma teoria da conspiração sem fundamentos." },
    { frase: "Plantas fazem fotossíntese", status: "fato", explicacao: "Esse processo é essencial para a produção de energia nas plantas." },
    { frase: "Coca-Cola dissolve dentes durante a noite", status: "fake", explicacao: "Embora ácida, isso não acontece tão rapidamente." }
  ];
  
  // Função para verificar a frase
  function verificarFrase() {
    const input = document.getElementById("inputFrase").value.trim().toLowerCase();
    const resultadoDiv = document.getElementById("resultado");
    resultadoDiv.innerHTML = "";
  
    const fraseEncontrada = baseDeDados.find(item => item.frase.toLowerCase() === input);
  
    if (fraseEncontrada) {
      const isFato = fraseEncontrada.status === "fato";
      resultadoDiv.className = isFato ? "fato" : "fake";
      resultadoDiv.innerHTML = `
        ${isFato ? "👍🎉 Fato Verificado" : "😲😰 Fake News"}<br />
        <small>${fraseEncontrada.explicacao}</small>
      `;
    } else {
      resultadoDiv.className = "";
      resultadoDiv.innerHTML = "Frase não encontrada na base de dados.";
    }
  }