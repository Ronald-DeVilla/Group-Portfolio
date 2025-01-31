const runButton = document.getElementById('runButton');
const arrayContainer = document.getElementById('arrayContainer');
const arraySizeInput = document.getElementById('arraySize');
const arrayValuesInput = document.getElementById('arrayValues');

runButton.addEventListener('click', async () => {
    const size = parseInt(arraySizeInput.value);
    const valuesInput = arrayValuesInput.value;
    let array = [];

    if (valuesInput) {
        array = valuesInput.split(',').map(Number);
        if (array.length !== size) {
            alert(`Please provide exactly ${size} values.`);
            return;
        }
    } else {
        array = Array.from({ length: size }, () => Math.floor(Math.random() * 100) + 1);
    }

    const response = await fetch('/insertion-sort', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ size, values: array }),
    });
    const data = await response.json();

    visualizeSteps(data.steps, data.original)
});


function visualizeSteps(steps, original) {
    let stepIndex = 0;

    const maxValue = Math.max(...original)
    function renderStep() {
        if (stepIndex < steps.length) {
             const currentStep = steps[stepIndex]
             arrayContainer.innerHTML = '';
             currentStep.forEach((value) => {
                const bar = document.createElement('div');
                 const normalizedHeight = (value / maxValue) * 100;
                 bar.style.height = `${normalizedHeight}%`;
                bar.classList.add('bar');
                 bar.textContent = value;
                 arrayContainer.appendChild(bar);
            });
            stepIndex++;
            setTimeout(renderStep, 500);
        }
    }
    renderStep()
}