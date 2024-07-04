from flask import Flask, send_file
from flask_socketio import SocketIO, emit
import os
import sys
import threading

# un-wrapped
# class flask_server_wrapper:
app = Flask(__name__)
socketio = SocketIO(app)
testvar = 0
monitor = {"top": 100, "left": 100, "width": 800, "height": 800}  # Define capture area
key_input = ""
# fsw = ""

def start_server():
    global app
    threading.Thread(
        target=socketio.run,
        args=(app, '0.0.0.0', 3000),
        kwargs={'allow_unsafe_werkzeug': True}  # For development purposes
    ).start()
    global key_input
    key_input = "initial key input"
    
## Casting ####################################################################
def capture_and_stream(self):
    with mss.mss() as sct:
        while True:
            global monitor
            img = sct.grab(monitor)
            img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
            self.socketio.emit('screen_data', img.tobytes(), namespace='/screen') 
            # self.socketio.emit('screen_data', output.getvalue())

@socketio.on('connect', namespace='/screen')  # Add namespace
def handle_connect():
    # showTxt('Client connected')
    global socketio
    global capture_and_stream
    socketio.start_background_task(capture_and_stream)

@socketio.on('disconnect')
def handle_disconnect():
    pass
    # showTxt('Client disconnected')

@socketio.on('message')
def handle_message(message):
#        import pdb; pdb.set_trace()
    global key_input
    global key_source
    ki = key_input
    if ki == '':
        return
    key_source = "socketio"
    key_input = ''  # Reset key input
    if message[0:7]=='keyup':
        key_input = ''
    else:
    # elif message[0:7]=='keydown:':
        socket_key_input = message[8:9]
        if socket_key_input in {'a', 'd'}:
            key_input = socket_key_input.upper()
        else:
            pass

@app.route('/')
def index():
    return send_file('\\public\\index.html')


# a = flask_server_wrapper()
# print(f"a.key_input: {a.key_input}")
