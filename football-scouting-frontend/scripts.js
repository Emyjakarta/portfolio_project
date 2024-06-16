// scripts.js

import config from './config'; // Adjust the path based on your project structure

const apiUrl = config.apiUrl;

// Function to fetch and display players
function fetchPlayers() {
    fetch(`${apiUrl}/players`)
        .then(response => response.json())
        .then(data => {
            const playersContainer = document.getElementById('playersContainer');
            playersContainer.innerHTML = ''; // Clear previous content
            data.forEach(player => {
                const playerElement = document.createElement('div');
                playerElement.classList.add('player');
                playerElement.innerHTML = `
                    <h3>${player.firstName} ${player.lastName}</h3>
                    <p>Position: ${player.position}</p>
                    <p>Created At: ${player.createdAt}</p>
                    <p>Updated At: ${player.updatedAt}</p>
                `;
                playersContainer.appendChild(playerElement);
            });
        })
        .catch(error => console.error('Error fetching players:', error));
}

// Function to add a new player
function addPlayer(firstName, lastName, position) {
    const formData = {
        firstName: firstName,
        lastName: lastName,
        position: position
    };

    fetch(`${apiUrl}/players`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Successfully added player:', data);
        fetchPlayers(); // Refresh player list after adding
    })
    .catch(error => console.error('Error adding player:', error));
}

// Event listener for form submission
document.getElementById('addPlayerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const position = document.getElementById('position').value;
    addPlayer(firstName, lastName, position);
});

// Initial fetch of players when page loads
fetchPlayers();

