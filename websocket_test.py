# import websockets
import asyncio
from websockets.sync.client import connect
from websockets.server import serve

def on_message(ws, message):
    print(message)  # Print the received message

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")
    
# websocket.enableTrace(True)  # Optional: Enable verbose logging
# ws = websocket.WebSocketApp("ws://localhost:3000",
#                             on_message=on_message,
#                             on_error=on_error,
#                             on_close=on_close)
# ws.on_open = on_open
# ws.run_forever() 

with connect("ws://localhost:8765") as websocket:
    websocket.send("Hello world!")
    message = websocket.recv()
    print(f"Received: {message}")