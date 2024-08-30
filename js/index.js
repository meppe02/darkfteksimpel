const courses = ["tif083", "enn190", "tma970"];
const id = "courses";

// Base URL, adjusting for GitHub Pages
// Checks if the current host includes 'github.io', adjusts path accordingly
const baseURL = window.location.hostname.includes('github.io') ?
                '/darkfteksimpel/' : '/';

let htmlContent = courses.sort().map(course => {
    const upper = course.toUpperCase();
    const lower = course.toLowerCase();
    return `
        <div class="clickable">
            <a href="${baseURL}courses/${lower}/${lower}.html">
                ${upper}
            </a>
        </div>`;
}).join('');

document.getElementById(id).innerHTML = htmlContent;

