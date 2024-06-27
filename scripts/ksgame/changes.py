# ... (imports remain the same)

# Streaming related libraries (Note: `mss` is not Flask-specific, it's for screen capture)
import mss
from PIL import Image

# ... (global variables remain the same)

class FlaskServerWrapper:
    # ... (other methods remain largely the same)

    def capture_and_stream(self):
        with mss.mss() as sct:
            while True:
                img = sct.grab(self.monitor)
                img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")

                # No need for io.BytesIO() here, Flask can directly send the image data
                self.socketio.emit('screen_data', img.tobytes(), namespace='/screen') 

    @socketio.on('connect', namespace='/screen')  # Add namespace
    def handle_connect():
        showTxt('Client connected')
        self.socketio.start_background_task(self.capture_and_stream)  # Use self.capture_and_stream
   
    # ... (handle_disconnect and handle_message remain the same)

# ... (ModalTimerOperator remains largely the same)

def execute(self, context):
    # Start the web server in a separate thread
    threading.Thread(
        target=self.fsw.socketio.run,
        args=(self.fsw.app, '0.0.0.0', 3000),
        kwargs={'allow_unsafe_werkzeug': True}  # For development purposes
    ).start()
    
    # ... (rest of execute method remains the same)

# ... (rest of the code remains the same)
