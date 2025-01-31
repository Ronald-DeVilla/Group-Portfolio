function generateRandomArray(size) {
    let arr = [];
    for (let i = 0; i < size; i++) {
        arr.push(Math.floor(Math.random() * 100) + 1);
    }
    return arr;
}

function generateBars(array) {
    const arrayContainer = document.getElementById('arrayContainer');
    arrayContainer.innerHTML = '';
    const maxValue = Math.max(...array);
    array.forEach(value => {
        const bar = document.createElement('div');
        bar.className = 'bar';
        const normalizedHeight = (value / maxValue) * 100;
        bar.style.height = `${normalizedHeight}%`;
        bar.textContent = value;
        arrayContainer.appendChild(bar);
    });
}

function visualizeQuickSort(array) {
      fetch('http://127.0.0.1:5000/quick-sort', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ array })
      })
      .then(response => response.json())
      .then(data => {
          if (data.error) {
              alert(data.error);
          } else {
            visualizeSteps(data.steps, data.sortedArray);
          }
      })
      .catch(error => console.error('Error:', error));
}


function visualizeSteps(steps, original) {
    let stepIndex = 0;
    const maxValue = Math.max(...original)

    function renderStep() {
       if (stepIndex < steps.length) {
            const currentStep = steps[stepIndex]
            const arrayContainer = document.getElementById('arrayContainer');
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

document.getElementById('runSort').addEventListener('click', () => {
    const arraySize = document.getElementById('arraySize').value;
    const arrayValues = document.getElementById('arrayValues').value;
    let array = [];

    if (arrayValues) {
        array = arrayValues.split(',').map(Number);
    } else {
        array = generateRandomArray(parseInt(arraySize));
    }

    generateBars(array);
    visualizeQuickSort(array);
});