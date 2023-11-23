if (!localStorage.getItem(`counter`)) {
    localStorage.setItem(`counter`, 0);
}
function count() {
    let counter = localStorage.getItem(`counter`);
    counter++;
    document.querySelector('h1').innerHTML = counter;
    
               
    }
    document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count;
    });
        