var clic = 1;

// const buttonForm = document.getElementById("calculando");
// buttonForm.addEventListener("click",(event) => {
//   event.preventDefault();
// })

//SE CREA LA RESPUESTA A LOS BOTONES DE LA CREACIÓN Y ELIMINACIÓN DE CARGAS
$(document).ready(function() {

  $("#add").click(function(){
    var contador = $("div[class='Cargas']").length + 1 ;

  $(this).before(
    '<div class="Cargas"><label for="Carga '+ contador +'"><b>Carga '+ contador +': </b></label><input type="text" id="Carga '+ contador +
    '" class="meterdatos_cargas_nombre" placeholder="Nombre '+ contador +'"  />&nbsp;&nbsp;<input type="number" id="Coordenada_X_Carga '+ 
    contador +'" class="meterdatos_cargas" placeholder="X'+ contador +'" /><label for="Coordenada_X_Carga '+ contador +
    '"><b>cm</b></label>&nbsp;&nbsp;<input type="number" id="Coordenada_Y_Carga '+ contador +'" class="meterdatos_cargas" placeholder="Y'+ 
    contador +'"  /><label for="Coordenada_Y_Carga '+ contador +'"><b>cm</b></label>&nbsp;&nbsp;<input type="number" id="Coordenada_Z_Carga '
    + contador +'" class="meterdatos_cargas" placeholder="Z'+ contador +'"  /><label for="Coordenada_Z_Carga '+ contador +
    '"><b>cm</b></label>&nbsp;&nbsp;<input type="number" id="Longitud_del_lado_h_Carga '+ contador +
    '" class="meterdatos_cargas" placeholder="A'+ contador +'"  /><label for="Longitud_del_lado_h_Carga '+ contador +
    '"><b>cm</b></label>&nbsp;&nbsp;<input type="number" id="Longitud_del_lado_v_Carga '+ contador +
    '" class="meterdatos_cargas" placeholder="B'+ contador +'"  /><label for="Longitud_del_lado_v_Carga '+ contador +
    '"><b>cm</b></label>&nbsp;&nbsp;<input type="number" id="Altura_Carga '+ contador +'" class="meterdatos_cargas" placeholder="H'+ 
    contador +'"  /><label for="Altura_Carga '+ contador +'"><b>cm</b></label>&nbsp;&nbsp;<input type="number" id="Masa_Carga '+ contador +
    '" class="meterdatos_cargas" placeholder="Masa '+ contador +'"  /><label for="Masa_Carga '+ contador +
    '"><b>kg</b></label> <br> <br> </div> ');
  
  });

  $(document).on('click', '#delete', function(){

    $(".Cargas").last().remove();

  });

  $('.default-open').click();

});

//ABRIR UNA SECCIÓN EN LA PÁGINA WEB
function opensection(evt, SectionName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(SectionName).style.display = "block";
  evt.currentTarget.className += " active";
}

//ABRIR UN ACORDEÓN DE LA PÁGINA WEB
function openacordeon(){
  var acc = document.getElementsByClassName("accordion");
  var i;

  for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var panel = this.nextElementSibling;
      if (panel.style.maxHeight) {
        panel.style.maxHeight = null;
      } else {
        panel.style.maxHeight = panel.scrollHeight + "px";
      } 
    });
  }
}

//ABRIR EL ACORDEÓN PARA DEFINIR LAS CARGAS DE PAGO
function openacordeon_scroll(){
  var acc = document.getElementsByClassName("accordion");
  var i;

  for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var panel = this.nextElementSibling;
      if (panel.style.maxHeight) {
        panel.style.maxHeight = null;
      } else {
        panel.style.maxHeight = 550 + "px";
      } 
    });
  }
}

