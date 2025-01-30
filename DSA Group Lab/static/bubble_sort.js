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
    array.forEach(value => {
        const bar = document.createElement('div');
        bar.className = 'bar';
        bar.style.height = `${value * 3}px`;
        bar.textContent = value;
        arrayContainer.appendChild(bar);
    });
  }
  
  function updateBars(array) {
    const arrayContainer = document.getElementById('arrayContainer');
    const bars = arrayContainer.querySelectorAll('.bar');
    bars.forEach((bar, index) => {
      bar.style.height = `${array[index] * 3}px`;
      bar.textContent = array[index];
    });
  }
  
  function visualizeBubbleSort(array) {
      fetch('http://127.0.0.1:5000/sort', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ array })
      })
      .then(response => response.json())
      .then(data => {
          if (data.error) {
              alert(data.error);
          } else {
              updateBars(data.sortedArray);
          }
      })
      .catch(error => console.error('Error:', error));
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
      visualizeBubbleSort(array);
  });