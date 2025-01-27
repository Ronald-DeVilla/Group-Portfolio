document.getElementById('convert-btn').addEventListener('click', async () => {
    const infix = document.getElementById('infix').value;
    const output = document.getElementById('output');
    const stepsTextBox = document.getElementById('steps');

    if (!infix) {
        output.innerHTML = '<p style="color: red;">Please enter a valid infix expression.</p>';
        return;
    }

    try {
        const response = await fetch('/infix_to_postfix', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ expression: infix })
        });

        const result = await response.json();

        if (response.ok) {
            output.innerHTML = `<p>${result.postfix}</p>`;
            stepsTextBox.innerHTML = result.steps.join('\n');
        } else {
            output.innerHTML = `<p style="color: red;">Error: ${result.error}</p>`;
        }
    } catch (error) {
        output.innerHTML = '<p style="color: red;">Failed to connect to the server.</p>';
    }
});