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

 function numberFormat(numero){
    // Variable que contendra el resultado final
    var resultado = "";

    // Si el numero empieza por el valor "-" (numero negativo)
    if(numero[0]=="-")
    {
        // Cogemos el numero eliminando los posibles puntos que tenga, y sin
        // el signo negativo
        nuevoNumero=numero.replace(/\./g,'').substring(1);
    }else{
        // Cogemos el numero eliminando los posibles puntos que tenga
        nuevoNumero=numero.replace(/\./g,'');
    }

    // Si tiene decimales, se los quitamos al numero
    if(numero.indexOf(",")>=0)
        nuevoNumero=nuevoNumero.substring(0,nuevoNumero.indexOf(","));

    // Ponemos un punto cada 3 caracteres
    for (var j, i = nuevoNumero.length - 1, j = 0; i >= 0; i--, j++)
        resultado = nuevoNumero.charAt(i) + ((j > 0) && (j % 3 == 0)? ".": "") + resultado;

    // Si tiene decimales, se lo añadimos al numero una vez forateado con
    // los separadores de miles
    if(numero.indexOf(",")>=0)
        resultado+=numero.substring(numero.indexOf(","));

    if(numero[0]=="-")
    {
        // Devolvemos el valor añadiendo al inicio el signo negativo
        return "-"+resultado;
    }else{
        return resultado;
    }
}
