let faithTitles = document.getElementsByClassName('faithTitle');
let faithTitleArray = Array.from(faithTitles).map((faithTitles) => faithTitles.textContent);

let backToTopBtn = document.querySelector(".backToTopBtn");

faithTitleArray.forEach(print);

function print(element, index){
    let faithTableBody = document.getElementById("faithTableBody");
    let row = faithTableBody.insertRow();

    // Add a class to the row for styling purposes
    row.classList.add("faithTitleRow");

    // Create a cell in the row
    let cell = row.insertCell(0);
    let link = document.createElement("a");
    link.setAttribute("id", "title-" + index);
    link.innerText = element;
    cell.appendChild(link);
    
    // Add click event listener to the row
    row.addEventListener('click', () => {
        document.getElementById(`section-${index}`).scrollIntoView();
    });
    
    console.log(element);
}

faithTitleArray.forEach((title, index) => {
    let link = document.getElementById(`title-${index}`);
    let row = link.parentNode.parentNode; // Get the parent row of the title element
    row.addEventListener('click', () => {
        document.getElementById(`section-${index}`).scrollIntoView();
    });
});


/*
faithTitleArray.forEach((title, index) => {
    document.getElementById(`title-${index}`).row.addEventListener('click', () => {
        document.getElementById(`section-${index}`).scrollIntoView();
    });
});
*/



// Back to top button

window.addEventListener('scroll', checkHeight)

function checkHeight(){
    if(window.scrollY > 20) {
        backToTopBtn.classList.add("active");
    } else {
        backToTopBtn.classList.remove("active");
    }
}


backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0
    })
})