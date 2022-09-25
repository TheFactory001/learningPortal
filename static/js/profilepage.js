



function display_info(){
    let profile_data = JSON.parse(document.getElementById("profileData").dataset.profiledata)
    
    let city = document.getElementById("city");
    city.innerHTML =profile_data['city'];
    let email = document.getElementById("email");
    email.innerHTML = profile_data['email'];
    let level = document.getElementById("level");
    level.innerHTML= profile_data['level'];
    let phone_number = document.getElementById('phoneNumber');
    phone_number.innerHTML= profile_data['phone_number'];
    let address = document.getElementById('address');
    address.innerHTML = profile_data['address']

    let personal_site = document.getElementById('personalSite');
    personal_site.innerHTML= profile_data['personal_site'];
    


    let github_link = document.getElementById("githubLink");
    github_link.innerHTML = profile_data['github_link'];
    let name = document.getElementById('fullName');
    name.innerHTML = profile_data['full_name'];
    let years_with_factory = document.getElementById("yearsWithFactory");
    years_with_factory.innerHTML = profile_data['years_with_factory'];

    console.log(profile_data)
    alert(profile_data)
}
// let profile_data = '{{profile_data}}';