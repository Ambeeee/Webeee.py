//DEFAULTS
window.onload = function(){
    var popup = document.getElementById('eliminaPopup')
    popup.classList.toggle('dNone')
    
}


function ApriMenu(){
    menu = document.getElementById("menu");
    logo = document.getElementById("logo");
    if(menu.style.display == "none"){
        menu.style.display = "flex";
    }
    else{
        menu.style.display = "none";
    }
}
function menuOn(){
    menu = document.getElementById("menuBox")
    icona = document.getElementById("frecciaMenu")
    menu.style.display = "block"
    icona.style.display = "none"
}
function menuOff(){
    menu = document.getElementById("menuBox")
    icona = document.getElementById("frecciaMenu")
    menu.style.display = "none"
    icona.style.display = "block"
}
//DARKMODE
function DM(){
    document.body.classList.toggle("Dm")
    console.log("blink")
}

function login(){
window.location.href = "/login"; 
}
function TogglePopup(){ 
    var tutto = document.getElementById('tutto')
    var popup = document.getElementById('eliminaPopup')
    var cancel = document.getElementById('cancel')

    tutto.classList.toggle('dNone')
    popup.classList.toggle('dNone')
    cancel.onclick=function(){
        tutto.classList.toggle('dNone')
        popup.classList.toggle('dNone')
    }
}

function scopri(element){
    element.style.display = 'flex'
}