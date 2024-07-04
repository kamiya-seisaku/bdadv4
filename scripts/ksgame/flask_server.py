from flask import Flask, send_file
from flask_socketio import SocketIO, emit
import shared_stuff as sf

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
        if sf.key_input_g == '':
            return
        sf.key_source_g = "socketio"
        sf.key_input_g = ''  # Reset key input
        if message[0:7]=='keyup':
            sf.key_input_g = ''
        else:
        # elif message[0:7]=='keydown:':
            socket_key_input = message[8:9]
            if socket_key_input in {'a', 'd'}:
                sf.key_input_g = socket_key_input.upper()
            else:
                pass

    @app.route('/')
    def index():
        return send_file('..\\..\\public\\index.html')
