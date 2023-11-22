if (!localStorage.getItem(`counter`)) {
    localStorage.setItem(`counter`, 0);
}
function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;
               
    }
    document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count;
    });
        