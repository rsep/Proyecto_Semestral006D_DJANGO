// Archivo para realizar validaciones a formularios

// ---------------------------------------------------------------------
// para Registro validar campos (nombre / email / contraseña)
// guardar en un arreglo los inputs
// ---------------------------------------------------------------------

// funciones auxiliares (mmostrar msje error)
function mensajeError(caja,mensaje){
    $("#" + caja).html(mensaje)
    $("#" + caja).fadeIn()
}

// ocultar mensaje si es true
function noError(caja){
    $("#" + caja).fadeOut()
}

// funcion nombre
function isName(nombre){
let regFullName = /^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$/;
return regFullName.test( nombre.trim() ) && nombre.length >= 3;
}

// funcion mail
function isMail(mail){
    let regMail = /^[^@]+@[^\.]+\..+$/;
	return regMail.test( mail.trim() );
}

// funcion contraseña (3 caracteres, 1 mayuscula, 1 numero)
function isPass(contraseña){

    let regPass = /^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{3,}$/;

    return regPass.test( contraseña.trim() );
}

// validacion campos

function validaNombre(){
    if (!isName($("#nombre").val())){
        mensajeError("eNombre",'Debes ingresar tu nombre')
        $("#nombre").focus()
        return false
    }else{
        noError("eNombre")
        return true
    }
}

function validaMail(){
    if ($("#mail").val().trim().length == 0){
        mensajeError("eMail",'Debes ingresar tu mail')
        $("#mail").focus()
        return false
    }else {
        if (!isMail($("#mail").val())){
            mensajeError("eMail",'Email no válido')
            $("#mail").focus()
            return false
        } else{
            noError("eMail")
            return true
        }   
    }
}

function validaPass(){
    if ($("#clave").val().trim().length == 0){
        mensajeError("ePass",'Debes ingresar una contraseña')
        $("#clave").focus()
        return false
    }else {
        if (!isPass($("#clave").val())){

            mensajeError("ePass",'Contraseña no válida mín: 3 caracteres, 1 Mayúscula, 1 Minúscula, 1 número')

            $("#clave").focus()
            return false
        } else{
            noError("ePass")
            return true
        }   
    }
}


// registrar credenciales
function registrarUsuario(cuentas){
    var data = $("#nombre").val().trim();
    var arrname = data.split(' ');
    var total_name = "";
    var name = "";
    for (var i in arrname){
        name = arrname[i].charAt(0).toUpperCase() + arrname[i].slice(1).toLowerCase();
        total_name = total_name + " " + name;
    }
    cuentas[$("#mail").val().trim()] = {'clave':$("#clave").val().trim(),'nombre': total_name.trim()};
    localStorage.setItem("reg_cuentas",JSON.stringify(cuentas));
}

function import_data(){
    var serial_data = localStorage.getItem("reg_cuentas");
    var data = JSON.parse(serial_data);
    if(!data){
        return {};
    } else{
        return data;
    }
}

function isRegister(cuentas,mail){
    var test = cuentas[mail];
    if (!test) {
        return false;
    }else{
        return true;
    }
}

// ---------------------------------------------------------------------
// para Login validar par email + contraseña
// ---------------------------------------------------------------------
function validaMail_log(){
    if ($("#log_mail").val().trim().length == 0){
        mensajeError("eMail_log",'Debes ingresar tu mail')
        $("#log_mail").focus()
        return false
    }else {
        if (!isMail($("#log_mail").val().trim())){
            mensajeError("eMail_log",'Email no válido')
            $("#log_mail").focus()
            return false
        } else{
            noError("eMail_log")
            return true
        }   
    }
}

function validaPass_log(){
    if ($("#log_clave").val().trim().length == 0){
        mensajeError("ePass_log",'Debes ingresar una contraseña')
        $("#log_clave").focus()
        return false
    }else {
        if (!isPass($("#log_clave").val().trim())){
            mensajeError("ePass_log",'Contraseña no válida mín: 3 caracteres, 1 Mayúscula, 1 Minúscula, 1 número')
            $("#log_clave").focus()
            return false
        } else{
            noError("ePass_log")
            return true
        }   
    }
}


// ---------------------------------------------------------------------
// para perfil validar campos carga archivos
// ---------------------------------------------------------------------
function validaTitulo(){
    var nombre = $("#titulo").val().trim();
    if (nombre.length == 0){
        mensajeError("eTitulo","Debes ingresar un título");
        $("#titulo").focus();
        return false;
    } else{
        noError("eTitulo");
        return true;
    }
}

function validaHistoria(limite_inf){
    var size = $("#historia").val().trim().length;
    if (size == 0){
        mensajeError("eHistoria",'Debe escribir una historia')
        $("#historia").focus()
    }else {
        if (size < limite_inf){
            mensajeError("eHistoria",'Historia debe tener al menos ' + limite_inf + ' caracteres')
            $("#historia").focus()
            return true
        }else{
            noError("eHistoria")
            return true
        }
    }
}

function validaDescripcion(limite_inf){
    var size = $("#descripcion").val().trim().length;
    if (size == 0){
        mensajeError("eDescripcion",'Debe escribir una descripción')
        $("#descripcion").focus()
    }else {
        if (size < limite_inf){
            mensajeError("eDescripcion",'Descripción debe tener al menos ' + limite_inf + ' caracteres')
            $("#descripcion").focus()
            return true
        }else{
            noError("eDescripcion")
            return true
        }
    }
}

