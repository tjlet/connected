const boardElement = document.getElementById('board');
const messageElement = document.getElementById('message');
const resetButton = document.getElementById('reset');

let board = Array(6).fill().map(() => Array(7).fill(0));

const drawBoard = () => {
    boardElement.innerHTML = '';
    board.forEach((row) => {
        row.forEach((cell) => {
            const cellDiv = document.createElement('div');
            cellDiv.className = 'cell' + (cell === 1 ? ' red' : cell === 2 ? ' yellow' : '');
            cellDiv.onclick = (e) => handleMove(row.indexOf(cell));
            boardElement.appendChild(cellDiv);
        });
    });
};

const handleMove = async (column) => {
    const response = await fetch(`/move/${column}`, { method: 'POST' });
    const data = await response.json();
    if (data.winner) {
        messageElement.innerText = `Player ${data.winner} wins!`;
    } else {
        messageElement.innerText = '';
    }
    board = data.board;
    drawBoard();
};

resetButton.onclick = async () => {
    const response = await fetch('/reset', { method: 'POST' });
    const data = await response.json();
    board = data.board;
    messageElement.innerText = '';
    drawBoard();
};

drawBoard();
