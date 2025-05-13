const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question(`Para qual temperatura você quer converter(Celsius/Farenheit)? -> `, (temperatura) => {
    readline.question(`Digite a temperatura -> `, (graus) => {
        const escala = String(temperatura);
        const intGraus = parseFloat(graus);
        if (escala == "Celsius"){
            const conversao = (graus-32)*(5/9);
            console.log(`${conversao}  graus Celsius`);
        }
        else if(escala == "Farenheit"){
            const conversao = graus*((9/5)+32);
            console.log(`${conversao}  graus Farenheit`);
        }
        else{
            console.log(`Valor inválido!`)
        }
        readline.close();
    })

});