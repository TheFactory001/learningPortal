
$(document).ready(function () {
    var data = JSON.parse(userData);
    //console.log(data)
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
    let interestA = document.getElementById("interest0");
    interestA.innerHTML = data['interest1'];
    let interestB = document.getElementById("interest1");
    interestB.innerHTML = data['interest2'];

    if(data['imageUri']){
        let image = document.getElementById("profileImage");
        image.src = data['imageUri'];
    }
})