document.addEventListener('DOMContentLoaded', function() {
    const calculatorForm = document.getElementById('calculatorForm');
    const resultContainer = document.getElementById('resultContainer');
    const resultText = document.getElementById('resultText');
    const backButton = document.getElementById('backButton');

    calculatorForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const num1 = parseFloat(document.getElementById('num1').value);
        const num2 = parseFloat(document.getElementById('num2').value);
        const operation = document.getElementById('operation').value;
        let result;

        switch (operation) {
            case 'add':
                result = num1 + num2;
                break;
            case 'subtract':
                result = num1 - num2;
                break;
            case 'multiply':
                result = num1 * num2;
                break;
            case 'divide':
                if (num2 !== 0) {
                    result = num1 / num2;
                } else {
                    result = 'Infinity';
                }
                break;
            default:
                result = 'Error';
                break;
        }

        resultText.textContent = `Result: ${result}`;
        resultContainer.style.display = 'block';
        calculatorForm.style.display = 'none';
    });

    backButton.addEventListener('click', function() {
        resultContainer.style.display = 'none';
        calculatorForm.style.display = 'block';
        calculatorForm.reset();
    });
});