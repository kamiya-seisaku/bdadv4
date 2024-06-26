## flask #####################################################################
### global variables
import bpy
import sys
from flask import Flask
from flask_socketio import SocketIO

from os import path as p
sys.path.append(p.join(p.dirname(bpy.data.filepath), "scripts\ksgame"))
import utils

## Utils ##################################################################
import bpy

previous_txt = ""

def showTxt(txt):
    global previous_txt
    if previous_txt == txt:
        return
    previous_txt = txt
    print(str(txt))
    text_obj_key = bpy.data.objects.get('ui.Text.key')
    text_obj_key.data.body = str(txt)    

class flask_server_wrapper_class:
    key_source = ""
    key_input = ""

    showTxt("flask_server_wrapper")
    
    app = Flask(__name__)
    showTxt(str(app))
    socketio = SocketIO(app)
    testvar = 0
    
    @socketio.on('connect')
    def handle_connect():
        showTxt('Client connected')

    @socketio.on('disconnect')
    def handle_disconnect():
        showTxt('Client disconnected')

    @socketio.on('message')
    def handle_message(message):
#        import pdb; pdb.set_trace()
        global key_input, key_source
        key_source = "socketio"
        showTxt(f'in flask_server_wrapper/handle_message, Received message {message}')
        showTxt(f'in flask_server_wrapper/handle_message, initial global key_input: {key_input}')
        key_input = ''  # Reset key input
        if message[0:7]=='keyup':
            key_input = ''
        else:
        # elif message[0:7]=='keydown:':
            socket_key_input = message[8:9]
            if socket_key_input in {'a', 'd'}:
                key_input = socket_key_input.upper()
                showTxt(f'in flask_server_wrapper, global key_input set:{key_input}')
            else:
                showTxt(f'Received non-a/d-message {message}')
                showTxt(f'key_input:{key_input}')
        showTxt(f'in flask_server_wrapper/handle_message, exiting global key_input: {key_input}')

    @app.route('/')
    def index():
        return send_file('..\\public\\index.html')
#        return send_file('../../public/index.html')

# test code
#c = flask_server_wrapper_class()
#print(str(c))