// to run the server: npm run devStart 
const express = require('express');
const app = express();
const https = require('http').createServer(app);
const WebSocket = require('ws');
const wss = new WebSocket.Server({ server:https });

// deviated from:
//  https://github.com/websockets/ws/blob/master/examples/express-session-parse/index.js
//  https://github.com/websockets/ws/blob/master/examples/express-session-parse/public/app.js

wss.on('connection', function (ws, request) {
  // const userId = request.session.userId;
  // map.set(userId, ws);

  ws.on('error', console.error);

  ws.on('message', function (message) {
    //
    // Here we can now use session parameters.
    //
    console.log(`on-connection: Received message ${message}`);
    // ws.send("server.js:send-message:"+message);
    ws.emit('server.js:emit-message:', JSON.stringify(message));


  });

  ws.on('close', function () {
    // map.delete(userId);
  });
});

wss.on('upgrade', function (request, socket, head) {
  console.log(`upgrade received`);

  if (!ws) {
    console.log('No WebSocket connection');
    return;
  };

  ws.send('Hello World!');
  console.log('Sent "Hello World!"');

  wss.removeListener('error', onSocketError);

  wss.handleUpgrade(request, socket, head, function (ws) {
    wss.emit('connection', ws, request);
  });
});

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
    // res.sendFile(__dirname + '/public/main.js');
});

https.listen(3000, () => console.log(`Lisening on port :3000`))
