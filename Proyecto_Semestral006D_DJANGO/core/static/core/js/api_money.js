// llenado precios
function llenadoPrecios(){
    var precio_array = JSON.parse(localStorage.getItem("reg_precios"));
    var price = 0;
    $('.precio').each(function(index, elemento) {
        price = precio_array[index+1].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
        elemento.innerHTML= '$ ' + price + ' CLP';
})
}



// escribir Funciones afuera del Ready
function getMoneda() {
    var codigo = $("#select_money").val();
    var price = 0;
    var precio_array = JSON.parse(localStorage.getItem("reg_precios"));
    if (codigo == 'CLP'){
        $('.precio').each(function(index, elemento) {
            console.log();
            price = precio_array[index+1].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
            elemento.innerHTML= '$ ' + price + ' CLP';
        })
        return false;
    }
    // (funcion que vaya recorriendo JSON)
    var url_api = 'https://api.gael.cloud/general/public/monedas/' + codigo
    var simbols = {'GBP':'£','EUR':'€','USD':'$','CAD':'$','AUD':'$','CLP':'$','JPY':'¥'};

    // funcion get JSON
    $.getJSON(
        // parametro_1: URL api
        url_api,
        // parametro_2: funcion que procesara la info que trae el JSON (puede ser funcion anonima)
        function (data) {
            $('.precio').each(function(index, elemento) {
                price = Math.round(precio_array[index+1] / parseFloat(data.Valor));
                price = price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
                elemento.innerHTML= simbols[codigo] + ' ' + price + ' ' + codigo;
        });
    })
}




// var price = 0;
// var precio_array = JSON.parse(localStorage.getItem("reg_precios"));
// $('.precio').each(function(index, elemento) {
//     price = Math.round(precio_array[index+1] * elemento.Valor);
//     price = price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
//     elemento.innerHTML= simbols[codigo] + ' ' + price + ' ' + codigo;