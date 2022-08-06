function get_box_details(){
    let username= document.getElementById("username").value;


    let country= document.getElementById("country");



    //let countryText = country.options[country.selectedIndex].text;
    let info={
        username: username, 
        country: countryText
    }
    alertu(username)
    console.log(info)

}




function password_retype_check(){
    let password1 = document.getElementById("password").value
    let password2 = document.getElementById("password2").value
    let unmatch_error = document.getElementById("passworderror")
    if (password1 !== password2){
        unmatch_error.style.visibility = "visible"
    }
    else {
        unmatch_error.style.visibility = "hidden"
        return true
    }
}

function passwordvalidation() {
    let password = document.getElementById("password").value;
    let case_valid = document.getElementById("password_validation");

    lowercase_in_password = false;
    uppercase_in_password = false;
    digit_in_password = false;
    punctuation_in_password = false;

    if (/[a-z]/.test(password)){
    lowercase_in_password = true;}

    if (/[A-Z]/.test(password)){
    uppercase_in_password = true;}
    if (/[0-9]/.test(password))
    digit_in_password = true;
    if (/[~!@#$%^&*()_+}{:|?><-=;.,]/.test(password))
    punctuation_in_password = true;
   
  

    
    if (!lowercase_in_password || !uppercase_in_password)
    {
        case_valid.style.visibility ="visible";
        case_valid.style.color ="red";
        case_valid.innerHTML ="Very weak: Password must contain at least one upper and one lower case";
    }
    else if(!digit_in_password)
    {
        case_valid.style.visibility ="visible";
        case_valid.style.color ="yellow";
        case_valid.innerHTML ="Weak Password: Password must contain digit";

    }
    else if(!punctuation_in_password)
    {
        case_valid.style.visibility ="visible";
        case_valid.style.color ="darkolivegreen";
        case_valid.innerHTML ="Average Password: Password must special character";
    }
    else if(password.length <8)
    {
        case_valid.style.visibility ="visible";
        case_valid.style.color ="darkolivegreen";
        case_valid.innerHTML ="Strong Password: Password must be more than 8 characters";
    }
    else
    {
        case_valid.style.visibility ="visible";
        case_valid.style.color ="rgb(73, 237, 73)";
        case_valid.innerHTML ="Secure Password";
        return true
    }
    }
function username_input(){
    let username_box = document.getElementById("username")
    username_box.style.border="green solid 1px";
    let username=username_box.value.trim();
    if (username == "")
        username_box.style.border="red solid 3px";
}

function email_validator(){
    email_box = document.getElementById("email")
    email = email_box.value
    if (/^([a-zA-Z0-9]+)@([a-zA-z]+)\.(com)$/.test(email)){
        document.getElementById("email").style.border ="green solid 3px"
    }
    else {document.getElementById("email").style.border ="red solid 3px"}
}
function mobile_number_validator(){
    let number_box= document.getElementById("mobile_number")
    let mobile_number=number_box.value.split(" ").join("")
    console.log(mobile_number)
}
    
//to check if user name input is valid
function is_valid() {

    let username_box = document.getElementById("username")
    
    let username=username_box.value.trim()
    if (username == ""){
        username_box.style.border="red solid 3px";
        return false;
    } 
    else if (!(passwordvalidation()) || !(password_retype_check()))
    {
        username_box.style.border="green solid 1px";
        alert("Make sure all errors are corrected");
        return false;
    }
    else 
    {   
        detail_obj ={
            'username':document.getElementById("username").value,
            'password':document.getElementById("password").value,
            'mobile_numer':document.getElementById("mobile_number").value
        }
        console.log(detail_obj)
        alert("details recieved but no where to take you to lol...")
        
    }
}


