async function generateTree() {
    const input = document.getElementById('nodeInput').value.trim();

    if (input.length === 0) {
      alert('Please enter node values.');
      return;
    }
    try {
      const response = await fetch('/generate-tree', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nodeInput: input }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        alert(`Error: ${errorData.error || 'An unknown error occurred'}`);
        return;
      }
      const data = await response.json();
      renderTree(data.nodes, data.lines);
    } catch (error) {
        console.error('Error:', error)
        alert('Failed to connect to the server.');
      }
  }

  function createNode(value, x, y) {
    const node = document.createElement('div');
    node.className = 'node';
    node.textContent = value;
    node.style.left = `${x}px`;
    node.style.top = `${y}px`;
    return node;
  }

  function createLine(x1, y1, x2, y2) {
    const line = document.createElement('div');
    line.className = 'line';
    const length = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
    line.style.width = `${length}px`;
    line.style.left = `${x1}px`;
    line.style.top = `${y1}px`;
    const angle = Math.atan2(y2 - y1, x2 - x1) * (180 / Math.PI);
    line.style.transform = `rotate(${angle}deg)`;
    return line;
  }

    function renderTree(nodes, lines) {
        const treeContainer = document.getElementById('tree');
        treeContainer.innerHTML = '';

        for (const nodeData of nodes){
          const node = createNode(nodeData.value, nodeData.x, nodeData.y);
          treeContainer.appendChild(node);
        }
        for (const lineData of lines){
            const line = createLine(lineData.x1, lineData.y1, lineData.x2, lineData.y2);
            treeContainer.appendChild(line);
        }

    }