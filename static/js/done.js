let toggleNavStatus = false;

let toggleNav = function() { 
    let getSidebar = document.querySelector(".nav-sidebar");
    let getSidebarUl = document.querySelector(".nav-sidebar ul");
    let getSidebarTitle = document.querySelector(".nav-sidebar span")
    let getSidebarLinks = document.querySelectorAll(".nav-sidebar a");
    let getPhrase = document.querySelectorAll("#phrase")
    let getButton = document.querySelector(".btn-toggle-nav");

    if (toggleNavStatus === false) {
        getSidebarUl.style.visibility = "visible";
        getSidebar.style.width = String(1439 - 1132)+"px";
        getSidebarTitle.style.opacity = "1";
        getButton.style.backgroundColor = "#222";
        getButton.style.backgroundRepeat = "no repeat"
        getButton.style.backgroundImage = 'url("./static/hamx1.png")';
        getButton.style.backgroundSize = "100%";
        

        let arrayLength = getSidebarLinks.length;
        
        for (let i = 0; i < arrayLength; i++) {
            getSidebarLinks[i].style.opacity = "1";
        }

        let len = getPhrase.length;
        for (let i = 0; i < len; i++) {
            getPhrase[i].style.opacity = "1";
        }

        toggleNavStatus = true;
    }

    else if (toggleNavStatus === true) {
        getButton.style.backgroundColor = "white";
        getButton.style.backgroundImage = 'url("./static/hamburger.png")';
        getButton.style.backgroundSize = "50%";
        getSidebar.style.width = "0px";
        getSidebarTitle.style.opacity = "0";



        let arrayLength = getSidebarLinks.length;
        
        for (let i = 0; i < arrayLength; i++) {
            getSidebarLinks[i].style.opacity = "0";
        }

        getSidebarUl.style.visibility = "visible";

        let len = getPhrase.length;
        for (let i = 0; i < len; i++) {
            getPhrase[i].style.opacity = "0";
        }

        toggleNavStatus = false;
    }

    
}