document.addEventListener('DOMContentLoaded', function() {
    const counterElement = document.getElementById('counter');
    const clickButton = document.getElementById('clickButton');

    clickButton.addEventListener('click', function() {
        let currentValue = parseInt(counterElement.textContent);
        currentValue++;
        counterElement.textContent = currentValue;
        counterElement.classList.add('animate');
        setTimeout(() => {
            counterElement.classList.remove('animate');
        }, 300);
    });
});