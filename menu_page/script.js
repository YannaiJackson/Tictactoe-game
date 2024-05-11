document.querySelectorAll(".menu-button").forEach(function(button) {
    button.addEventListener("click", function() {
        // Redirect to the new page with the clicked button's ID as a query parameter
        window.location.href = "../game_board/main.html?gameMode=" + this.id;
    });
});