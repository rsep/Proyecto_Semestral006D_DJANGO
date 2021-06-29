// archivos para todos los estados cuando este iniciada la sesion

// funcion status
function inicioSesion(mail){
    var status = {'usuario':{'estado':1,'mail':mail} };
    localStorage.setItem("reg_status",JSON.stringify(status));
}

// diccionario carga
function generateCarga(){
    var carga = {'estado': 1};
    localStorage.setItem("reg_cargas",JSON.stringify(carga));
};

function disableCarga(){
    var carga = {'estado': 0};
    localStorage.setItem("reg_cargas",JSON.stringify(carga));
};

function veriCarga(){
    var serial_carga = localStorage.getItem("reg_cargas");
    var carga = JSON.parse(serial_carga);
    if (!carga){
        return false
    } else if (carga.estado == 1){
        alert("Carga exitosa");
        disableCarga();
    }
};

function redireccionar(){
    var serial_status = localStorage.getItem("reg_status");
    var status = JSON.parse(serial_status);
    if (!status){ 
        return false 
    }else if(status.usuario.estado == 1){
            window.location.replace("{% url 'perfil' %}")
    }
}

function nuevoRegistro(){
    var newReg = {'estado':1};
    localStorage.setItem("reg_newUser",JSON.stringify(newReg));
};

function veriRegistro(){
    var serial_reg = localStorage.getItem("reg_newUser");
    var reg = JSON.parse(serial_reg);
    if (!reg){
        return false;
    } else if (reg.estado == 1){
        alert("Registro exitoso");
        disableRegistro();
    }
};

function disableRegistro(){
    var newReg = {'estado':0};
    localStorage.setItem("reg_newUser",JSON.stringify(newReg));
}

function perfilUser(){
    var serial_status = localStorage.getItem("reg_status");
    var data = JSON.parse(serial_status);
    if (!data){
        return false;
    } else if(data.usuario.estado == 1){
        var profile = document.createElement("a");
        var container = document.getElementById("enlace");
        profile.id = "perfil";
        profile.href = "{% url 'perfil' %}";
        profile.className = "whiteBox";
        container.appendChild(profile);
        var name = getUserName(data.usuario.mail);
        document.getElementById("perfil").innerHTML = name.split(" ")[0];
    }
}

function getUserName(mail){
    var serial_data = localStorage.getItem("reg_cuentas");
    var data = JSON.parse(serial_data);
    return data[mail].nombre;
}

function bienvenida(){
    var serial_status = localStorage.getItem("reg_status");
    var data = JSON.parse(serial_status);
    if(data.usuario.estado == 1){
        var titulo = document.createElement("h1");
        var container = document.getElementById("bienvenida");
        titulo.id = "msjeBienvenida";
        container.appendChild(titulo);
        var name = getUserName(data.usuario.mail);
        document.getElementById("msjeBienvenida").innerHTML = name;
    }
}

function sesion(){
    var serial_status = localStorage.getItem("reg_status");
    var data = JSON.parse(serial_status);
    if(!data){
        var sesion = document.createElement("a");
        var hamburger = document.getElementById("mySidenav");
        sesion.id = "sesion";
        sesion.href = "{% url 'registro' %}";
        hamburger.appendChild(sesion);
        document.getElementById("sesion").innerHTML = "Registro & Acceso";
    } else if(data.usuario.estado == 1){
        var sesion = document.createElement("a");
        var hamburger = document.getElementById("mySidenav");
        sesion.id = "sesion";
        sesion.href = "{% url 'index' %}";
        sesion.setAttribute("onclick","closeSesion()")
        hamburger.appendChild(sesion);
        document.getElementById("sesion").innerHTML = "Cerrar Sesión";
    }else{
        var sesion = document.createElement("a");
        var hamburger = document.getElementById("mySidenav");
        sesion.id = "sesion";
        sesion.href = "{% url 'registro' %}";
        hamburger.appendChild(sesion);
        document.getElementById("sesion").innerHTML = "Registro & Acceso";
    }
}

function closeSesion(){
    var status = {'usuario':{'estado':0,'mail':""} };
    localStorage.setItem("reg_status",JSON.stringify(status));
}
