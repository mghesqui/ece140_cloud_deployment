menu_open=false;
function menuToggle(){
 if(menu_open){
   document.getElementById("menuContent").innerHTML="";
 }else{
   document.getElementById("menuContent").innerHTML="<a href=\"/\" >Home</a><a href=\"/product\" >Product Details</a><a href=\"/kvp\" >KVP</a><a href=\"/revenue\" >Revenue Model</a>";
 }
  menu_open=!menu_open;
}
