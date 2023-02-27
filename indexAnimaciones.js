
//-------------------------------------------------------IMPORTACIÓN DE MÓDULOS-------------------------------------------------------------------

import * as THREE from './Archivosthreejs/three.module.js';
import {STLLoader} from './Archivosthreejs/STLLoader.js';
import {OrbitControls} from './Archivosthreejs/OrbitControls.js';
import {EffectComposer} from './Archivosthreejs/EffectComposer.js';  //Añadir efectos de animacion
import {RenderPass} from './Archivosthreejs/RenderPass.js';
import {OutlinePass} from './Archivosthreejs/OutlinePass.js';        //Remarcar cada elemento
import { GUI } from './Archivosthreejs/lil-gui.module.min.js';

//-------------------------------------------------------DECLARACIÓN DE VARIABLES------------------------------------------------------------------

let scene, camera, renderer, composer, outlinePass;

let selectedObjects = [];

let Fuselaje, Semiala_izquierda, Semiala_derecha, Timon_Semiala_derecha, Timon_Semiala_izquierda, Cola_estab_vertical, Timon_estab_vertical, 
    Estab_horizontal_derecho, Timon_estab_horizontal_derecho, Estab_horizontal_izquierdo, Timon_estab_horizontal_izquierdo;

let Pieza_negra_seccion_fuselaje_cola, Pieza_negra_fuselaje_semiala_izquierda, Pieza_negra_fuselaje_semiala_derecha, Tubo_soporte_BA, 
    Tubo_soporte_BS, Pieza_negra_semiala_derecha, Pieza_negra_semiala_izquierda, TuboBS_de_Semiala_izquierda, TuboBA_de_Semiala_izquierda, 
    TuboBS_de_Semiala_derecha, TuboBA_de_Semiala_derecha, Tubo_cola_fuselaje, Pieza_negra_seccion_cola_fuselaje, 
    Pieza_negra_fuselaje_estab_horizontal_derecho, Pieza_negra_fuselaje_estab_horizontal_izquierdo,Pieza_negra_estab_horizontal_derecho, 
    Pieza_negra_timon_estab_horizontal_derecho, Tubo_estab_horizontal_derecho, Tubo_estab_horizontal_izquierdo, 
    Pieza_negra_timon_estab_horizontal_izquierdo, Pieza_negra_estab_horizontal_izquierdo;

let Patin_izquierdo, Patin_derecho, Tapa1, Tapa2, Tapa3, Tapa4, Tapa_inferior, Pestana_de_union_derecha, Pestana_de_union_izquierda;

let Cargas_pago, cdg_DRON, cdg_TOTAL;

let nombres_blancas = [
    Fuselaje, Semiala_izquierda, Semiala_derecha, Timon_Semiala_derecha, Timon_Semiala_izquierda, Cola_estab_vertical, Timon_estab_vertical, 
    Estab_horizontal_derecho, Timon_estab_horizontal_derecho, Estab_horizontal_izquierdo, Timon_estab_horizontal_izquierdo
];

let nombres_negras = [
    Pieza_negra_seccion_fuselaje_cola, Pieza_negra_fuselaje_semiala_izquierda, Pieza_negra_fuselaje_semiala_derecha, Tubo_soporte_BA, 
    Tubo_soporte_BS, Pieza_negra_semiala_derecha, Pieza_negra_semiala_izquierda, TuboBS_de_Semiala_izquierda, TuboBA_de_Semiala_izquierda, 
    TuboBS_de_Semiala_derecha, TuboBA_de_Semiala_derecha, Tubo_cola_fuselaje, Pieza_negra_seccion_cola_fuselaje, 
    Pieza_negra_fuselaje_estab_horizontal_derecho, Pieza_negra_fuselaje_estab_horizontal_izquierdo,Pieza_negra_estab_horizontal_derecho, 
    Pieza_negra_timon_estab_horizontal_derecho, Tubo_estab_horizontal_derecho, Tubo_estab_horizontal_izquierdo, 
    Pieza_negra_timon_estab_horizontal_izquierdo, Pieza_negra_estab_horizontal_izquierdo
];

let nombres_otras = [
    Patin_izquierdo, Patin_derecho, Tapa1, Tapa2, Tapa3, Tapa4, Tapa_inferior, Pestana_de_union_derecha, Pestana_de_union_izquierda
];

let nombre_carga_pago = [Cargas_pago];

let nombre_cdg_dron = [cdg_DRON];

let nombre_cdg_total = [cdg_TOTAL];

