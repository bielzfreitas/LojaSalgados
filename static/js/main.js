document.addEventListener('DOMContentLoaded', () => {
    const orderForm = document.getElementById('order-form');
    const orderList = document.getElementById('order-list');

    orderForm.addEventListener('submit', (event) => {
        event.preventDefault();
        
        const formData = new FormData(orderForm);
        const orderItem = formData.get('salgado');

        if (orderItem) {
            const listItem = document.createElement('li');
            listItem.textContent = `Você pediu: ${orderItem}`;
            orderList.appendChild(listItem);
            orderForm.reset();
        } else {
            alert('Por favor, selecione um salgado.');
        }
    });
});