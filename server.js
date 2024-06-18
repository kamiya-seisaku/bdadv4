const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require('socket.io');
const io = new Server(server);
const path = require('path');

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});

function showMessage(message) {
    window.setTimeout(() => window.alert(message), 50);
}


const connect4 = require('./connect4');

function receiveMoves(board, websocket) {
    websocket.addEventListener("message", ({ data }) => {
        const event = JSON.parse(data);
        switch (event.type) {
        case "play":
            // Update the UI with the move.
            connect4.playMove(board, event.player, event.column, event.row);
            break;
        case "win":
            showMessage(`Player ${event.player} wins!`);
            // No further messages are expected; close the WebSocket connection.
            websocket.close(1000);
            break;
        case "error":
            showMessage(event.message);
            break;
        default:
            throw new Error(`Unsupported event type: ${event.type}.`);
        }
    });
}
    
function sendMoves(board, websocket) {
    // When clicking a column, send a "play" event for a move in that column.
    board.addEventListener("click", ({ target }) => {
      const column = target.dataset.column;
      // Ignore clicks outside a column.
      if (column === undefined) {
        return;
      }
      const event = {
        type: "play",
        column: parseInt(column, 10),
      };
      websocket.send(JSON.stringify(event));
    });
  }

  // window.addEventListener("DOMContentLoaded", () => {
  app.on('event:DOMContentLoaded', () => {
      // Initialize the UI.
    const board = document.querySelector(".board");
    connect4.createBoard(board);
    // Open the WebSocket connection and register event handlers.
    const websocket = new WebSocket("ws://localhost:8001/");
    receiveMoves(board, websocket);
    sendMoves(board, websocket);
  });

server.listen(3000, () => {
    console.log('Listening on *:3000');
});