//-------------------------------------------------ALMACENAMIENTO DE LAS URL DE LOS ARCHIVOS STL---------------------------------------------------------------

let url_blancas = [
    "./ArchivosSTL/Fuselaje_AllCATPart.stl", "./ArchivosSTL/Semiala izquierda_AllCATPart.stl", "./ArchivosSTL/Semiala derecha_AllCATPart.stl", 
    "./ArchivosSTL/Timon semiala derecha_AllCATPart.stl", "./ArchivosSTL/Timon semiala izquierda_AllCATPart.stl", 
    "./ArchivosSTL/Cola_estab.vertical_AllCATPart.stl", "./ArchivosSTL/Timon estab. vertical_AllCATPart.stl", 
    "./ArchivosSTL/Estabilizador horizontal derecho_AllCATPart.stl", "./ArchivosSTL/Timon estab. horizontal derecho_AllCATPart.stl", 
    "./ArchivosSTL/Estabilizador horizontal izquierdo_AllCATPart.stl", "./ArchivosSTL/Timon estab. horizontal izquierdo_AllCATPart.stl"
];

let url_negras = [
    "./ArchivosSTL/Pieza negra seccion fuselaje-cola_AllCATPart.stl", 
    "./ArchivosSTL/Pieza negra fuselaje-semiala izquierda_AllCATPart.stl", "./ArchivosSTL/Pieza negra fuselaje-semiala derecha_AllCATPart.stl", 
    "./ArchivosSTL/Tubo soporte BA_AllCATPart.stl", "./ArchivosSTL/Tubo soporte BS_AllCATPart.stl", 
    "./ArchivosSTL/Pieza negra semiala derecha_AllCATPart.stl", "./ArchivosSTL/Pieza negra semiala izquierda_AllCATPart.stl", 
    "./ArchivosSTL/Tubo BS del semiala izquierda_AllCATPart.stl", "./ArchivosSTL/Tubo BA del semiala izquierda_AllCATPart.stl",
    "./ArchivosSTL/Tubo BS del semiala derecha_AllCATPart.stl", "./ArchivosSTL/Tubo BA del semiala derecha_AllCATPart.stl", 
    "./ArchivosSTL/Tubo cola-fuselaje_AllCATPart.stl", "./ArchivosSTL/Pieza negra seccion cola-fuselaje_AllCATPart.stl",
    "./ArchivosSTL/Pieza negra fuselaje-estab. horizontal derecho_AllCATPart.stl", 
    "./ArchivosSTL/Pieza negra fuselaje-estab. horizontal izquierdo_AllCATPart.stl", 
    "./ArchivosSTL/Pieza negra estab. horizontal derecho_AllCATPart.stl", 
    "./ArchivosSTL/Pieza negra timon estab. horizontal derecho_AllCATPart.stl", 
    "./ArchivosSTL/Tubo estab. horizontal derecho_AllCATPart.stl", "./ArchivosSTL/Tubo estab. horizontal izquierdo_AllCATPart.stl", 
    "./ArchivosSTL/Pieza negra timon estab. horizontal izquierdo_AllCATPart.stl", 
    "./ArchivosSTL/Pieza negra estab. horizontal izquierdo_AllCATPart.stl"
];

let url_otras = [
    "./ArchivosSTL/Patin izquierdo_AllCATPart.stl", "./ArchivosSTL/Patin derecha_AllCATPart.stl", 
    "./ArchivosSTL/Tapa 1_AllCATPart.stl", "./ArchivosSTL/Tapa 2_AllCATPart.stl", "./ArchivosSTL/Tapa 3_AllCATPart.stl", 
    "./ArchivosSTL/Tapa 4_AllCATPart.stl", "./ArchivosSTL/Tapa Inferior_AllCATPart.stl", "./ArchivosSTL/Pestana union derecha_AllCATPart.stl", 
    "./ArchivosSTL/Pestana union izquierda_AllCATPart.stl"
];

let url_carga_pago = ["./ArchivosSTL/Parte_CargaPago.stl"];

let url_cdg_dron = ["./ArchivosSTL/Parte_CuboCDG_ORIGINAL.stl"];

let url_cdg_total = ["./ArchivosSTL/Parte_CuboCDG_CARGADO.stl"];

//--------------------------------------------DECLARACIÓN DE COLORES APLICADOS A LOS STL EN LA ESCENA---------------------------------------------------------------

