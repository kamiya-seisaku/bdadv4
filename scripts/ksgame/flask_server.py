from flask import Flask, send_file
from flask_socketio import SocketIO, emit

## flask #####################################################################
class flask_server_wrapper:
    # showTxt("flask_server_wrapper")
  
    app = Flask(__name__)
    socketio = SocketIO(app)
    testvar = 0
    monitor = {"top": 100, "left": 100, "width": 800, "height": 800}  # Define capture area
    
    ## Casting ####################################################################
    def capture_and_stream(self):
        with mss.mss() as sct:
            while True:
                img = sct.grab(self.monitor)
                img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
                self.socketio.emit('screen_data', img.tobytes(), namespace='/screen') 
                # self.socketio.emit('screen_data', output.getvalue())

    @socketio.on('connect', namespace='/screen')  # Add namespace
    def handle_connect():
        # showTxt('Client connected')
        self.socketio.start_background_task(self.capture_and_stream)

    @socketio.on('disconnect')
    def handle_disconnect():
        pass
        # showTxt('Client disconnected')

    @socketio.on('message')
    def handle_message(message):
#        import pdb; pdb.set_trace()
        global key_input, key_source
        if key_input == '':
            return
        key_source = "socketio"
        # showTxt(f'in flask_server_wrapper/handle_message, Received message {message}')
        # showTxt(f'in flask_server_wrapper/handle_message, initial global key_input: {key_input}')
        key_input = ''  # Reset key input
        if message[0:7]=='keyup':
            key_input = ''
        else:
        # elif message[0:7]=='keydown:':
            socket_key_input = message[8:9]
            if socket_key_input in {'a', 'd'}:
                key_input = socket_key_input.upper()
                # showTxt(f'in flask_server_wrapper, global key_input set:{key_input}')
            else:
                # showTxt(f'Received non-a/d-message {message}')
                # showTxt(f'key_input:{key_input}')
                # showTxt(f'in flask_server_wrapper/handle_message, exiting global key_input: {key_input}')
                pass

    @app.route('/')
    def index():
        return send_file('..\\public\\index.html')
