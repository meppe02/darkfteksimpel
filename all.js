// Base URL, adjusting for GitHub Pages or local hosting
const isGitHub = window.location.hostname.includes('github.io');
const repoName = 'darkfteksimpel'; // Repository name
const url = isGitHub ? `/${repoName}/` : 'http://127.0.0.1:5500/darkfteksimpel/';
const expfysen_url = "https://stekpannan02.github.io/Expfys-calculator/";
const svgUrl = url + 'images/ftek.svg'; // Path to your local SVG file
const hem_state=false 
// Function to check website status and update link accordingly
function checkAndUpdateLink() {
    fetch(expfysen_url, { method: 'HEAD' })
        .then(response => {
            const linkText = response.ok ? "Expfysräknare" : "Expfysräknare (Nere)";
            updateNavbarLink(linkText);
        })
        .catch(error => {
            console.error('Error accessing the website:', error);
            updateNavbarLink("Expfysräknare (Error)");
        });
}

// Function to update the navbar links
function updateNavbarLink(text) {
    const navbarList = document.querySelector('.navbar-list');
    const navbarListDropDown = document.querySelector('.navbar-list-drop');
    const logoHTML = `
        <a href="${url}index.html" class="logo-box">
            <img src="${svgUrl}" class="logo"/>
        </a>
    `; // Add SVG logo

    let linksHTML = (hem_state)?'<li><a href="${url}index.html" class="nav-items">Hem</a></li>':''
    linksHTML+=`
        <li><a href="${url}about.html" class="nav-items">Om oss</a></li>
        <li><a href="${expfysen_url}" class="nav-items">${text}</a></li>
    `;
    
    if (navbarList) {
        navbarList.innerHTML = logoHTML + linksHTML;
    }
    if (navbarListDropDown) {
        navbarListDropDown.innerHTML = linksHTML;
    }
}

// Main function to initialize the navbar and other elements
function main() {
    console.log("DOM fully loaded and parsed");
    document.body.innerHTML = `
        <nav class="navbar">
        
            <ul class="navbar-list">
                <!-- Links will be populated by checkAndUpdateLink function -->
            </ul>
            <div id="burger">
                <div></div>
                <div></div>
                <div></div>
            </div>
            <div id="drop-down" class="not-active">
                <ul class="navbar-list-drop">
                    <!-- Links will be populated by checkAndUpdateLink function -->
                </ul>
            </div>
            
        </nav>
        ${document.body.innerHTML}
        <footer>&copy DARKFTEK (darkftek@gmail.com)</footer>
    `;
    console.log("Navbar and footer added to DOM");

    // Update the navbar links with the SVG logo
    checkAndUpdateLink();

    // Burger menu event listener
    document.getElementById("burger").addEventListener("click", () => {
        const dropDown = document.getElementById("drop-down");
        if (dropDown.classList.contains("not-active")) {
            dropDown.classList.remove("not-active");
            dropDown.classList.add("active");
        } else {
            dropDown.classList.remove("active");
            dropDown.classList.add("not-active");
        }
    });
}
 
// Run the main function
main();
