document.getElementById('generateBtn').addEventListener('click', async () => {
    const city = document.getElementById('cityInput').value;
    const vibe = document.getElementById('vibeInput').value;
    const budget = document.getElementById('budgetInput').value;
    const terminal = document.getElementById('terminalOutput');

    terminal.innerHTML = "> INITIATING WRANGLER ENGINE...\n";

    const response = await fetch('http://localhost:8000/api/generate_itinerary', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({city, vibe, budget})
    });

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    while(true) {
        const {value, done} = await reader.read();
        if(done) break;

        const chunk = decoder.decode(value);
        const lines = chunk.split('\n');
        for(const line of lines) {
            if(line.startsWith('data: ')) {
                const data = JSON.parse(line.substring(6));
                if(data.status) {
                    terminal.innerHTML += `> ${data.status}\n`;
                }
                if(data.payload) {
                    terminal.innerHTML += `\n[PAYLOAD RECEIVED]:\n${JSON.stringify(data.payload, null, 2)}\n`;
                }
            }
        }
    }
});