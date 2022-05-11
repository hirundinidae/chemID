let cards = document.querySelectorAll(".card-back");
cards.forEach(button => {
    button.addEventListener("click", flip);
});
cards.forEach(button => {
    //button.addEventListener("mouseover", expand);
});
document.querySelector("#expand-button").addEventListener("click",expand);
let expands = document.querySelectorAll(".expand");
expands.forEach(expand => {
    expand.style.display="none";
});

function flip() {
    this.classList.toggle("is-flipped");
}

function expand() {
    cards.forEach(card => {
        card.classList.toggle("is-expanded");
        let summaries = document.querySelectorAll(".summary");
        let expands = document.querySelectorAll(".expand");
        if (card.classList.contains("is-expanded")){
            summaries.forEach(summary => {
                summary.style.display="none";
            });
            expands.forEach(expand => {
                expand.style.display="block";
            });
        }else {
            summaries.forEach(summary => {
                summary.style.display="block";
            });
            expands.forEach(expand => {
                expand.style.display="none";
            });
        }

    });
}
