
const questions = 
[
    "You are offered two different sales jobs. The first company offers a straight commission of 6% of the sales" +
    ". The second company offers a salary of 390 per week plus 1% of the sales. How much would you have to sell in " + 
    "a week for the straight commission offer to be at least as good?",
    "Two times a number plus three times another number equals 44. Three times the first number plus four times the other number is 77. Find the numbers.",
    "Twelve less than four times a number is the same as six times the number. How do you find the number?",
    "Susana and Lawrence are running on a track. Susana finishes one lap every 5 minutes and Lawrence finishes one lap every 8 minutes." + 
    "If they both start at the same time, after how many minutes will they be side by side again?",
    "The difference between two numbers is 20. Three times the smaller number is 44 more than the larger number. What are the numbers?",
    "If eight times a number equals 24 more than two times that number, what is the number?",
    "How do you find the greatest common factor of 20 and 28?"
]

const qualitatives = 
[
    "print ( 10 + 20 ) = ___________", "print ( 40 + 20 ) = ___________", "print ( 34 * 2 ) = ___________",
    "print ( ____ + ____ ) = 50" , "_________ ( ____ * ___ ) = 33", "print ( \"We are going to \" + \"school\" ) = ___________",
    "print ( \"We will arrive at \" + 2 ) = ______________", 
    "print ( \"Number of days in a leap year is \" + _____________ ) = \"Number of days in a leap year is 366\"",
]

for (let i = 0; i < questions.length; i++) {
    document.getElementById("questionHolder").innerHTML += `<div id="question"> ${i+1}. ${questions[i]} </div> <br>`;
}

for (let i = 0; i < qualitatives.length; i++) {
    document.getElementById("qualitativeHolder").innerHTML += `<div id="question"> ${qualitatives[i]} </div> <br>`;
}
