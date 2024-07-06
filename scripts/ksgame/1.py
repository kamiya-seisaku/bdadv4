from flask import Flask, send_file
from flask_socketio import SocketIO, emit
import shared_stuff as sf
import mss
from PIL import Image

# Import ScreenShareCamera
from screen_share import ScreenShareCamera


class flask_server_wrapper:
    app = Flask(__name__)
    socketio = SocketIO(app)
    testvar = 0
    monitor = {"top": 100, "left": 100, "width": 800, "height": 800}  

    def __init__(self):
        self.video_camera = ScreenShareCamera(**self.monitor)  # Initialize the camera

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
        self.socketio.start_background_task(self.capture_and_stream)

    @socketio.on('disconnect')
    def handle_disconnect():
        pass

    @socketio.on('message')
    def handle_message(message):
        # ... (your existing key handling logic remains the same)

    @app.route('/')
    def index():
        return send_file('..\\..\\public\\index.html')
