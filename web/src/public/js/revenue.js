menu_open=false;
function menuToggle(){
 if(menu_open){
   document.getElementById("menuContent").innerHTML="";
 }else{
   document.getElementById("menuContent").innerHTML="<a href=\"/\" >Home</a><a href=\"/product\" >Product Details</a><a href=\"/kvp\" >KVP</a><a href=\"/info_arch\" >Information Architecture</a><a href=\"/pivot\" >Pivot</a>";
 }
  menu_open=!menu_open;
}
