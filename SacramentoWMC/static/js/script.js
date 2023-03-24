
let faithTitles = document.getElementsByClassName('faithTitle');
let faithTitleArray = Array.from(faithTitles).map((faithTitles) => faithTitles.textContent);
 
faithTitleArray.forEach(print);

function print(element, index){
    let faithTableBody = document.getElementById("faithTableBody");
    let row = faithTableBody.insertRow();
    let cell = row.insertCell(0);
    let link = document.createElement("a");
    link.setAttribute("id", "title-" + index);
    link.innerText = element;
    cell.appendChild(link);
    
    
    console.log(element);
}

faithTitleArray.forEach((title, index) => {
    document.getElementById(`title-${index}`).addEventListener('click', () => {
        document.getElementById(`section-${index}`).scrollIntoView();
    });
});