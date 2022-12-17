
let menu_display_btn = document.getElementById("menuDisplay");
let menu_close_btn = document.getElementById("menuClose");
let nav_items = document.getElementById('navList');
menu_display_btn.addEventListener('click',()=>{
    menu_display_btn.style.display = 'none';
    menu_close_btn.style.display='inline-block';
    nav_items.style.display ='inline-block';
}
)
menu_close_btn.addEventListener('click',()=>{
    
    menu_close_btn.style.display='none';
    nav_items.style.display ='none';
    menu_display_btn.style.display = 'inline-block';

})
