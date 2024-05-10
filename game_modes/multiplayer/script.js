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
        }
        return data; // Return the result data
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function handleCellClick(index) {
    if (!gameEnded && !board_list[index]) {
        board_list[index] = currentPlayer;
        cells[index].innerText = currentPlayer;

        checkWinner(board_list).then(data => {
            if (data[0]) {
                gameEnded = true;
            } else {
                currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
            }
        });
        
    }
}

cells.forEach((cell, index) => {
    cell.addEventListener('click', () => handleCellClick(index));
});
