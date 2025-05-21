// Dicionário de cores com códigos hexadecimais conhecidos
const coresPredefinidas = {
    red: "#FF0000",
    blue: "#0000FF",
    green: "#008000",
    yellow: "#FFFF00",
    orange: "#FFA500",
    purple: "#800080",
    black: "#000000",
    white: "#FFFFFF",
    gray: "#808080",
    pink: "#FFC0CB"
  };
  
  // Array que armazenará objetos { nome, codigo }
  let listaDeCores = [];
  
  const input = document.getElementById("entradaCor");
  const ul = document.getElementById("listaCores");
  
  // Mensagem de erro (criada dinamicamente)
  const mensagemErro = document.createElement("p");
  mensagemErro.style.color = "red";
  mensagemErro.style.marginTop = "0.5rem";
  input.insertAdjacentElement("afterend", mensagemErro);
  
  // Atualiza a lista no DOM
  function atualizarLista() {
    ul.innerHTML = ""; // Limpa lista anterior
    mensagemErro.textContent = ""; // limpa mensagem de erro
  
    listaDeCores.forEach(cor => {
      const li = document.createElement("li");
      li.textContent = cor.nome;
      li.style.backgroundColor = cor.codigo;
      li.style.color = cor.nome.toLowerCase() === "yellow" || cor.codigo === "#FFFF00" ? "#000" : "#fff";
      ul.appendChild(li);
    });
  }
  
  // Evento ao pressionar Enter no campo
  input.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
      const nomeCor = input.value.trim().toLowerCase();
  
      if (nomeCor) {
        if (coresPredefinidas.hasOwnProperty(nomeCor)) {
          const novaCor = {
            nome: nomeCor,
            codigo: coresPredefinidas[nomeCor]
          };
          listaDeCores.unshift(novaCor);
          atualizarLista();
        } else {
          mensagemErro.textContent = "Cor inexistente no sistema.";
        }
  
        input.value = ""; // limpa o campo
      }
    }
  });