function validaTecnica(){
    var nombre = $("#tecnica").val().trim();
    if (nombre.length == 0){
        mensajeError("eTecnica","Debes ingresar una técnica");
        $("#tecnica").focus();
        return false;
    } else{ 
        noError("eTecnica");
        return true;
    }
}

function validaPrecio(){
    if ($("#precio").val().trim().length == 0){
        mensajeError("ePrecio",'Debes ingresar el precio');
        $("#precio").focus();
        return false;
    } else{
        noError("ePrecio");
        return true;
    }
}

function validaYear(){
    if ($("#year").val().trim().length == 0){
        mensajeError("eYear",'Debes ingresar el año');
        $("#year").focus();
        return false;
    } else{
        noError("eYear");
        return true;
    }
}

// ---------------------------------------------------------------------
// para contacto (nombre)
// ---------------------------------------------------------------------
function validaNombre_cto(){
    if (!isName($("#nom_contacto").val())){
        mensajeError("eNombre_cto",'Debes ingresar tu nombre')
        $("#nom_contacto").focus()
        return false
    }else{
        noError("eNombre_cto")
        return true
    }
}

function validaMail_cto(){
    if ($("#mail_contacto").val().trim().length == 0){
        mensajeError("eMail_cto",'Debes ingresar tu mail')
        $("#mail_contacto").focus()
        return false
    }else {
        if (!isMail($("#mail_contacto").val())){
            mensajeError("eMail_cto",'Email no válido')
            $("#mail_contacto").focus()
            return false
        } else{
            noError("eMail_cto")
            return true
        }   
    }
}

function validaComentario(limite_inf){
    var size = $("#comentario").val().trim().length;
    if (size == 0){
        mensajeError("eComentario",'Debe escribir un comentario')
        $("#comentario").focus()
    }else {
        if (size < limite_inf){
            mensajeError("eComentario",'Comentario debe tener al menos ' + limite_inf + ' caracteres')
            $("#comentario").focus()
            return true
        }else{
            noError("eComentario")
            return true
        }
    }
}

// ---------------------------------------------------------------------
// jQUERY (llamado a las funciones)
// ---------------------------------------------------------------------
$(document).ready(function(){
    // mensajes error ocultos
    $(".invalid-feedback").hide()


    // REGISTRO:

    // validación nombre
    $("#nombre").blur(function(){
        exito = validaNombre()
    });

    // validación mail
    $("#mail").blur(function(){
        exito = validaMail()
    });

    // validación password
    $("#clave").blur(function(){
        exito = validaPass()
    });

    // LOGIN:

    // validación mail
    $("#log_mail").blur(function(){
        exito = validaMail_log()
    });

    // validación password
    $("#log_clave").blur(function(){
        exito = validaPass_log()
    });


    // PERFIL:

    // validacion titulo
    $("#titulo").blur(function(){
        exito = validaTitulo();
    });

    $("#tecnica").blur(function(){
        exito = validaTecnica();
    });

    $("#historia").blur(function(){
        exito = validaHistoria(100);
    });

    $("#descripcion").blur(function(){
        exito = validaDescripcion(100);
    });

    $("#precio").blur(function(){
        exito = validaPrecio();
    });

    $("#year").blur(function(){
        exito = validaYear();
    });


    // CONTACTO
    $("#nom_contacto").blur(function(){
        exito = validaNombre_cto();
    });

    $("#mail_contacto").blur(function(){
        exito = validaMail_cto();
    });
    
    $("#comentario").blur(function(){
        exito = validaComentario(10);
    });
    
    $("#cleaner").click(function(){
        window.location.reload()
    });


    // ENVIOS FORMULARIOS:

    // Registro
    $("#form_registro").submit(function(){
        exito = false
        // validación pre envío del formulario
        if(
            !validaNombre()||
            !validaMail()||
            !validaPass
        ){
            event.preventDefault()
        }else {
            var cuentas = import_data();
            if (!isRegister(cuentas,$("#mail").val().trim())) {
                registrarUsuario(cuentas)
                nuevoRegistro();
            } else{
                event.preventDefault()
                alert('Usuario ya existe')
            }
        }
    });
  
    // Login
    $("#form_login").submit(function(){
        exito = false;
        // validación pre envío del formulario
        if(
            !validaMail_log()||
            !validaPass_log()
        ){
            event.preventDefault();
        }else {
            var cuentas = import_data();
            if (isRegister(cuentas,$("#log_mail").val().trim())) {
                if (cuentas[$("#log_mail").val().trim()].clave == $("#log_clave").val().trim()){           
                    inicioSesion($("#log_mail").val().trim());
                } else{
                    event.preventDefault();
                    alert('Usuario no registrado o contraseña incorrecta');
                }
            }else{
                event.preventDefault();
                alert('Usuario no registrado o contraseña incorrecta');
            }
        }
    });

    // Carga archivos perfil
    $("#form_carga").submit(function(){
        exito = false
        // validación pre envío del formulario
        if(
            !validaTitulo()||
            !validaTecnica()||
            !validaHistoria(100)||
            !validaDescripcion(100)||
            !validaPrecio()||
            !validaYear()

        ){
            event.preventDefault()
        } else{
            generateCarga();
        }
    });

});



