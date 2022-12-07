// $(document).ready(function(){

//     $nav=$('.nav');
//     $toggleCollapse=$('.toggle-collapse');

//     /**click event on toggle menu*/
//     $toggleCollapse.click(function () {
//       $nav.toggleClass('collapse');
//     })


//     /* Show nav-items*/
    


    
//   });


let close_btn = document.getElementById('closeMenuBtn');
//const menu_items = document.getElementsByClassName('menu_items');
let menu_btn2 = document.querySelector('#openMenuBtn');
let menu_items = document.querySelector('.nav-items')



menu_btn2.addEventListener('click',() =>{
  
    close_btn.style.display='inline-block';
    menu_btn2.style.display='none'
    menu_items.style.display='flex'
  
}
)

close_btn.addEventListener('click',function() {

  close_btn.style.display='none';
  menu_btn2.style.display='inline-block';
  menu_items.style.display='none'
})


$(window).resize(function() {
  if ($(window).width() > 750){
    close_btn.style.display='none';
    menu_btn2.style.display='none'
    menu_items.style.display='flex'
  }
  else{
    close_btn.style.display='none';
    menu_btn2.style.display='inline-block'
    menu_items.style.display='none'
  }
    
});
