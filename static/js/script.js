// static/js/script.js
console.log("Script loaded!");

// Toggle team cards on About page
document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll(".team-btn");
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            const target = document.querySelector(button.dataset.target);
            target.classList.toggle("d-none");
        });
    });
});