let color_blancas = {color: "rgb(190, 190, 255)"};
let color_negras = {color: "rgb(0, 0, 0)"};
let color_otras = {color: "rgb(50, 50, 100)"};
let color_carga_pago = {color: "rgb(0, 50, 100)"};
let color_cdg_dron = {color: "rgb(255, 0, 0)"};
let color_cdg_total = {color: "rgb(0, 255, 0)"};
let colores_piezas = [color_blancas, color_negras, color_otras, color_carga_pago, color_cdg_dron, color_cdg_total];

//-----------------------------------------DECLARACIÓN DE VARIABLES DE CONTROL NECESARIAS PARA ESCENA---------------------------------------------------------------

let loader = new STLLoader();
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();

//-----------------------------------------------------------LLAMADA A LAS FUNCIONES---------------------------------------------------------------

init();
animate();

//--------------------------------------------------------------FUNCIÓN ANIMATE()---------------------------------------------------------------

function animate(){
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
    composer.render();
    renderer.clearDepth();
}

//----------------------------------------------------------------FUNCIÓN INIT()-----------------------------------------------------------------------

function init(){

    //--------------------------------------------------------INICIALIZACIÓN DE ESCENA----------------------------------------------------------------

    scene = new THREE.Scene();

    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 10000);
    camera.position.set(0,0,19);
    camera.lookAt(0,0,0);

    camera.layers.enable( 50 );    // enabled by default
    camera.layers.enable( 40 );
	scene.add( camera );

    var posiciones = [10, -10];
    for (let i = 0; i < 3; i++) {
        let light_50 = new THREE.DirectionalLight("rgb(110, 110, 110)");
        let light_50_2 = new THREE.DirectionalLight("rgb(110, 110, 110)");
        let position_i = posiciones[i];
        light_50.position.set(0,0,position_i);
        light_50_2.position.set(position_i, 0, 0);
        light_50.layers.enable( 50 );
        light_50_2.layers.enable( 50 );
	    camera.add( light_50, light_50_2 );
    }

    renderer = new THREE.WebGLRenderer({
        alpha: true,                        //hace background blanco/transparente
        antialias: false                    //mejora calidad de las lineas
    });

    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById("canvas").appendChild(renderer.domElement);

    //-----------------------------------------BUCLES DE CARGA DE PIEZAS (POR GRUPOS DE COLORES Y DE CAPAS)-------------------------------------------------

    for (let i = 0; i < nombres_blancas.length; i++) {
        loader.load(url_blancas[i], (model)=>{
        nombres_blancas[i] = new THREE.Mesh(model,new THREE.MeshLambertMaterial(colores_piezas[0]));
        nombres_blancas[i].scale.set(0.1, 0.1, 0.1);
        nombres_blancas[i].position.set(-1,2,0);
        nombres_blancas[i].rotation.set(-Math.PI/2.5, -Math.PI/30, -Math.PI/2.8);
        nombres_blancas[i].layers.set(50);
        scene.add(nombres_blancas[i]);
        });
    }
    for (let i = 0; i < nombres_negras.length; i++) {
        loader.load(url_negras[i], (model)=>{
        nombres_negras[i] = new THREE.Mesh(model,new THREE.MeshLambertMaterial(colores_piezas[1]));
        nombres_negras[i].scale.set(0.1, 0.1, 0.1);
        nombres_negras[i].position.set(-1,2,0);
        nombres_negras[i].rotation.set(-Math.PI/2.5, -Math.PI/30, -Math.PI/2.8);
        scene.add(nombres_negras[i]);
        });
    }
    for (let i = 0; i < nombres_otras.length; i++) {
        loader.load(url_otras[i], (model)=>{
        nombres_otras[i] = new THREE.Mesh(model,new THREE.MeshLambertMaterial(colores_piezas[2]));
        nombres_otras[i].scale.set(0.1, 0.1, 0.1);
        nombres_otras[i].position.set(-1,2,0);
        nombres_otras[i].rotation.set(-Math.PI/2.5, -Math.PI/30, -Math.PI/2.8);
        scene.add(nombres_otras[i]);
        });
    }
    for (let i = 0; i < nombre_carga_pago.length; i++) {
        loader.load(url_carga_pago[i], (model)=>{
        nombre_carga_pago[i] = new THREE.Mesh(model,new THREE.MeshLambertMaterial(colores_piezas[3]));
        nombre_carga_pago[i].scale.set(0.01, 0.01, 0.01);
        nombre_carga_pago[i].position.set(-1,2,0);
        nombre_carga_pago[i].rotation.set(-Math.PI/2.5, -Math.PI/30, -Math.PI/2.8);
        nombre_carga_pago[i].layers.set(40);
        scene.add(nombre_carga_pago[i]);
        });
    }
    for (let i = 0; i < nombre_cdg_dron.length; i++) {
        loader.load(url_cdg_dron[i], (model)=>{
        nombre_cdg_dron[i] = new THREE.Mesh(model,new THREE.MeshLambertMaterial(colores_piezas[4]));
        nombre_cdg_dron[i].scale.set(0.1, 0.1, 0.1);
        nombre_cdg_dron[i].position.set(-1,2,0);
        nombre_cdg_dron[i].rotation.set(-Math.PI/2.5, -Math.PI/30, -Math.PI/2.8);
        nombre_cdg_dron[i].layers.set(40);
        scene.add(nombre_cdg_dron[i]);
        });
    }
    for (let i = 0; i <= nombre_cdg_total.length; i++) {
        loader.load(url_cdg_total[i], (model)=>{
        nombre_cdg_total[i] = new THREE.Mesh(model,new THREE.MeshLambertMaterial(colores_piezas[5]));
        nombre_cdg_total[i].scale.set(0.01, 0.01, 0.01);
        nombre_cdg_total[i].position.set(-1,2,0);
        nombre_cdg_total[i].rotation.set(-Math.PI/2.5, -Math.PI/30, -Math.PI/2.8);
        nombre_cdg_total[i].layers.set(40);
        scene.add(nombre_cdg_total[i]);
        });
    }
    
    //---------------------------PROGRAMACIÓN DE LAS ACCIONES APLICADAS A LAS "CAPAS" AL CLICAR UNO U OTRO BOTÓN---------------------------------------
    const layers = {

        'Ocultar/Mostrar las Piezas Externas': function() {
            camera.layers.toggle (50);
            camera.layers.enable(40);
        },

        'Mostrar el Dron Completo': function () {
            camera.layers.enableAll();
        },

        'Ocultar el Dron Completo': function () {
            camera.layers.disableAll();
        }

    };

    //-----------------------------------------AÑADIR Graphical User Interface Y CONTROLES DEL RATÓN------------------------------------------------------
   
    const gui = new GUI();
    gui.add( layers, 'Ocultar/Mostrar las Piezas Externas');
    gui.add( layers, 'Mostrar el Dron Completo' );
    gui.add( layers, 'Ocultar el Dron Completo' );

    let control = new OrbitControls(camera, renderer.domElement);
    control.enablePan = false;
    control.minDistance = 2;
    // control.maxDistance = 19;
    control.enableDamping = true;
    control.dampingFactor = 0.05;
    control.maxPolarAngle = Math.PI;    //opcion por defecto; es el máximo
    control.target.set(3, 2, 5);

    //-----------------------------------------------------------POST-PROCESSING-------------------------------------------------------------------------
   
    composer = new EffectComposer(renderer);
    const renderPass = new RenderPass(scene, camera);
    composer.addPass(renderPass);

    outlinePass = new OutlinePass(new THREE.Vector2(window.innerWidth, window.innerHeight), scene, camera, layers);
    outlinePass.edgeStrength = 8;
    outlinePass.visibleEdgeColor.set("#0000ff");
    outlinePass.hiddenEdgeColor.set("#ff0000");
    composer.addPass(outlinePass);

    window.addEventListener("resize", onWindowResize);
    renderer.domElement.style.touchAction = "none";
    renderer.domElement.addEventListener("pointermove", onPointerMove);

    //----------------------------------------------------FUNCIONES PARA LAS ANIMACIONES--------------------------------------------------------------

    async function onPointerMove(event){
        if(event.isPrimary === false) return;

        mouse.x = (event.clientX/window.innerWidth)*2 - 1;
        mouse.y = -(event.clientY/window.innerHeight)*2 + 1;

        checkIntersection();
    }
    async function checkIntersection() {
        raycaster.setFromCamera(mouse, camera);
        const intersects = raycaster.intersectObject(scene, true);

        if (intersects.length > 0) {
            const selectedObject = intersects[0].object;
            addSelectedObject(selectedObject);
            outlinePass.selectedObjects = selectedObjects;
        } else {
            //outlinePass.selectedObjects = [];
        }
    }
    async function addSelectedObject(object){
        selectedObjects = [];
        selectedObjects.push(object);

    }
    async function onWindowResize(){
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize( window.innerWidth, window.innerHeight );
        composer.setSize( window.innerWidth, window.innerHeight );
    };

}