const board = document.getElementById('board');
const cells = Array.from(board.children);
const result = document.getElementById('result');

let currentPlayer = 'X';
let gameEnded = false;
let board_list = ['', '', '', '', '', '', '', '', ''];

function checkWinner(board_list) {
    const data = {
        board: board_list
    };

    return fetch('http://127.0.0.1:8000/check_winner', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            if (data[0]) {
                if (data[1] === 'Draw') {
                    result.innerText = "It's a draw!";
                } else {
                    result.innerText = `${data[1]} wins!`;
                }
                gameEnded = true; // End the game
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}


function makeComputerMove(board_list) {
    if (!gameEnded) {
        const data = {
            board: board_list
        };

        // Simulate computer's move
        return fetch('http://127.0.0.1:8000/get-move', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text(); // Assuming the response body contains a plain integer
        })
        .then(moveIndex => {
            moveIndex = parseInt(moveIndex);
            // Introduce a delay of 3 seconds before placing 'O'
            setTimeout(() => {
                board_list[moveIndex] = 'O'; // Assign 'O' to the cell
                cells[moveIndex].innerText = 'O'; // Update the corresponding cell on the UI with 'O'
                checkWinner(board_list); // Check if the game has been won or ended in a draw
            }, 1000); // Delay in milliseconds
        })
        .catch(error => {
            console.error('Error:', error);
            // Handle error appropriately
        });
    }
}


function handleCellClick(index) {
    if (!gameEnded && !board_list[index]) {
        board_list[index] = currentPlayer;
        cells[index].innerText = currentPlayer;

        checkWinner(board_list).then(() => {
            if (!gameEnded) {
                makeComputerMove(board_list);
            }
        });
    }
}

cells.forEach((cell, index) => {
    cell.addEventListener('click', () => handleCellClick(index));
});
