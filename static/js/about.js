const h3Clicker = () => {
    const header = document.getElementById("headers").textContent
    document.getElementById("resourceTopic").innerHTML = header
    document.getElementById("list").innerHTML = `<li><a href="https://climate.ucdavis.edu/AM341.pdf" target="_blank"> Intro to Computational Math </a></li>`;
}

const h3ClickerML = () => {
    const header = document.getElementById("headersML").textContent
    document.getElementById("resourceTopic").innerHTML = header
    document.getElementById("list").innerHTML 
        = `
            <li><a href="https://alex.smola.org/drafts/thebook.pdf" target="_blank"> Intro to Machine Learning </a></li>
            <li><a href="https://developers.google.com/machine-learning/intro-to-ml" target="_blank"> Machine Learning by Google</li>
        `;
}


const h3ClickerAI = () => {
    const header = document.getElementById("headersAI").textContent
    document.getElementById("resourceTopic").innerHTML = header
    document.getElementById("list").innerHTML 
        = `
            <li><a href="https://www.edx.org/course/cs50s-introduction-to-artificial-intelligence-with-python" target="_blank"> Intro to Artificial Intelligence </a></li>
        `;
}

const h3ClickerSec = () => {
    const header = document.getElementById("headerSec").textContent
    document.getElementById("resourceTopic").innerHTML = header
    document.getElementById("list").innerHTML 
        = `
            <li><a href="https://www.sans.org/cyber-security-courses/automating-information-security-with-python/ target="_blank"> Intro to Cyber Security in Python </a></li>
        `;
}