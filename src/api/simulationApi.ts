const API_BASE_URL = 'http://localhost:8000';  // Adjust this to match your API server address

export const startSimulation = async (numStates: number, maxSteps: number) => {
    const response = await fetch(`${API_BASE_URL}/simulate`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ num_states: numStates, max_steps: maxSteps }),
    });
    return response.json();
};

export const getResults = async () => {
    const response = await fetch(`${API_BASE_URL}/results`);
    return response.json();
};

export const connectWebSocket = (onMessage: (data: any) => void) => {
    const ws = new WebSocket(`wss://${window.location.hostname}/ws`);
    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        onMessage(data);
    };
    return ws;
};