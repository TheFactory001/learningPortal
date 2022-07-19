const h3Clicker = () => {
    const header = document.getElementById("headers").textContent
    document.getElementById("resourceTopic").innerHTML = header
    document.getElementById("list").innerHTML = `<li><a href="https://climate.ucdavis.edu/AM341.pdf" target="_blank"> Intro to Computational Math </a></li>`;
}

const h3ClickerML = () => {
    const header = document.getElementById("headersML").textContent
    document.getElementById("resourceTopic").innerHTML = header
    document.getElementById("list").innerHTML = `<li><a href="https://alex.smola.org/drafts/thebook.pdf" target="_blank"> Intro to Machine Learning </a></li>`;
}