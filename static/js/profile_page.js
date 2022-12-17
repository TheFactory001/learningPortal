
$(document).ready(function () {
    
    var data = JSON.parse(userData);
    console.log(data)
    let name = document.getElementById('fullName');
    name.innerHTML = data['name'];
    let address = document.getElementById('contactAddress');
    address.innerHTML = data['address']
    let phone_number = document.getElementById('phoneNumber');
    phone_number.innerHTML= data['phone'];
    let github_link = document.getElementById("githubLink");
    github_link.innerHTML = data['github'];
    let level = document.getElementById("level");
    level.innerHTML= data['level'];
    let email = document.getElementById("email");
    email.innerHTML = data['email'];
    let city = document.getElementById("city");
    city.innerHTML = data['city'];
    //interest0
    let interestA = document.getElementById("interest1");
    interestA.innerHTML = data['interest1'];
    let interestB = document.getElementById("interest2");
    interestB.innerHTML = data['interest2'];

    if(data['imageUri']){
        let image = document.getElementById("profileImage");
        image.src = data['imageUri'];
    }
   


})
let timeline =document.getElementById('timeline')
let contact_info = document.getElementById('contactInfo')
let timeline_btn = document.getElementById('timelineBtn')
let about_btn = document.getElementById('aboutBtn')

function showContact() {
    timeline.style.display='none';
    contact_info.style.display='flex';
    contact_info.style.flexDirection='column';
    about_btn.style.color='#6495ED'
    about_btn.style.fontSize='18px'
    timeline_btn.style.color='black'
    timeline_btn.style.fontSize='15px'
    
    // var contact = document.getElementsByClassName("contact_info");
    // var assessment = document.getElementsByClassName("assessment");
    // var contactButton = document.getElementsByClassName("contact");
    // var assessButton = document.getElementsByClassName("assess");
    // //assessment.style.display = "none"
    // //contact.style.display = "block"
    // for(var i = 0; i < assessment.length; i++){
    //     //contact[i].style.visibility = "hidden";
    //     assessment[i].style.display = "none"; 
    // }

    // for(var i = 0; i < contact.length; i++){
    //     //contact[i].style.visibility = "hidden";
    //     contact[i].style.display = "block";
    // }

    // for(var i = 0; i < contactButton.length; i++){
    //     contactButton[i].style.display = "none";
    // }

    // for(var i = 0; i < assessButton.length; i++){
    //     assessButton[i].style.display = "block";
    // }
  }

  function showAssessment() {
   
    // var contact = document.getElementsByClassName("contact_info");
    // var assessment = document.getElementsByClassName("assessment");
    // var contactButton = document.getElementsByClassName("contact");
    // var assessButton = document.getElementsByClassName("assess");
        timeline.style.display='block'
        contact_info.style.display='none'
        about_btn.style.color='black'
        about_btn.style.fontSize='15px'
        timeline_btn.style.color='#6495ED'
        timeline_btn.style.fontSize='18px'


    // //assessment.style.display = "none"
    // //contact.style.display = "block"
    // for(var i = 0; i < assessment.length; i++){
    //     //contact[i].style.visibility = "hidden";
    //     assessment[i].style.display = "block"; 
    // }

    // for(var i = 0; i < contact.length; i++){
    //     //contact[i].style.visibility = "hidden";
    //     contact[i].style.display = "none";
    // }

    // for(var i = 0; i < contactButton.length; i++){
    //     contactButton[i].style.display = "block";
    // }

    // for(var i = 0; i < assessButton.length; i++){
    //     assessButton[i].style.display = "none";
    // }


  }
  function alertSubmit(){
    alert("You have successfully submitted your assessment")
  }