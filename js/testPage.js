var addDivButton = document.getElementById('addDiv');
addDivButton.addEventListener('click', addDiv);

function addDiv()
{
    const divData = ['div1', 'div2', 'div3', 'div4', 'div5'];
    const parent = document.getElementById('main-div');
    divData.forEach(item => {
        const newDiv = document.createElement('div');
        newDiv.textContent = item;
        newDiv.className = 'child-div';
        parent.appendChild(newDiv);        
    });
}