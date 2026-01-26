// bitboards
let x = 0;
let o = 0;
let state = 0;

const boardDiv = document.getElementById("board");

// render the board
function renderBoard() {
  boardDiv.innerHTML = "";
  for (let i = 0; i < 9; i++) {
    const cell = document.createElement("div");
    cell.className = "cell";
    
    // check bitboards for X or O
    if (x & (1 << i)) cell.textContent = "X";
    else if (o & (1 << i)) cell.textContent = "O";
    else cell.textContent = "";

    // on click, make a move if empty
    cell.onclick = () => playerMove(i);
    boardDiv.appendChild(cell);
  }
}

function playerMove(i) {
// Prevent clicking an already occupied square
if ((state & (1 << i)) !== 0) return;

// Send POST with the clicked cell
fetch("http://127.0.0.1:5000/move", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ x, o, state, action: i })  // action = clicked cell
})
.then(res => res.json())
.then(data => {
    x = data.x;
    o = data.o;
    state = data.state;
    renderBoard();

    if (data.winner) alert("Winner: " + data.winner);
});
}

// initial render
renderBoard();