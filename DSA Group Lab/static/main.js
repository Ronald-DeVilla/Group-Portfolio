async function updateDisplay() {
    try {
        const response = await fetch('/display');
        const result = await response.json();
        document.getElementById('list-display').textContent = JSON.stringify(result.list);
    } catch (error) {
        alert('Failed to fetch list: ' + error);
    }
}

async function addNode() {
    const data = document.getElementById('data-input').value;
    try {
        const response = await fetch('/add', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: `data=${encodeURIComponent(data)}`
        });
        const result = await response.json();
        updateDisplay();
        alert('Added: ' + data);
    } catch (error) {
        alert('Failed to add node: ' + error);
    }
}

async function removeBeginning() {
    try {
        const response = await fetch('/remove_beginning', {
            method: 'POST',
        });
        const result = await response.json();
        updateDisplay();
        alert('Removed from beginning: ' + result.removed);
    } catch (error) {
        alert('Failed to remove from beginning: ' + error);
    }
}

async function removeAtEnd() {
    try {
        const response = await fetch('/remove_at_end', {
            method: 'POST',
        });
        const result = await response.json();
        updateDisplay();
        alert('Removed from end: ' + result.removed);
    } catch (error) {
        alert('Failed to remove from end: ' + error);
    }
}

async function removeAt() {
    const data = document.getElementById('remove-data-input').value;
    try {
        const response = await fetch('/remove_at', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: `data=${encodeURIComponent(data)}`
        });
        const result = await response.json();
        updateDisplay();
        alert('Removed: ' + result.removed);
    } catch (error) {
        alert('Failed to remove specific node: ' + error);
    }
}

document.addEventListener('DOMContentLoaded', updateDisplay);
