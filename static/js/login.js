function get_sign_up_details(){
    let full_name= document.getElementById("FullName").value;
    let mobile_number= document.getElementById("MobileNumber").value;
    let email =document.getElementById('Email').value
    let password = document.getElementById('Password').value


    let sign_up_details={
        full_name:full_name,
        mobile_number:mobile_number,
        email:email,
        password:password
    }
    console.log(sign_up_details)
    //alert(sign_up_details)
    console.log(sign_up_details['mobile_number'])
    alert('done')


}

/** 
function get_login_details(e) {
    e.preventDefault();
    let email =document.getElementById("loginEmail").value;
    let password =document.getElementById("loginPassword").value;
    let login_details={
        email:email,
        password:password
    };
    console.log(login_details);
}

*/

// Gets a reference to the form element
var form = document.getElementById('LoginForm');

// Adds a listener for the "submit" event.
form.addEventListener('submit', function(e) {

  e.preventDefault();
  let email =document.getElementById("loginEmail").value;
  let password =document.getElementById("loginPassword").value;
  let login_details={
      email:email,
      password:password
  };
  console.log(login_details);

});

function password_validation() {
    let password = document.getElementById("Password").value;
    let case_valid = document.getElementById("PasswordValidationMessage");

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
        case_valid.style.color ="darkred";
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
// function username_input(){
//     let username_box = document.getElementById("username")
//     username_box.style.border="green solid 1px";
//     let username=username_box.value.trim();
//     if (username == "")
//         username_box.style.border="red solid 3px";
// }

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

    // let username_box = document.getElementById("username")
    
    // let username=username_box.value.trim()
    // if (username == ""){
    //     username_box.style.border="red solid 3px";
    //     return false;
    // } 
    // else if (!(passwordvalidation()) || !(password_retype_check()))
    // {
    //     username_box.style.border="green solid 1px";
    //     alert("Make sure all errors are corrected");
    //     return false;
    // // }
    // else 
    // {   
    //     detail_obj ={
    //         'username':document.getElementById("username").value,
    //         'password':document.getElementById("password").value,
    //         'mobile_numer':document.getElementById("mobile_number").value
    //     }
    //     console.log(detail_obj)
    //     alert("details recieved but no where to take you to lol...")
        
    // }
}

var login_form=document.getElementById('LoginForm');
var reg_form = document.getElementById('RegForm');
var selector = document.getElementById('Selector');
function switch_login_form(){
    
    // login_form.style.transform = "translateX(100%)"
    // reg_form.style.transform = "translateX(-100%)"
    login_form.style.visibility="visible"
    reg_form.style.visibility="hidden"
    selector.style.transform ="translateX(11rem)"


    // form_title.innerHTML="Login Form"

}
function switch_reg_form(){
    // login_form.style.transform = "translateX(0)"
    // reg_form.style.transform = "translateX(0)"
    login_form.style.visibility="hidden"
    reg_form.style.visibility="visible"
    selector.style.transform ="translateX(2rem)"
    // form_title.innerHTML="Registration Form"

}
