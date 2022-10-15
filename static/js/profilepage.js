
function display_info(profile_data){
    
    //let city = document.getElementById("city");
    //city.innerHTML =profile_data['city'];
    //let email = document.getElementById("email");
    //email.innerHTML = profile_data['email'];
    //let level = document.getElementById("level");
    //level.innerHTML= profile_data['level'];
    //let phone_number = document.getElementById('phoneNumber');
    //phone_number.innerHTML= profile_data['phone'];
    let address = document.getElementById('address');
    address.innerHTML = profile_data['address']

    //let personal_site = document.getElementById('personalSite');
    //personal_site.innerHTML= profile_data['personal_site'];

    //let github_link = document.getElementById("githubLink");
    //github_link.innerHTML = profile_data['github_link'];
    let name = document.getElementById('fullName');
    name.innerHTML = profile_data['name'];
    //let years_with_factory = document.getElementById("yearsWithFactory");
    //years_with_factory.innerHTML = profile_data['years_with_factory'];

}
// let profile_data = '{{profile_data}}';

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
    //display_info(data)
})