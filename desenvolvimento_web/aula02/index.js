document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('itemForm');
    const tableBody = document.querySelector('#itemTable tbody');

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        
        const name = document.getElementById('name').value;
        const address = document.getElementById('address').value;
        const telephone = document.getElementById('telephone').value;

        const newRow = document.createElement('tr');
        const nameCell = document.createElement('td');
        const addressCell = document.createElement('td');
        const telephoneCell = document.createElement('td');

        nameCell.textContent = name;
        addressCell.textContent = address;
        telephoneCell.textContent = telephone;

        newRow.appendChild(nameCell);
        newRow.appendChild(addressCell);
        newRow.appendChild(telephoneCell);

        tableBody.appendChild(newRow);

        form.reset();
    });
});