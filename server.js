const express = require('express')
const app = express()
const https = require('http').createServer(app);
const WebSocket = require('ws');
const wss = new WebSocket.Server({ server:https });

// deviated from:
//  https://github.com/websockets/ws/blob/master/examples/express-session-parse/index.js
//  https://github.com/websockets/ws/blob/master/examples/express-session-parse/public/app.js

wss.on('upgrade', function (request, socket, head) {
  // socket.on('error', onSocketError);

  // console.log('Parsing session from request...');

  // sessionParser(request, {}, () => {
  if (!ws) {
    console.log('No WebSocket connection');
    return;
  };

  ws.send('Hello World!');
  console.log('Sent "Hello World!"');

  // if (!request.session.userId) {
  //   socket.write('HTTP/1.1 401 Unauthorized\r\n\r\n');
  //   socket.destroy();
  //   return;
  // };

  // console.log('Session is parsed!');

  wss.removeListener('error', onSocketError);

  wss.handleUpgrade(request, socket, head, function (ws) {
    wss.emit('connection', ws, request);
  });
});

wss.on('connection', function (ws, request) {
  // const userId = request.session.userId;
  // map.set(userId, ws);

  ws.on('error', console.error);

  ws.on('message', function (message) {
    //
    // Here we can now use session parameters.
    //
    console.log(`Received message ${message}`);
  });

  ws.on('close', function () {
    // map.delete(userId);
  });
});

// wss.on('connection', function (ws) {
//   const id = setInterval(function () {
//     ws.send(JSON.stringify(process.memoryUsage()), function () {
//       //
//       // Ignore errors.
//       //
//     });
//     // console.log('interval running');
//   }, 100);
//   console.log('started client interval');

//   ws.on('error', console.error);

//   ws.on('close', function () {
//     console.log('stopping client interval');
//     clearInterval(id);
//   });
// });

// app.get('/', (req, res) => res.send('Hello World!'))
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
    // res.sendFile(__dirname + '/public/main.js');
});

https.listen(3000, () => console.log(`Lisening on port :3000`))

// const express = require('express');
// const app = express();
// const http = require('http');
// const webServer = http.createServer(app);
// const { Server: socketServer } = require('socket.io');
// const io = new socketServer(webServer);
// const path = require('path');
// const { WebSocket } = require('ws');
// const ws = new WebSocket(webServer);

// app.use(express.static(path.join(__dirname, 'public')));

// app.get('/', (req, res) => {
//     res.sendFile(__dirname + '/public/index.html');
// });

// function showMessage(message) {
//     window.setTimeout(() => window.alert(message), 50);
// }


// const connect4 = require('./connect4');

// function receiveMoves(board, websocket) {
//     websocket.addEventListener("message", ({ data }) => {
//         const event = JSON.parse(data);
//         switch (event.type) {
//         case "play":
//             // Update the UI with the move.
//             connect4.playMove(board, event.player, event.column, event.row);
//             break;
//         case "win":
//             showMessage(`Player ${event.player} wins!`);
//             // No further messages are expected; close the WebSocket connection.
//             websocket.close(1000);
//             break;
//         case "error":
//             showMessage(event.message);
//             break;
//         default:
//             throw new Error(`Unsupported event type: ${event.type}.`);
//         }
//     });
// }
    
// function sendMoves(board, websocket) {
//     // When clicking a column, send a "play" event for a move in that column.
//     board.addEventListener("click", ({ target }) => {
//       const column = target.dataset.column;
//       // Ignore clicks outside a column.
//       if (column === undefined) {
//         return;
//       }
//       const event = {
//         type: "play",
//         column: parseInt(column, 10),
//       };
//       websocket.send(JSON.stringify(event));
//     });
// }

//   // window.addEventListener("DOMContentLoaded", () => {
// app.on('event:DOMContentLoaded', () => {
//       // Initialize the UI.
//     const board = document.querySelector(".board");
//     connect4.createBoard(board);
//     // Open the WebSocket connection and register event handlers.
//     const websocket = new WebSocket("ws://localhost:/");
//     receiveMoves(board, websocket);
//     sendMoves(board, websocket);
// });


// // io.on("connection", (socket) => {
// //     // ...
// // });
  
// // io.listen(8080);

// webServer.listen(3000, () => {
//     console.log('Listening on *:3000');
// });
