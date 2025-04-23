//Ex 03
const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question("Digite um número -> ", function (input) {
    const numero = parseFloat(input);
    if (numero > 0) {
        console.log("Seu número é positivo");
    } else if (numero == 0) {
        console.log("Seu número é 0");
    } else {
        console.log("Seu número é negativo");
    }

    readline.close();
});


