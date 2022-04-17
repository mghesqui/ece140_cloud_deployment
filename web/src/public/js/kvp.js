menu_open=false;
function menuToggle(){
 if(menu_open){
   document.getElementById("menuContent").innerHTML="";
 }else{
   document.getElementById("menuContent").innerHTML="<a href=\"/\" >Home</a><a href=\"/product\" >Product Details</a>";
 }
  menu_open=!menu_open;
}
