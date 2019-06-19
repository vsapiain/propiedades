function Miles(entrada){
    var num = entrada.replace(/\./g,"");
    if(!isNaN(num)){
        num = num.toString().split("").reverse().join("").replace(/(?=\d*\.?)(\d{3})/g,"$1.");
        num = num.split("").reverse().join("").replace(/^[\.]/,"");
        entrada = num;
    }else{
        entrada = input.value.replace(/[^\d\.]*/g,"");
    }
    return entrada;
}


