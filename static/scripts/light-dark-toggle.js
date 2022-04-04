//global variables
let toggleThemeBtn = document.getElementById("toggleThemeBtn");
let head = document.getElementsByTagName('HEAD')[0];
// let link = document.createElement('link');
let link = document.getElementById("toggleable")

toggleThemeBtn.addEventListener("click", function() {
    // Toggle the local storage session variable
    if (localStorage.getItem("theme") === "light") {
        localStorage.setItem("theme", "dark");
    }
    else {
        localStorage.setItem("theme", "light");
    }

    link.href = "/static/css/" + localStorage.getItem("theme") + ".css";
    head.appendChild(link); 
})

window.addEventListener("load", function() {
    link.href = "/static/css/" + localStorage.getItem("theme") + ".css";
    head.appendChild(link); 
})