//LECTURA, COMPROBACIÓN Y ENVÍO DE DATOS AL SERVIDOR DE LOS VALORES INTRODUCIDOS PARA HAYAR EL ALCANCE Y LA AUTONOMÍA
function CalcularAyA(){

  let mijson = {};
  mijson = []

  var n_motores = document.getElementById("Numero_motores").value;
  var I_max_1e = document.getElementById("Corriente_max_1motor").value;
  var I_max_equip = document.getElementById("Corriente_max_equipos").value;
  var velocidad = document.getElementById("Velocidad_vuelo").value;
  var V_nomin_bat = document.getElementById("Tension_nominal_bateria").value;
  var capacidad_bat = document.getElementById("Capacidad_bateria").value;
  var tasa_C = document.getElementById("Tasa_C_bateria").value;
  var regla_descarga = document.getElementById("Regla_descarga_bateria").value;
  var carga_vuelo = document.getElementById("Carga_vuelo").value;

  if (n_motores === null || n_motores ==='' || I_max_1e === null || I_max_1e ==='' || I_max_equip === null || I_max_equip ==='' || 
  velocidad === null || velocidad ==='' || V_nomin_bat === null || V_nomin_bat ==='' || capacidad_bat === null || capacidad_bat ==='' 
  || tasa_C === null || tasa_C ==='' || regla_descarga === null || regla_descarga ==='' || carga_vuelo === null || carga_vuelo ==='') {

    // alert("ERROR. Debe completar todos los campos. Además, evite escribir operaciones en los recuadros.");
    swal("ERROR", "Debe completar todos los campos. Además, evite escribir operaciones en los recuadros.", "error");
    return;

  } else if (n_motores < 0 || I_max_1e < 0 || I_max_equip < 0 || velocidad < 0 || V_nomin_bat < 0 || capacidad_bat < 0 || tasa_C < 0 || 
    regla_descarga < 0 || carga_vuelo < 0){

    swal("ERROR", "Los números negativos no son admitidos como una entrada correcta. También, procure poner un valor superior a cero 0.", "error");
    return;

  } else {

    let  DatosAyA = {
      Numero_motores: n_motores,
      Corriente_max_1motor: I_max_1e,
      Corriente_max_equipos: I_max_equip,
      Velocidad_vuelo: velocidad,
      Tension_nominal_bateria: V_nomin_bat,
      Capacidad_bateria: capacidad_bat,
      Tasa_C_bateria: tasa_C,
      Regla_descarga_bateria: regla_descarga, 
      Carga_vuelo: carga_vuelo
    }
  
    mijson.push(DatosAyA);
  
    // var dictstring = JSON.stringify(mijson);
    // var type = "JSON";
    // var filename = "Datos Autonomia y Alcance.json";
    // var file = new Blob([dictstring], {type: type});
    // var a = document.createElement("a"),
    // url = URL.createObjectURL(file);
    // a.href = url;
    // a.download = filename;
    // document.body.appendChild(a);
    // a.click();
  
    let string_AyA = JSON.stringify(mijson);
    Enviar_AyA(string_AyA);
    
  }

}

//FUNCIÓN QUE ENVÍA EL JSON DE LA AUTONOMÍA Y EL ALCANCE AL SERVIDOR FLASK
async function Enviar_AyA(ourjson){

  const response_AyA = await fetch(`http://127.0.0.1:5000/datos_AyA/${ourjson}`);
  const data_AyA = await response_AyA.json();

  let autonomia_def = parseFloat(data_AyA[0]);
  let alcance_def = parseFloat(data_AyA[1]);

  let autonomia_definitiva = Number(autonomia_def.toFixed(3));
  let alcance_definitivo = Number(alcance_def.toFixed(3));

  document.getElementById("horas").innerHTML = autonomia_definitiva + " h";
  document.getElementById("kilometros").innerHTML = alcance_definitivo + " km";

  swal("PERFECTO", "Los datos se han enviado y cargado correctamente. Ya puede ver sus resultados.", "success");

}

//CREA EN UNA VARIABLE LA LISTA PARA AÑADIR AL JSON DE CADA UNA DE LAS CARGAS
function getCargaPago(name,x,y,h_off,long_lado_h,long_lado_v,l_pad,masa){
  let cargaPago = {
    name:name,
    x:x,
    y:y,
    h_off:h_off,
    long_lado_h:long_lado_h,
    long_lado_v:long_lado_v,
    l_pad:l_pad,
    masa:masa
  }

  return cargaPago;
}

