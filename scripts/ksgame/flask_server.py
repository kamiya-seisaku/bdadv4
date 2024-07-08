from flask import Flask, send_file, Response, render_template
from flask_socketio import SocketIO, emit
import shared_stuff as sf
import mss
from PIL import Image
from screen_share import ScreenShareCamera

## flask #####################################################################
class flask_server_wrapper:
    # showTxt("flask_server_wrapper")
  
    app = Flask(__name__)
    socketio = SocketIO(app)
    testvar = 0
    monitor = {"top": 100, "left": 100, "width": 800, "height": 800}  # Define capture area
    
    # def __init__(self):
    #     self.video_camera = ScreenShareCamera(**self.monitor)  # Initialize the camera

    def __init__(self):
        # Extract values as individual variables
        top = self.monitor["top"]
        left = self.monitor["left"]
        width = self.monitor["width"]
        height = self.monitor["height"]

        # Initialize the camera with positional arguments
        self.video_camera = ScreenShareCamera(top, left, width, height)

    def capture_and_stream(self):
        while True:
            frame = self.video_camera.get_frame()
            if frame is not None:
                self.socketio.emit('screen_data', frame, namespace='/screen')
            else:
                # If there's an issue capturing the frame, wait a short time and retry
                time.sleep(0.1) 

    @socketio.on('connect', namespace='/screen')
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
