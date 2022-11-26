function get_sign_up_details() {
    let full_name = document.getElementById("fullName").value;
    let mobile_number = document.getElementById("mobileNumber").value;
    let email = document.getElementById('email').value
    let password = document.getElementById('passwordReg').value
    let first_name = full_name.split(" ")[0];
    let last_name = full_name.split(" ")[1];



    let sign_up_details = {
        first_name: first_name,
        last_name: last_name,
        mobile_number: mobile_number,
        email: email,
        password: password
    }
    send_details('sign_up', sign_up_details)
    // console.log(sign_up_details)
    //alert(sign_up_details)
    //console.log(sign_up_details['mobile_number'])

}


let case_valid = document.getElementById("PasswordValidationMessage");

function password_validation() {
    let password = document.getElementById("passwordReg").value;
    //let case_valid = document.getElementById("PasswordValidationMessage");
    if (reg_form.style.visibility = 'visible') {
        case_valid.style.visibility = "visible";


        lowercase_in_password = false;
        uppercase_in_password = false;
        digit_in_password = false;
        punctuation_in_password = false;

        if (/[a-z]/.test(password)) {
            lowercase_in_password = true;
        }

        if (/[A-Z]/.test(password)) {
            uppercase_in_password = true;
        }
        if (/[0-9]/.test(password))
            digit_in_password = true;
        if (/[~!@#$%^&*()_+}{:|?><-=;.,]/.test(password))
            punctuation_in_password = true;




        if (!lowercase_in_password || !uppercase_in_password) {

            case_valid.style.color = "red";
            case_valid.innerHTML = "Very weak: Password must contain at least one upper and one lower case";
        }
        else if (!digit_in_password) {

            case_valid.style.color = "darkred";
            case_valid.innerHTML = "Weak Password: Password must contain digit";

        }
        else if (!punctuation_in_password) {

            case_valid.style.color = "darkolivegreen";
            case_valid.innerHTML = "Average Password: Password must special character";
        }
        else if (password.length < 8) {

            case_valid.style.color = "darkolivegreen";
            case_valid.innerHTML = "Strong Password: Password must be at least 8 characters";
        }
        else {

            case_valid.style.color = "rgb(73, 237, 73)";
            case_valid.innerHTML = "Secure Password";
            return true
        }
    } else case_valid.style.visibility = "hidden";
}
// function username_input(){
//     let username_box = document.getElementById("username")
//     username_box.style.border="green solid 1px";
//     let username=username_box.value.trim();
//     if (username == "")
//         username_box.style.border="red solid 3px";
// }

function email_validator() {
    email_box = document.getElementById("email")
    email = email_box.value
    if (/^([a-zA-Z0-9]+)@([a-zA-z]+)\.(com)$/.test(email)) {
        document.getElementById("email").style.border = "green solid 3px"
    }
    else { document.getElementById("email").style.border = "red solid 3px" }
}
function mobile_number_validator() {
    let number_box = document.getElementById("mobileNumber")
    let mobile_number = number_box.value.split(" ").join("")
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

var login_form = document.getElementById('loginForm');
var reg_form = document.getElementById('regForm');
let sign_up_switch = document.getElementById('signUpSwitch');
let login_switch = document.getElementById('loginSwitch');
// var selector = document.getElementById('Selector');
// sign_up_switch.addEventListener('click', ()=>{
//     alert('hey')
// })
function switch_login_form() {
    login_switch.style.borderBottom='3px solid black';
    sign_up_switch.style.borderBottom='none';
    reg_form.style.display ='none';
    login_form.style.display='initial';
    
    
}
function switch_reg_form() {
    login_switch.style.borderBottom='none';
    sign_up_switch.style.borderBottom='3px solid black';
    login_form.style.display ='none';
    reg_form.style.display='initial';
}

var see_icon_reg = document.getElementById('seeIconReg');
var unsee_icon_reg = document.getElementById('unseeIconReg');
var see_icon_login = document.getElementById('seeIconLogin');
var unsee_icon_login = document.getElementById('unseeIconLogin');
let password_login = document.getElementById('passwordLogin');
let password_reg = document.getElementById('passwordReg');


let passwordReg = document.getElementById('Password');
function show_password() {
    password_reg.type = 'text';
    password_login.type='text';
    see_icon_reg.style.visibility='hidden';
    see_icon_login.style.visibility='hidden';
    unsee_icon_login.style.visibility = 'visible';
    unsee_icon_reg.style.visibility = 'visible';
}

function hide_password() {
    password_reg.type = 'password';
    password_login.type='password';
    see_icon_reg.style.visibility='visible';
    see_icon_login.style.visibility='visible';
    unsee_icon_login.style.visibility = 'hidden';
    unsee_icon_reg.style.visibility = 'hidden';
}
