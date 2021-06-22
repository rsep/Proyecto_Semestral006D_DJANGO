// funciones de la web
function cleanInput(input){
    input.val("");
    input.next('.custom-file-label').html("Examinar equipo");
}

function carga_foto(){
    $(document).ready(function(){
        $('#inputGroupFile').on('change',function(){
            var address = $(this).val().split("\\");
            var fileName = address[address.length-1];
            $(this).next('.custom-file-label').html(fileName);
        });
    });  
}

function estado_carga(){
    $(document).ready(function(){
        veriCarga();
      });
};

function estado_registro(){
    $(document).ready(function(){
        veriRegistro();
    });
}