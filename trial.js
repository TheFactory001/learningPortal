function passwordvalidation() {
    
var password = document.getElementById("password").value;

var upper_case = "ABCDEFHIJKLMNOPQRSTUVWXYZ";
var lower_case= "abcdefghijklkmnopqrstuvwxyz";
var digit= "1234567890";
var punctuation = "~!@#$%^&*()_+}{:\"|?><`-=][\\';\/.,]";

lowercase_in_password = false;
uppercase_in_password = false;
digit_in_password = false;
punctuation_in_password = false;
for (i in password){
    
    var each_char = password[i];

    if (lower_case.includes(each_char)) 
    lowercase_in_password = true;

    if (upper_case.includes(each_char)) 
    uppercase_in_password = true;

    if (digit.includes(each_char)) 
    digit_in_password = true;

    if (punctuation.includes(each_char)) 
    punctuation_in_password = true;

}
var case_valid = document.getElementById("passwordvalidation");
if (!lowercase_in_password || !uppercase_in_password) {
    case_valid.style.visibility ="visble";
    case_valid.style.color ="red";
    case_valid.style.text = "Password must contain upper and lower case";
}
}
password="123"
console.log(password.length)