//LECTURA, COMPROBACIÓN Y ENVÍO DE DATOS AL SERVIDOR DE LOS VALORES INTRODUCIDOS PARA LAS CARGAS DE PAGO
function meteCargaPago(){

  let mijson = [];

  let num_cargas = document.getElementsByClassName("Cargas").length;
  if (num_cargas == 1) {
    document.getElementById("numero_cargas").innerHTML = "La <b>cantidad de cargas</b> introducidas es de " + num_cargas + 
    " carga. Los resultados obtenidos con esta distribución de carga son los siguientes.";
  } else {
    document.getElementById("numero_cargas").innerHTML = "La <b>cantidad de cargas</b> introducidas es de " + num_cargas + 
    " cargas. Los resultados obtenidos con esta distribución de carga son los siguientes.";
  }

  let numero_cargas = {numero_cargas:num_cargas};
  mijson.push(numero_cargas);

  if(num_cargas == 0){

    // var dictstring = JSON.stringify(mijson);
    // var type = "JSON";
    // var filename = "Datos de las cargas.json";
    // var file = new Blob([dictstring], {type: type});
    // var a = document.createElement("a"),
    // url = URL.createObjectURL(file);
    // a.href = url;
    // a.download = filename;
    // document.body.appendChild(a);
    // a.click();

    let str = JSON.stringify(mijson);
    Enviar_cargas(str);
    swal("Esto es solo un AVISO", "No se ha introducido ninguna carga de pago, por lo que en la siguiente sección el dron se visualizará vacío.");
  
  } else{

    for (let i = 1; i <= num_cargas; i++) {

      let text = i.toString();
  
      var nombre_carga = document.getElementById("Carga " + text).value;
      var coord_x = document.getElementById("Coordenada_X_Carga " + text).value;
      var coord_y = document.getElementById("Coordenada_Y_Carga " + text).value;
      var coord_z = document.getElementById("Coordenada_Z_Carga " + text).value;
      var lado_h = document.getElementById("Longitud_del_lado_h_Carga " + text).value;
      var lado_v = document.getElementById("Longitud_del_lado_v_Carga " + text).value;
      var altura =  document.getElementById("Altura_Carga " + text).value;
      var masa_carga = document.getElementById("Masa_Carga " + text).value;
  
      let cargaPago = getCargaPago(nombre_carga, coord_x, coord_y, coord_z, lado_h, lado_v, altura, masa_carga);
  
      mijson.push(cargaPago);
  
    }
  
    // var dictstring = JSON.stringify(mijson);
    // var type = "JSON";
    // var filename = "Datos de las cargas.json";
    // var file = new Blob([dictstring], {type: type});
    // var a = document.createElement("a"),
    // url = URL.createObjectURL(file);
    // a.href = url;
    // a.download = filename;
    // document.body.appendChild(a);
    // a.click();
  
    let str = JSON.stringify(mijson);
  
    for (let j = 1; j <= num_cargas; j++) {
  
      let j_text = j.toString();
  
      var coord_x_comprobar = mijson[j].x;
      var coord_y_comprobar = mijson[j].y;
      var coord_z_comprobar = mijson[j].h_off;
      var lado_h_comprobar = mijson[j].long_lado_h;
      var lado_v_comprobar = mijson[j].long_lado_v;
      var altura_comprobar = mijson[j].l_pad;
      var masa_carga_comprobar = mijson[j].masa;
  
      if (coord_x_comprobar === null || coord_x_comprobar ==='' || coord_y_comprobar === null || coord_y_comprobar ==='' || 
      coord_z_comprobar === null || coord_z_comprobar ==='' || lado_h_comprobar === null || lado_h_comprobar ==='' || 
      lado_v_comprobar === null || lado_v_comprobar ==='' || altura_comprobar === null || altura_comprobar ==='' || 
      masa_carga_comprobar === null || masa_carga_comprobar ==='') {

        swal("ERROR", "Le falta un campo por completar en los datos de la Carga " + j_text +" o ha introducido un valor no válido.", "error");
        return;

      } else if (lado_h_comprobar < 0.1 || lado_v_comprobar < 0.1 || altura_comprobar < 0.1){

        swal("ERROR", "La longitud de alguno de los lados de la Carga " + j_text + 
        " es demasiado pequeña o tiene un valor negativo. Se deben introducir valores superiores a 0.1cm.", "error");
        return;

      } else if (masa_carga_comprobar < 0.0001){

        swal("ERROR", "El valor de la masa de la Carga " + j_text + 
        " es demasiado pequeño o tiene un valor negativo. Se debe introducir un valor superior a 0.0001kg.", "error");
        return;

      } else if (j === num_cargas){

        Enviar_cargas(str);
        
      }
  
    }

  }

}

//FUNCIÓN QUE ENVÍA EL JSON DE LAS CARGAS DE PAGO AL SERVIDOR FLASK
async function Enviar_cargas(myjson){

  clic = clic + 1;

  const response = await fetch(`http://127.0.0.1:5000/datos_cargas/${myjson}`);
  const data = await response.json();

  let x_cdg_dron = Number(parseFloat(data[0]).toFixed(2));
  let y_cdg_dron = Number(parseFloat(data[1]).toFixed(2));
  let z_cdg_dron = Number(parseFloat(data[2]).toFixed(2));
  let x_cdg_total = Number(parseFloat(data[3]).toFixed(2));
  let y_cdg_total = Number(parseFloat(data[4]).toFixed(2));
  let z_cdg_total = Number(parseFloat(data[5]).toFixed(2));
  let string_sugerencias = data[6];


  document.getElementById("cdg_original").innerHTML = "("+ x_cdg_dron + ", " + y_cdg_dron + ", " + z_cdg_dron + ") cm";
  document.getElementById("cdg_cargado").innerHTML = "("+ x_cdg_total + ", " + y_cdg_total + ", " + z_cdg_total + ") cm";
  document.getElementById("sugerencias").innerHTML = "<b>&quot" + string_sugerencias + "&quot</b>";

  swal("PERFECTO", "Los datos se han enviado y cargado correctamente. Ya puede ver sus resultados.", "success");

}


//SI SE HA CLICADO EL BOTÓN "GUARDAR Y CARGAR" EN LA DEFINICIÓN DE LAS CARGAS DE PAGO, ENTONCES SE PUEDE VISUALIZAR
//EL DRON; SI NO SE HA PULSADO ESE BOTÓN, NO SE PUEDE VISUALIZAR

function divLogin(){ 

  if(clic==0){

    document.getElementById("viewer").style.height = "0%";
    document.getElementById("viewer").style.border = "0px solid";
    swal("ATENCIÓN", "Antes de poder visualizar su modelo, debe clicar el botón 'Guardar y cargar datos' en la pestaña" + 
    "'Parámetros de entrada', sección 'Defina las cargas de pago'.", "error");

  } else{

    document.getElementById("viewer").style.height = "85%";
    document.getElementById("viewer").style.border = "1.5px solid";
    swal("PERFECTO", "A continuación se abrirá una nueva pestaña para que usted pueda visualizar su dron.", "success");

  }   

}

