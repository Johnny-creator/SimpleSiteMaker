//global variables
let toggleThemeBtn = document.getElementById("toggleThemeBtn");
let head = document.getElementsByTagName('HEAD')[0];
// let link = document.createElement('link');
let link = document.getElementById("toggleable")

// Configure the link element
// link.rel="stylesheet";

// localStorage.setItem("theme", "light");

toggleThemeBtn.addEventListener("click", function() {
    // Toggle the local storage session variable
    if (localStorage.getItem("theme") === "light") {
        localStorage.setItem("theme", "dark");
    }
    else {
        localStorage.setItem("theme", "light");
    }

    // console.log("{{ url_for('static', filename='scripts/" + localStorage.getItem("theme") + ".css') }}")
    // link.href = "{{ url_for('static', filename='css/" + localStorage.getItem("theme") + ".css') }}";
    link.href = "/static/css/" + localStorage.getItem("theme") + ".css";
    head.appendChild(link); 
    console.log(link)
})

window.addEventListener("load", function() {
    link.href = "/static/css/" + localStorage.getItem("theme") + ".css";
    console.log(localStorage.getItem("theme"))

    head.appendChild(link); 
})